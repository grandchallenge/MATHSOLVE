# ERDOS-470-N4: bounded historical-interface investigation

State: `EXACT_SOURCE_GAP_WITH_NEW_PINNED_LEAD`; no full search or certification.

The author owns an older [weird-odd-engine repository](https://github.com/fwjmath/weird-odd-engine). It was exported from Google Code and has five main-branch commits dated 3 March 2013. The inspected head is `6ba33a63217b60f8e2a8583929078eec3c454d8f`; the wiki branch is `19d0b67f6c544c155046e1c86c94cb3d878e08cb`.

This is **not** the missing first-batch DFS executable. `weirdodd.cpp` reads two scalar bounds from `inp.txt`, restores a two-value `(n, checksum)` checkpoint and scans selected residue classes modulo 30. Its source header limits applicability to numbers below `2^63`, preferably below `10^18`. The archived `ows-data@88d22faf46400f0050287c3c32c9a807ca3b1340` workunits instead have seven header scalars and a variable-depth prime-power traversal state. The later `wobt-smart.cpp` consumes nine header scalars. No parser padding or engine substitution is justified by these different interfaces.

## Lower-band provenance

The prior missing band now has an identified author-origin statement: [OEIS A006037](https://oeis.org/A006037) attributes exclusion below `1.8*10^19` to Wenjie Fang on 4 September 2013, and the later `10^21` announcement to Fang on 23 February 2014. This explains the archived lower-bound value as a plausible predecessor boundary. It does not supply the predecessor's executable, interval manifest or replay receipts, and the old repository's documented `2^63` range does not cover that entire bound.

The [project's news archive](https://www.rechenkraft.net/yoyo/all_news.php) records testing from August 2013, a Windows XP result-validation bug fixed in September 2013, and completion of the first batch in February 2014. The [March 2014 author/operator discussion](https://www.rechenkraft.net/forum/viewtopic.php?f=57&t=14219) describes a separate restart after a checkpoint bug in the second batch. A historical replay therefore needs batch- and version-specific validation evidence; a later executable and a terminal marker cannot substitute for it.

## Exact local falsification and its limit

The legacy program comments that every abundant number in its range should be divisible by 3 or 7; its `primes.txt` begins with 7 and its residue-5/25 branches require divisibility by that prime. The integer

`n = 366005822969340125 = 5^3 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47`

lies between `10^17` and `10^18`, is divisible by neither 3 nor 7, and has

`sigma(n) = 732732840109670400 > 2n`, with abundance `721194170990150`.

The exact verifier proves primality of the displayed factors by trial division, verifies the product and divisor-sum formula, and checks six distinct proper divisors summing to the abundance:

`707941630501625 + 13249079564501 + 3453874853 + 7043185 + 5945 + 41`.

Consequently this integer **is semiperfect**, by complementing those six divisors within the complete proper-divisor set. It is not an odd weird number. The certificate falsifies the broad comment and exhibits a skipped abundant input; it does not prove the engine's target exclusion false. Any reliance on the legacy scanner still needs a general justification that its skipped families are safely pseudoperfect.

## Archive reconciliation and public recovery pass

The [2018 case study](https://doi.org/10.1007/s10723-017-9411-5), Table 1 (page 655), reports 41,776 first-batch lineages and 527,191 workunits. Its server model validates at least two replicas by byte comparison, and its OWS discussion notes locally completed large workunits. Those records are relevant to the missing coverage and validation provenance.

The read-only reconciliation of all 183 pinned archives checks each archive's Git blob and SHA-256 identity before parsing. It finds 527,827 records: 485,384 `t` and 42,443 `c`. There are exactly 41,776 distinct `c` payloads and 476,638 distinct `t` payloads. The completed-payload count agrees with the published lineage count; total records exceed the published workunit count by 636. Neither observation supplies an interval cover or replayed historical checksums.

The [project's filename documentation](https://www.rechenkraft.net/wiki/index.php?title=Yoyo%40home_en) identifies the three numerical filename tokens as remaining sections, running number in the batch and creation timestamp. Grouping only by the batch running number yields 41,777 observed groups, 36,622 without a `c` and 2,000 with multiple distinct `c` payloads. Thus treating that number as a persistent lineage identity is unjustified without the generator and recycle mapping.

The [2022 author paper](https://arxiv.org/html/2207.12906) points back to `fwjmath/ows-data` for code and data. The live repository has one branch, no tags or releases, and only one source-code addition. The public Google Code source archive for `weird-odd-engine` has SHA-256 `b2bbcc372462434d3c394b082b35ce1e3736c85ee64dfbe76458451ae3d41d4a`; its inventory contains the older direct scanner and auxiliary code, not the seven-field tree engine or generator. The [surviving project download directory](https://www.rechenkraft.net/yoyo/download/download/ows/) supplies a March 2014 ZIP with `app_info.xml` and `wobt-smart-sandy-boinc.exe`, declaring app version 102. Its ZIP SHA-256 is `5ee5c1c91748da3cd02bf5dbf33e4cdd5637a51def6bd5ff98bebfb4ac01b1df`; it was inspected without execution. The public source directory lists ECM, evolution, Muon and OGR, with no OWS source entry. A bounded public archive query returned no matching 2013 OWS/weird/wobt download captures. No exact first-batch engine was recovered in this public pass.

## Exact recovery request, prepared but not sent

Please supply the first-batch August 2013–February 2014 seven-field search-tree source/executable and workunit generator, their version/checksum identities, the initial and recycled DFS interval manifests (including locally completed workunits), replica-comparison receipts and the validation history following the September 2013 Windows fix. Please identify how the 41,776 lineages and 527,191 published workunits map to the 527,827 archived records, including the 41,776 distinct completed payloads, and explain the running-number identity across recycling. Please also identify the implementation and interval/replay evidence for the predecessor exclusion below `1.8*10^19`. The public older direct scanner and later nine-field `wobt-smart.cpp` do not match the archived seven-field traversal records. No exhaustive rerun is requested.
