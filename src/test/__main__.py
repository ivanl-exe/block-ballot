from toml import load
from ballot import Ballot

ELECTION = 'test/toml/election.toml'

if __name__ == '__main__':
    ballot = Ballot()
    with open(ELECTION, 'r') as file:
        candidates = load(file)
    ballot.announce(candidates, until = -1)
    ballot.submit()