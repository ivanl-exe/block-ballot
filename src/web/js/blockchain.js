$().ready(() => {
    eel.beginBallot()(() => {
        eel.getBallots()(([ballots, scores]) => {
            const blockchainItem = $($(".blockchain-item").get(1));
            for(const [ballotHash, ballot] of Object.entries(ballots)) {
                const ballotItem = appendItem("div", "blockchain-ballot-item", blockchainItem);
                const ballotHashItem = appendItem("div", "blockchain-ballot-hash-item", ballotItem)
                const ballotBlockchainHash = appendItem("p1", "blockchain-hash", ballotHashItem);
                ballotBlockchainHash.text(ballotHash);
                const config = ballot['config'];
                const candidates = ballot['candidates'];
                for(const [candidateHash, candidate] of Object.entries(candidates)) {
                    const ballotCandidateHashItem = appendItem("div", "blockchain-ballot-candidate-hash-item", ballotItem);
                    const ballotCandidateHash = appendItem("p1", "blockchain-hash", ballotCandidateHashItem);
                    ballotCandidateHash.text(candidateHash);
                    const ballotCandidate = appendItem("div", "blockchain-ballot-candidate-item", ballotItem);
                    for(const [key, values] of Object.entries(candidate)) {
                        const ballotCandidatePair = appendItem("div", "blockchain-ballot-candidate-pair-item", ballotCandidate);
                        const ballotCandidateKey = appendItem("p1", "blockchain-ballot-candidate-key", ballotCandidatePair);
                        ballotCandidateKey.text(key);
                        const ballotCandidateValues = appendItem("div", "blockchain-ballot-candidates-values", ballotCandidatePair);
                        for(const value of values) {
                            const ballotCandidateValue = appendItem("div", value.type, ballotCandidateValues);
                            ballotCandidateValue.text(value.value);
                        }
                    }
                }
            }
        });
    });
});

const appendItem = (element, _class, _parent) => {
    const _id = generateID();
    $(`<${element}>`, { id: _id, class: _class }).appendTo(_parent);
    return _parent.children(`#${_id}`);
}