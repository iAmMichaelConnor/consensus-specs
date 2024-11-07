# Mike's installation notes:

Because I have no idea how python works:

Make sure python3 and pip3 are installed:

Clone this repo. Then:

`cd consensus-specs`

`sudo apt update`

`sudo apt install python3-pip`

`pip3 --version`

`python3 --version`

`sudo apt install python3.12-venv`

Set up a `venv`. It's like a safe place to run python code:

`python3 -m venv venv` <-- this creates a little folder called `venv` where a load of installation stuff will get dumped.

`source venv/bin/activate`

When you're done working in the virtual environment, you can deactivate it by running:

`deactivate`

Now use commands `venv/bin/python` and `venv/bin/pip` instead of `python3` and `pip3`, when within this consensus-specs dir

Now install some stuff that they specified in a txt file, and maybe also some other stuff and hope for the best:

`venv/bin/pip install -r requirements_preinstallation.txt`

(maybe `venv/bin/python setup.py install` , although I didn't do this the first time)

Install linting and testing stuff (to see the words you can write, look at setup.py, down at the bottom it says "extras_require"):

`venv/bin/pip install .[test,lint]`

To install the repo, there's a setup.py file. I'm just shooting from the hip, here.

Run:

`venv/bin/pip install .`

`venv/bin/python setup.py` install seemed to work, to then be able to import and execute stuff!

Maybe we've done enough. Maybe we installed too much. I don't know. I then had this scratchpad where I explored and learned about blobs. It includes lots of commented out stuff. It looks like it's currently just printing the roots of unity to a file, Noir formatted:

**Important command to run play.py**:

`venv/bin/python play.py`

To install the tests from the eth consensus specs code, run:

`make install_test`

(maybe: `python setup.py pyspecdev`)?

`cd ./tests/core/pyspec`

`python -m pytest --preset=minimal ./eth2spec/test/deneb/unittests/polynomial_commitments/test_polynomial_commitments.py`

or to run a specific function in a test (where `test_verify_kzg_proof_impl_incorrect_proof` is the name of the function):

`python -m pytest --preset=minimal -k test_verify_kzg_proof_impl_incorrect_proof eth2spec`

Hmmm then it looks like I've tried to distill it into a smaller set of commands, but no idea if these would work without the other random commands above:

sudo apt update
sudo apt install python3-pip
pip3 --version
python3 --version
sudo apt install python3.12-venv

python3 -m venv venv

source venv/bin/activate

venv/bin/pip install eth2spec
venv/bin/pip list

venv/bin/python play.py

---

# Ethereum Proof-of-Stake Consensus Specifications

[![Join the chat at https://discord.gg/qGpsxSA](https://img.shields.io/badge/chat-on%20discord-blue.svg)](https://discord.gg/qGpsxSA)

To learn more about proof-of-stake and sharding, see the [PoS documentation](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/), [sharding documentation](https://ethereum.org/en/upgrades/sharding/) and the [research compendium](https://notes.ethereum.org/s/H1PGqDhpm).

This repository hosts the current Ethereum proof-of-stake specifications. Discussions about design rationale and proposed changes can be brought up and discussed as issues. Solidified, agreed-upon changes to the spec can be made through pull requests.

## Specs

[![GitHub release](https://img.shields.io/github/v/release/ethereum/eth2.0-specs)](https://github.com/ethereum/eth2.0-specs/releases/) [![PyPI version](https://badge.fury.io/py/eth2spec.svg)](https://badge.fury.io/py/eth2spec)

Core specifications for Ethereum proof-of-stake clients can be found in [specs](specs/). These are divided into features.
Features are researched and developed in parallel, and then consolidated into sequential upgrades when ready.

### Stable Specifications

| Seq. | Code Name                                                                    | Fork Epoch | Specs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---- | ---------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0    | **Phase0**                                                                   | `0`        | <ul><li>Core</li><ul><li>[The beacon chain](specs/phase0/beacon-chain.md)</li><li>[Deposit contract](specs/phase0/deposit-contract.md)</li><li>[Beacon chain fork choice](specs/phase0/fork-choice.md)</li></ul><li>Additions</li><ul><li>[Honest validator guide](specs/phase0/validator.md)</li><li>[P2P networking](specs/phase0/p2p-interface.md)</li><li>[Weak subjectivity](specs/phase0/weak-subjectivity.md)</li></ul></ul>                                                                                                                                                                                                                                                   |
| 1    | **Altair**                                                                   | `74240`    | <ul><li>Core</li><ul><li>[Beacon chain changes](specs/altair/beacon-chain.md)</li><li>[Altair fork](specs/altair/fork.md)</li></ul><li>Additions</li><ul><li>[Light client sync protocol](specs/altair/light-client/sync-protocol.md) ([full node](specs/altair/light-client/full-node.md), [light client](specs/altair/light-client/light-client.md), [networking](specs/altair/light-client/p2p-interface.md))</li><li>[Honest validator guide changes](specs/altair/validator.md)</li><li>[P2P networking](specs/altair/p2p-interface.md)</li></ul></ul>                                                                                                                           |
| 2    | **Bellatrix** <br/> (["The Merge"](https://ethereum.org/en/upgrades/merge/)) | `144896`   | <ul><li>Core</li><ul><li>[Beacon Chain changes](specs/bellatrix/beacon-chain.md)</li><li>[Bellatrix fork](specs/bellatrix/fork.md)</li><li>[Fork choice changes](specs/bellatrix/fork-choice.md)</li></ul><li>Additions</li><ul><li>[Honest validator guide changes](specs/bellatrix/validator.md)</li><li>[P2P networking](specs/bellatrix/p2p-interface.md)</li></ul></ul>                                                                                                                                                                                                                                                                                                          |
| 3    | **Capella**                                                                  | `194048`   | <ul><li>Core</li><ul><li>[Beacon chain changes](specs/capella/beacon-chain.md)</li><li>[Capella fork](specs/capella/fork.md)</li></ul><li>Additions</li><ul><li>[Light client sync protocol changes](specs/capella/light-client/sync-protocol.md) ([fork](specs/capella/light-client/fork.md), [full node](specs/capella/light-client/full-node.md), [networking](specs/capella/light-client/p2p-interface.md))</li></ul><ul><li>[Validator additions](specs/capella/validator.md)</li><li>[P2P networking](specs/capella/p2p-interface.md)</li></ul></ul>                                                                                                                            |
| 4    | **Deneb**                                                                    | `269568`   | <ul><li>Core</li><ul><li>[Beacon Chain changes](specs/deneb/beacon-chain.md)</li><li>[Deneb fork](specs/deneb/fork.md)</li><li>[Polynomial commitments](specs/deneb/polynomial-commitments.md)</li><li>[Fork choice changes](specs/deneb/fork-choice.md)</li></ul><li>Additions</li><ul><li>[Light client sync protocol changes](specs/deneb/light-client/sync-protocol.md) ([fork](specs/deneb/light-client/fork.md), [full node](specs/deneb/light-client/full-node.md), [networking](specs/deneb/light-client/p2p-interface.md))</li></ul><ul><li>[Honest validator guide changes](specs/deneb/validator.md)</li><li>[P2P networking](specs/deneb/p2p-interface.md)</li></ul></ul> |

### In-development Specifications

| Code Name or Topic                    | Specs                                                                                                                                                                                                                                                                                                                       | Notes                                                                                                                       |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Electra                               | <ul><li>Core</li><ul><li>[Beacon Chain changes](specs/electra/beacon-chain.md)</li><li>[EIP-6110 fork](specs/electra/fork.md)</li></ul><li>Additions</li><ul><li>[Honest validator guide changes](specs/electra/validator.md)</li></ul></ul>                                                                                |
| Sharding (outdated)                   | <ul><li>Core</li><ul><li>[Beacon Chain changes](specs/_features/sharding/beacon-chain.md)</li></ul><li>Additions</li><ul><li>[P2P networking](specs/_features/sharding/p2p-interface.md)</li></ul></ul>                                                                                                                     |
| Custody Game (outdated)               | <ul><li>Core</li><ul><li>[Beacon Chain changes](specs/_features/custody_game/beacon-chain.md)</li></ul><li>Additions</li><ul><li>[Honest validator guide changes](specs/_features/custody_game/validator.md)</li></ul></ul>                                                                                                 | Dependent on sharding                                                                                                       |
| Data Availability Sampling (outdated) | <ul><li>Core</li><ul><li>[Core types and functions](specs/_features/das/das-core.md)</li><li>[Fork choice changes](specs/_features/das/fork-choice.md)</li></ul><li>Additions</li><ul><li>[P2P Networking](specs/_features/das/p2p-interface.md)</li><li>[Sampling process](specs/_features/das/sampling.md)</li></ul></ul> | <ul><li> Dependent on sharding</li><li>[Technical explainer](https://hackmd.io/@HWeNw8hNRimMm2m2GH56Cw/B1YJPGkpD)</li></ul> |

### Accompanying documents can be found in [specs](specs) and include:

- [SimpleSerialize (SSZ) spec](ssz/simple-serialize.md)
- [Merkle proof formats](ssz/merkle-proofs.md)
- [General test format](tests/formats/README.md)

## Additional specifications for client implementers

Additional specifications and standards outside of requisite client functionality can be found in the following repos:

- [Beacon APIs](https://github.com/ethereum/beacon-apis)
- [Engine APIs](https://github.com/ethereum/execution-apis/tree/main/src/engine)
- [Beacon Metrics](https://github.com/ethereum/beacon-metrics/)

## Design goals

The following are the broad design goals for the Ethereum proof-of-stake consensus specifications:

- to minimize complexity, even at the cost of some losses in efficiency
- to remain live through major network partitions and when very large portions of nodes go offline
- to select all components such that they are either quantum secure or can be easily swapped out for quantum secure counterparts when available
- to utilize crypto and design techniques that allow for a large participation of validators in total and per unit time
- to allow for a typical consumer laptop with `O(C)` resources to process/validate `O(1)` shards (including any system level validation such as the beacon chain)

## Useful external resources

- [Design Rationale](https://notes.ethereum.org/s/rkhCgQteN#)
- [Phase 0 Onboarding Document](https://notes.ethereum.org/s/Bkn3zpwxB)
- [Combining GHOST and Casper paper](https://arxiv.org/abs/2003.03052)

## For spec contributors

Documentation on the different components used during spec writing can be found here:

- [YAML Test Generators](tests/generators/README.md)
- [Executable Python Spec, with Py-tests](tests/core/pyspec/README.md)

## Online viewer of the latest release (latest `master` branch)

[Ethereum Consensus Specs](https://ethereum.github.io/consensus-specs/)

## Consensus spec tests

Conformance tests built from the executable python spec are available in the [Ethereum Proof-of-Stake Consensus Spec Tests](https://github.com/ethereum/consensus-spec-tests) repo. Compressed tarballs are available in [releases](https://github.com/ethereum/consensus-spec-tests/releases).
