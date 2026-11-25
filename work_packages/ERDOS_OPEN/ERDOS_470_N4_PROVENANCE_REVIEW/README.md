# ERDOS-470-N4 historical provenance review candidate

Read `470_HISTORICAL_INTERFACE_REVIEW.md` for the exact findings, limits and prepared recovery request. The seven-field historical engine and exhaustive coverage are still missing. No exclusion bound or solution is certified.

Run `python verify_provenance.py` to check this packet's hashes and claim boundaries.

For a fresh read-only inspection, clone `https://github.com/fwjmath/ows-data` into a scratch directory and detach at `88d22faf46400f0050287c3c32c9a807ca3b1340`. Run `python 470_lineage_provenance_audit.py --source /absolute/path/to/ows-data --output /absolute/path/to/fresh-audit.json` and compare the reported counts and source identities. This scans the 183 compressed first-batch archives, without executing a search engine or extracting their members to disk.

Clone `https://github.com/fwjmath/weird-odd-engine` and detach at `6ba33a63217b60f8e2a8583929078eec3c454d8f`. Run `python 470_legacy_pruning_certificate.py --source /absolute/path/to/weird-odd-engine --output /absolute/path/to/fresh-certificate.json`. The exact integer certificate refutes an overbroad code comment; its integer is semiperfect and does not refute the odd-weird exclusion.

The older Google Code archive and the 2014 optimized binary are recorded by source URL and content identity. Neither is substituted for the first-batch engine. No historical binary was executed, and no recovery request was sent.
