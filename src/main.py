import eel
from classifier import TypeClassifier
from ballot import Ballot
from util.datatype import ndepth_defaultdict
from blockchain import Blockchain
from toml import load

WEB_ROOT = 'web'
WEB_FILENAME = 'index.html'

@eel.expose
def beginBallot() -> None:
    global typeClassifier
    typeClassifier = TypeClassifier()
    global ballot
    ballot = Ballot()
    with open('test/toml/election.toml', 'r') as file:
        ballot.announce(load(file), -1)
    ballot.submit()

@eel.expose
def getBallots() -> dict:
    ballots = ndepth_defaultdict(4, list)
    scores = ndepth_defaultdict(1, int)
    #ignore genesis block
    for block in ballot.blockchain.chain[1:]:
        for txn in block.data:
            data = txn.data
            ballot_hash = Blockchain.__encode__(txn.hash)
            try:
                _type = data['type']
                data = data['data']
                if _type == Ballot.BALLOT:
                    until = data['until']
                    ballots[ballot_hash]['config'].update({'until': until})
                elif _type == Ballot.CANDIDATE:
                    for candidate_hash, candidate in data.items():
                        candidate_hash = Blockchain.__encode__(candidate_hash)
                        for key, value in candidate.items():
                            if type(value) == list or type(value) == tuple: value = ' '.join(map(lambda s: str(s), value))
                            else: value = str(value)
                            classes = typeClassifier.classify(value)
                            for _class in classes: ballots[candidate_hash]['candidates'][ballot_hash][key].append(vars(_class))
                elif _type == Ballot.VOTE:
                    scores[ballot_hash] += 1
            except Exception as e:
                print(e)
    return (ballots, scores)

if __name__ == '__main__':
    eel.init(WEB_ROOT)
    eel.start(WEB_FILENAME, port = 8000)