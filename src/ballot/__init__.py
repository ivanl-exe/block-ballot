from typing import Union
from blockchain import Blockchain

class Candidate:
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        for key, value in kwargs.items():
            self.__attribute__(key, value)
    
    def __attribute__(self, key, value) -> None:
        self.__dict__[key] = value

class Data:
    def __init__(self, type: str, data: dict) -> None:
        self.type = type
        self.data = data

class Ballot(Candidate):
    BALLOT = ELECTION = 'ballot'
    CANDIDATE = 'candidate'
    VOTE = 'vote'

    def __init__(self) -> None:
        self.blockchain = Blockchain()
        self.blockchain.difficulty = 2
    
    def announce(self, candidates: Union[list[Candidate], dict], until: int) -> list[bytes]:
        if type(candidates) == dict: candidates = [Candidate(name, **values) for name, values in candidates.items()]
        
        #Announce an election
        data = Data(type = Ballot.BALLOT, data = {'until': until})
        txn = self.blockchain.transaction(vars(data))
        ballot_hash = txn.hash

        #Announce candidates
        for candidate in candidates:
            data = Data(type = Ballot.CANDIDATE, data = {ballot_hash: vars(candidate)})
            self.blockchain.transaction(vars(data))

    def submit(self) -> None:
        while len(self.blockchain.pool) > 0:
            nonce = Blockchain.nonce()
            hash = self.blockchain.add_block(nonce)

    def vote(self, candidate: str) -> None:
        data = Data(type = Ballot.VOTE, data = {Ballot.CANDIDATE: candidate})
        self.blockchain.transaction(vars(data))

    def candidates(self) -> dict:
        pass