# LLM4UT extraction data

Study-level data for the **228 included studies** in the revised survey of LLM-based unit testing. Literature cutoff: **through August 2026**. Data snapshot: **23 September 2026**.

## Contents

- `studies.csv`: bibliographic information, coded analytical fields and public source/artifact links. One row per study.
- `statistics.csv`: descriptive counts, denominators and fractions, recomputed from studies.csv.
- `memberships.csv`: study IDs contributing to each category, linking statistics to the study records.
- `recompute.py`: standalone Python 3 script to regenerate the two derived CSV files.

All CSV files are UTF-8 with BOM. There are no Excel files, primary-paper PDFs, private review notes or local filesystem references in this package.

## Field definitions and RQ mapping

| Field | Definition | Main use |
|---|---|---|
| study_id | Stable study identifier; gaps in numbering are intentional. | All RQs |
| publication_year | Publication year used in the review, not necessarily the first preprint year. | RQ1 |
| title | Title in the included-study inventory. | RQ1 |
| venue | Recorded publication venue. This is not a separate verification of peer-review status. | RQ1 |
| ccf_2026 | Recorded CCF 2026 venue classification. | RQ1 |
| languages | Programming languages of the software under test; multiple labels possible. | RQ1 |
| tasks | Top-level unit testing tasks; multiple labels possible. | RQ2 |
| task_subcategories | Recorded finer-grained task categories where available. | RQ2 |
| study_types | Contribution types, e.g. Approach, Empirical, Benchmark, Dataset. | RQ2 |
| models | Normalized model labels used for the review statistics. | RQ3 |
| strategies | Training and prompting strategy labels. | RQ3 |
| strategy_parents | Training/prompting parent categories and explicit status labels. | RQ3 |
| integrated_techniques | Traditional techniques and associated workflow labels combined with LLMs. | RQ3 |
| generation_metrics | Reported metric categories for Test Generation studies; not performance values. | RQ2 |
| benchmarks | Reported benchmark/dataset names and brief role descriptions. | RQ2 |
| training_datasets | Reported training-data descriptions where available. | RQ3 |
| tool_names | Reported approach/tool names. | RQ2/RQ3 |
| source_links | Public links to primary studies. | All RQs |
| artifact_links | Recorded public code/data links; not necessarily complete implementations. | RQ1 |
| code_availability_group | Recorded artifact-access classification. | RQ1 |
| code_audit_date | Date of the artifact availability assessment, distinct from the literature cutoff. | RQ1 |

RQ4 synthesizes challenges and opportunities across studies. It is not generated automatically from category frequencies.

## Counting and coding conventions

1. **Population:** 228 included studies. Excluded records are not included in the files.
2. **Multiple labels:** each study is counted once per distinct label in each dimension. Multi-label categories overlap. Strategy parent counts are not sums of child counts.
3. **Denominators:** `study_fraction = study_count / study_denominator`. The denominator is 228, except generation metrics, which use the 144 Test Generation studies. `assignment_fraction` instead divides by the total number of category memberships in the dimension. Fractions are on a 0--1 scale; multiply by 100 for percentages. Do not mix these denominators.
4. **Missing values:** blanks mean not coded in the released record, not necessarily absent from the paper. `Not reported` means not reported; `Not applicable` means not applicable. Explicitly unspecified labels remain unspecified; none are replaced by zero or inferred into a more specific category.
5. **Task hierarchy:** Test Oracle Generation is a top-level task containing assertion-related work. Do not add assertion subcategory counts to that parent count. Test Augmentation concerns adding tests; Test Evolution concerns updating tests with software changes. These are distinct from test repair and bug reproduction as coded.
6. **Models:** normalized model labels concern the investigated approach or directly studied internal configurations; purely external method baselines are excluded under the review's coding convention. These files do not provide a complete inventory of every baseline or exact model snapshot. `model_family` contains four distinct-study unions used in the model display (Claude, Gemini, Phi and Gemma), matched by name prefix. Do not add a family count to its constituent variants or call the mixed labels distinct model architectures.
7. **Strategies:** Full FT, PEFT, RL and Pre-training are training labels. Zero-shot, Few-shot, CoT, ToT and GToT are prompting labels. `Fine-tuning (type unspecified)` is not Full FT. `Other prompting` is a residual specific-category label, not a distinct prompting method. Reuse/no-new-experiment and not-reported labels are status information rather than extra technical categories.
8. **Techniques:** auxiliary workflow and status labels are preserved. They are not automatically plotted as traditional techniques. Execution feedback alone does not establish reinforcement-learning training.
9. **Metrics:** metric usage frequency is not evidence of comparative effectiveness. Code Coverage is a broad category and should not be added to line/branch coverage as if mutually exclusive. Training datasets are not evaluation datasets.
10. **Artifact availability:** accessible code does not establish a complete implementation or successful reproduction. Checks reflect the recorded audit date, not necessarily availability at the literature cutoff. URLs were not rechecked when this snapshot was packaged.

Artifact status labels:

| Label | Meaning |
|---|---|
| Verified implementation or experimental code | Implementation or experimental code verified accessible. |
| Partial implementation or auxiliary code | Partial implementation or auxiliary code verified accessible. |
| Accessible author code not verified | Accessible author code not verified. |
| Code claimed by authors; accessibility unverified | Authors claim code, but access was not verified. |

## Recompute

Run in this directory:

```sh
python3 recompute.py
```

The script uses only the Python standard library and overwrites statistics.csv and memberships.csv. It does not alter studies.csv, re-search literature, re-read papers or reclassify studies.

## Analytical scope

The dimensions support publication/year and venue summaries, the programming-language table, task distribution (Fig. 5), model distribution (Fig. 6), utilization strategies (Fig. 7), integrated techniques (Fig. 8), generation metrics (Fig. 9), and artifact availability. Figure numbering may change with manuscript revisions.

This package supplies **descriptive-distribution data**, not the historical database-search logs or performance-comparison results for SWT, TestBench, assertion benchmarks, or independently executed experiments. Counts should be calculated from the records rather than copied from an older figure. The release does not represent a new full-text audit.

## Rights and citation

Primary papers and linked code/data retain their original rights and licenses. No third-party full text is redistributed. The data are released under the repository's CC BY 4.0 license (see LICENSE at the repository root). When citing these data, cite the survey and the repository release or commit used for the analysis.
