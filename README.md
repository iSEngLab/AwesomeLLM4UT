<h1 align="center">🤖 Awesome LLM for UT</h1>
<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://arxiv.org/abs/2506.15227"><img src="https://img.shields.io/badge/arXiv-2506.15227-blue.svg" alt="Paper"></a>
  <img src="https://img.shields.io/github/stars/iSEngLab/AwesomeLLM4UT?color=yellow&amp;label=Stars" alt="Stars">
  <img src="https://img.shields.io/badge/PRs-Welcome-red" alt="PRs welcome">
  <img src="https://img.shields.io/github/last-commit/iSEngLab/AwesomeLLM4UT" alt="Last commit">
</p>

A collection of studies on large language models for unit testing, accompanying **Large Language Models for Unit Testing: A Systematic Literature Review**.

The revised collection contains **228 unique studies** with a literature cutoff of **1 September 2026**. This repository snapshot was updated on **23 September 2026**. The linked 2025 manuscript is an earlier version; the data below describe the revised collection.

## Contents

- [Citation](#citation)
- [Papers by Unit Testing Task](#papers-by-unit-testing-task)
  - [Test Generation (144)](#test-generation)
  - [Test Oracle Generation (37)](#test-oracle-generation)
  - [Test Augmentation (15)](#test-augmentation)
  - [Bug Reproduction (14)](#bug-reproduction)
  - [Test Evolution (13)](#test-evolution)
  - [Test Repair (6)](#test-repair)
  - [Test Smell Detection (4)](#test-smell-detection)
  - [Test Readability Improvement (4)](#test-readability-improvement)
  - [Test Completion (3)](#test-completion)
  - [Test Migration (2)](#test-migration)
  - [Test Minimization (2)](#test-minimization)
  - [Test Refactoring (2)](#test-refactoring)
  - [Test-to-Code Traceability (1)](#test-to-code-traceability)
- [Related Surveys](#related-surveys)
- [Star History](#star-history)
- [Extraction Data](#extraction-data)

## Citation

```bibtex
@misc{zhang2025llm4ut,
  title={Large Language Models for Unit Testing: A Systematic Literature Review},
  author={Zhang, Quanjun and Fang, Chunrong and Gu, Siqi and Shang, Ye and Chen, Zhenyu and Xiao, Liang},
  year={2025},
  eprint={2506.15227},
  archivePrefix={arXiv},
  primaryClass={cs.SE},
  url={https://arxiv.org/abs/2506.15227}
}
```

## Papers by Unit Testing Task

Studies may address multiple tasks and therefore appear in more than one section below. There are 247 task memberships across the 228 unique studies. Assertion generation is included under Test Oracle Generation, alongside whole-oracle and exceptional-oracle generation.

### Test Generation

144 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Advancing Code Coverage: Incorporating Program Analysis with Large Language Models](https://arxiv.org/pdf/2404.04966) | 2026 | TOSEM |
| 2 | [ATGen: Adversarial Reinforcement Learning for Test Case Generation](https://proceedings.iclr.cc/paper_files/paper/2026/file/eed25c037bc08afcbefab6f7a6b700e0-Paper-Conference.pdf) | 2026 | ICLR |
| 3 | [Auditing and Decomposing Feedback-Driven Evolution in LLM Test Generation under the Oracle Problem](https://arxiv.org/html/2608.19626v1) | 2026 | arXiv |
| 4 | [Automated Unit Test Generation via Chain-of-Thought Prompt and Reinforcement Learning from Coverage Feedback](https://dl.acm.org/doi/full/10.1145/3745765) | 2026 | TOSEM |
| 5 | [Benchmarking LLMs for Unit Test Generation from Real-World Functions](https://discovery.ucl.ac.uk/id/eprint/10223971/1/3805043.pdf) | 2026 | TOSEM |
| 6 | [Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects](https://arxiv.org/html/2607.12068v1) | 2026 | COMPSAC |
| 7 | [Boosting unit test generation via structure-aware fine-tuning of pre-trained model](https://doi.org/10.1016/j.infsof.2025.107948) | 2026 | IST |
| 8 | [BreakGuard: Towards Detecting Dependency Breaking Changes with LLM-Generated Tests](https://arxiv.org/html/2608.20167v1) | 2026 | arXiv |
| 9 | [Call-Chain-Aware LLM-Based Test Generation for Java Projects](https://arxiv.org/pdf/2604.22046v1) | 2026 | arXiv |
| 10 | [CASCADE: Detecting Inconsistencies between Code and Documentation with Automatic Test Generation](https://arxiv.org/html/2604.19400v1) | 2026 | FSE |
| 11 | [CGTest: A hybrid coverage-guided framework for cost-effective unit test generation](https://doi.org/10.1016/j.jss.2026.113055) | 2026 | JSS |
| 12 | [CITYWALK: Enhancing LLM-Based C++ Unit Test Generation via Project-Dependency Awareness and Language-Specific Knowledge](https://zhangyw.work/file/papers/Zhang2026TOSEM_B.pdf) | 2026 | TOSEM |
| 13 | [CogPath: A Constraint-Guided Context-Reduction Framework for LLM-Based Test Generation](https://xutangzhi.github.io/assets/pdf/scam2026-cogpath.pdf) | 2026 | SCAM |
| 14 | [Consistency Meets Verification: Enhancing Test Generation Quality in Large Language Models Without Ground-Truth Solutions](https://arxiv.org/html/2602.10522v1) | 2026 | ICST |
| 15 | [Context Matters: Improving the Practical Reliability of LLM-Based Unit Test Generation](https://arxiv.org/html/2607.19682v1) | 2026 | ISSTA |
| 16 | [Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate With Their Effectiveness?](https://arxiv.org/html/2607.22880v1) | 2026 | ISSTA |
| 17 | [Enabling Global, Human-Centered Explanations for LLMs: From Tokens to Interpretable Code and Test Generation](https://arxiv.org/html/2503.16771v3) | 2026 | ICSE |
| 18 | [Evaluating and Mitigating the Misguidance Effect of Buggy Code in LLM-Generated Unit Tests](https://arxiv.org/html/2607.22883v1) | 2026 | ISSTA |
| 19 | [From Greedy Steps to Global Optimization: Learning Sequential Test Suite Generation](https://arxiv.org/html/2604.01799v2) | 2026 | ISSTA |
| 20 | [Fusing LLMs and Genetic Algorithm for High-Quality Unit Test Generation](https://doi.org/10.1145/3819237) | 2026 | TOSEM |
| 21 | [Generating Project-Specific Test Cases with Requirement Validation Intention](https://arxiv.org/html/2507.20619v4) | 2026 | ISSTA |
| 22 | [Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation](https://arxiv.org/html/2506.02943v7) | 2026 | TOSEM |
| 23 | [HieraTest: Hierarchical Dependency-Driven Framework with Multi-Strategy Repair for LLM-Based Unit Test Generation](https://doi.org/10.1109/SANER67736.2026.00013) | 2026 | SANER |
| 24 | [How well LLM-based test generation techniques perform with newer LLM versions?](https://arxiv.org/html/2601.09695v2) | 2026 | ICST |
| 25 | [Impact of code context and prompting strategies on automated unit test generation with modern general-purpose large language models](https://arxiv.org/html/2507.14256v1) | 2026 | JSS |
| 26 | [Improving LLM-Based Unit Test Generation Through Root-Cause-Driven Prompt Design](https://doi.org/10.1109/AITest70988.2026.00021) | 2026 | AITest |
| 27 | [JSTestCraft: Addressing Context Deficits in JavaScript Unit Test Generation via Agentic Multi-Level Contextual Analysis](https://doi.org/10.1145/3828725) | 2026 | TOSEM |
| 28 | [Knowledge Matters: Injecting Project and Testing Knowledge into LLM-based Unit Test Generation](https://arxiv.org/html/2511.14224v3) | 2026 | ICSE |
| 29 | [Knowledge-Guided Synthetic Bug Feedback for LLM-Based Unit Test Generation](https://arxiv.org/html/2607.11573v1) | 2026 | arXiv |
| 30 | [Learning to Generate Unit Test via Adversarial Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/file/efb02f96766a3b599c76852abf4d42dd-Paper-Conference.pdf) | 2026 | ICLR |
| 31 | [Less Is More: Failing Test Generation with Large Language Models](https://dl.acm.org/doi/full/10.1145/3793675) | 2026 | TOSEM |
| 32 | [Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware](https://arxiv.org/html/2606.19725v2) | 2026 | arXiv |
| 33 | [LLM Test Generation via Iterative Hybrid Program Analysis](https://arxiv.org/html/2503.13580v2) | 2026 | ICSE |
| 34 | [LLM vs. Human Unit Tests: Fault Detection on Real Python Bugs](https://arxiv.org/html/2606.08588v1) | 2026 | arXiv |
| 35 | [LLM-Based Detection and Test Generation for Command Injection Vulnerabilities in Python](https://arxiv.org/abs/2505.15088) | 2026 | AITest |
| 36 | [LLM-Based Invariant Testing for Software Functional Bugs](https://arxiv.org/html/2607.18711v1) | 2026 | ISSRE |
| 37 | [LSPRAG: LSP-Guided RAG for Language-Agnostic Real-Time Unit Test Generation](https://arxiv.org/html/2510.22210v2) | 2026 | ICSE |
| 38 | [MACO: Multi-agent collaborative optimization for unit test case generation](https://doi.org/10.1016/j.infsof.2026.108098) | 2026 | IST |
| 39 | [Measuring the Influence of Incorrect Code on Test Generation](https://arxiv.org/html/2409.09464v3) | 2026 | ICSE |
| 40 | [MR-Coupler: Automated Metamorphic Test Generation via Functional Coupling Analysis](https://arxiv.org/html/2604.10126v2) | 2026 | FSE |
| 41 | [Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows](https://arxiv.org/html/2607.09101v1) | 2026 | arXiv |
| 42 | [MultiFileTest: A Multi-File-Level LLM Unit Test Generation Benchmark and Impact of Error Fixing Mechanisms](https://aclanthology.org/2026.findings-acl.1403.pdf) | 2026 | ACL |
| 43 | [Mutation-Guided Unit Test Generation With a Large Language Model](https://arxiv.org/html/2506.02954v8) | 2026 | TSE |
| 44 | [Ockhamareto: Pareto-Gated Segment-Level Credit Assignment for Concise Unit-Test Generation with Reinforcement Learning](https://arxiv.org/html/2608.24473v1) | 2026 | arXiv |
| 45 | [On the risk of coding before testing: An empirical study on LLM-based test generation workflow](https://arxiv.org/abs/2607.05139) | 2026 | arXiv |
| 46 | [Optimizing Context and Cost in LLM ‐Based Unit Test Generation: A Study on External Dependency Retrieval Strategies](https://doi.org/10.1111/exsy.70401) | 2026 | Expert Systems |
| 47 | [PALM: Path-aware LLM-based Test Generation with Comprehension](https://arxiv.org/html/2506.19287v2) | 2026 | ICPC |
| 48 | [Planning to Explore: Curiosity-Driven Planning for LLM Test Generation](https://arxiv.org/html/2604.05159v1) | 2026 | arXiv |
| 49 | [Prompt engineering in LLMs for automated unit test generation: A large-scale study](https://orbilu.uni.lu/bitstream/10993/68099/1/s10664-026-10840-4.pdf) | 2026 | EMSE |
| 50 | [Reference-Based Retrieval-Augmented Unit Test Generation](https://gaoxiang9430.github.io/papers/TOSEM25_RefTest.pdf) | 2026 | TOSEM |
| 51 | [Retrieval-Augmented Test Generation: How Far Are We?](https://arxiv.org/pdf/2409.12682v2) | 2026 | ICSE |
| 52 | [Retrieval-Augmented Unit Test Suggestion Generation](https://doi.org/10.1145/3821423) | 2026 | TOSEM |
| 53 | [RM-RF: Reward Model for Run-Free Unit Test Evaluation](https://arxiv.org/html/2601.13097v1) | 2026 | SANER |
| 54 | [SCATE: Learning to Supervise Coding Agents for Cost-Effective Test Generation](https://arxiv.org/html/2607.08983v1) | 2026 | arXiv |
| 55 | [Synthesizing File-Level Data for Unit Test Generation with Chain-of-Thoughts via Self-Debugging](https://arxiv.org/html/2602.03181v1) | 2026 | ASE |
| 56 | [TATG: Tracking-Aware Testing Objective for LLM-based Test Generation](https://arxiv.org/html/2607.03194v1) | 2026 | arXiv |
| 57 | [Test smells in LLM-Generated Unit Tests](https://arxiv.org/html/2410.10628v3) | 2026 | TOSEM |
| 58 | [Test vs Mutant: Adversarial LLM Agents for Robust Unit Test Generation](https://arxiv.org/html/2602.08146v3) | 2026 | ISSTA |
| 59 | [TestBench: Evaluating Class-Level Test Case Generation Capability of Large Language Models](https://arxiv.org/pdf/2409.17561v1) | 2026 | FCS |
| 60 | [TestForge: Benchmarking LLM-Based Test Case Generation](https://doi.org/10.1109/SANER67736.2026.00014) | 2026 | SANER |
| 61 | [Testora: Using Natural Language Intent to Detect Behavioral Regressions](https://arxiv.org/html/2503.18597) | 2026 | ICSE |
| 62 | [TestWeaver: Execution-aware, Feedback-driven Regression Testing Generation with Large Language Models](https://arxiv.org/html/2508.01255v2) | 2026 | ICSE |
| 63 | [The Quality of Claude AI-authored Python Tests Is Not Weaker Than Human-authored Tests](https://arxiv.org/html/2608.15188v1) | 2026 | arXiv |
| 64 | [Type-aware LLM-based Test Generation for Python Programs](https://arxiv.org/html/2503.14000v2) | 2026 | TOSEM |
| 65 | [Uncovering Business Logic Bugs via Semantics-Driven Unit Test Generation](https://arxiv.org/html/2604.23509v2) | 2026 | ISSTA |
| 66 | [VALTEST: Automated Validation of Language Model Generated Test Cases](https://arxiv.org/pdf/2411.08254v3) | 2026 | TSE |
| 67 | [XREPOTEST: Benchmarking Multilingual Repository-Level Unit Test Generation for Large Language Models](https://arxiv.org/abs/2608.25939v1) | 2026 | arXiv |
| 68 | [A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing](https://arxiv.org/pdf/2412.16620) | 2025 | ISSTA |
| 69 | [AgentTester: An LLM-Based Tool for Unit Test Generation with Automatically Generated Prompts](https://doi.org/10.1007/978-981-95-0011-6_10) | 2025 | ICIC |
| 70 | [ASTER: Natural and Multi-language Unit Test Generation with LLMs](https://arxiv.org/pdf/2409.03093v2) | 2025 | ICSE |
| 71 | [Automating Autograding: Large Language Models as Test Suite Generators for Introductory Programming](https://arxiv.org/pdf/2411.09261) | 2025 | JCAL |
| 72 | [CasModaTest: A Cascaded and Model-agnostic Self-directed Framework for Unit Test Generation](https://arxiv.org/html/2406.15743v1) | 2025 | ISSRE |
| 73 | [Clarifying Semantics of In-Context Examples for Unit Test Generation](https://arxiv.org/html/2510.01994v1) | 2025 | ASE |
| 74 | [Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning](https://arxiv.org/html/2506.03136v2) | 2025 | NeurIPS |
| 75 | [CoverUp: Effective High Coverage Test Generation for Python](https://raw.githubusercontent.com/plasma-umass/coverup-eval/main/CoverUp.pdf) | 2025 | FSE |
| 76 | [CUBETESTERAI: Automated JUnit Test Generation Using the LLaMA Model](https://arxiv.org/html/2504.15286v1) | 2025 | ICST |
| 77 | [DiffuTester: Accelerating Unit Test Generation for Diffusion LLMs via Mining Structural Pattern](https://arxiv.org/html/2509.24975v3) | 2025 | arXiv |
| 78 | [Dynamic Scaling of Unit Tests for Code Reward Modeling](https://aclanthology.org/2025.acl-long.343.pdf) | 2025 | ACL |
| 79 | [Enhancing Large Language Models for Text-to-Testcase Generation](https://arxiv.org/pdf/2402.11910v2) | 2025 | JSS |
| 80 | [Enhancing LLM's Ability to Generate More Repository-Aware Unit Tests Through Precise Contextual Information Injection](https://arxiv.org/html/2501.07425v1) | 2025 | ASE |
| 81 | [Enriching Automatic Test Case Generation by Extracting Relevant Test Inputs from Bug Reports](https://link.springer.com/article/10.1007/s10664-025-10635-z) | 2025 | EMSE |
| 82 | [exLong: Generating Exceptional Behavior Tests with Large Language Models](https://users.ece.utexas.edu/~gligoric/papers/ZhangETAL25exLong.pdf) | 2025 | ICSE |
| 83 | [FuzzAug: Data Augmentation by Coverage-guided Fuzzing for Neural Test Generation](https://aclanthology.org/2025.findings-emnlp.847.pdf) | 2025 | EMNLP |
| 84 | [Learning to Generate Unit Tests for Automated Debugging](https://arxiv.org/html/2502.01619v3) | 2025 | COLM |
| 85 | [Less is More: On the Importance of Data Quality for Unit Test Generation](https://xing-hu.github.io/assets/papers/FSE25CleanTest.pdf) | 2025 | FSE |
| 86 | [LLM Based Input Space Partitioning Testing for Library APIs](https://zhendong2050.github.io/res/icse25.pdf) | 2025 | ICSE |
| 87 | [LLM-enhanced evolutionary test generation for untyped languages](https://doi.org/10.1007/s10515-025-00496-7) | 2025 | AUSE |
| 88 | [LLM-Powered Test Case Generation for Detecting Bugs in Plausible Programs](https://aclanthology.org/2025.acl-long.20.pdf) | 2025 | ACL |
| 89 | [LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework](https://arxiv.org/html/2511.20403v2) | 2025 | ASE |
| 90 | [Navigating the Labyrinth: Path-Sensitive Unit Test Generation with Large Language Models](https://arxiv.org/html/2509.23812v2) | 2025 | ASE |
| 91 | [PALM: Synergizing Program Analysis and LLMs to Enhance Rust Unit Test Coverage](https://arxiv.org/pdf/2506.09002v3) | 2025 | ASE |
| 92 | [PyTester: Deep Reinforcement Learning for Text-to-Testcase Generation](https://arxiv.org/pdf/2401.07576v2) | 2025 | JSS |
| 93 | [Reflective Unit Test Generation for Precise Type Error Detection with Large Language Models](https://arxiv.org/html/2507.02318v2) | 2025 | ASE |
| 94 | [Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation](https://arxiv.org/html/2412.14308v1) | 2025 | DeepTest |
| 95 | [RUG: Turbo LLM for Rust Unit Test Generation](https://taesoo.kim/pubs/2025/cheng:rug.pdf) | 2025 | ICSE |
| 96 | [Seed&Steer: Guiding Large Language Models with Compilable Prefix and Branch Signals for Unit Test Generation](https://arxiv.org/html/2507.17271v1) | 2025 | arXiv |
| 97 | [STRUT: Structured Seed Case Guided Unit Test Generation for C Programs using LLMs](https://doi.org/10.1145/3728970) | 2025 | ISSTA |
| 98 | [Test Intention Guided LLM-based Unit Test Generation](https://doi.org/10.1109/ICSE55347.2025.00243) | 2025 | ICSE |
| 99 | [Test Wars: A Comparative Study of SBST, Symbolic Execution, and LLM-Based Approaches to Unit Test Generation](https://arxiv.org/html/2501.10200v1) | 2025 | ICST |
| 100 | [TESTEVAL: Benchmarking Large Language Models for Test Case Generation](https://aclanthology.org/2025.findings-naacl.197.pdf) | 2025 | NAACL |
| 101 | [TestForge: Feedback-Driven, Agentic Test Suite Generation](https://arxiv.org/html/2503.14713v1) | 2025 | arXiv |
| 102 | [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf) | 2025 | ICLR |
| 103 | [TestLoter: A logic-driven framework for automated unit test generation and error repair using large language models](https://doi.org/10.1016/j.cola.2025.101348) | 2025 | JCL |
| 104 | [The Prompt Alchemist: Automated LLM-Tailored Prompt Optimization for Test Case Generation](https://arxiv.org/pdf/2501.01329) | 2025 | arXiv |
| 105 | [The Role of Test Repair in LLM-Based Unit Test Generation](https://arxiv.org/html/2507.18316v1) | 2025 | arXiv |
| 106 | [TRACETS4J: A Traceable Unit Test Generation Dataset](https://doi.org/10.1109/SANER64311.2025.00077) | 2025 | SANER |
| 107 | [Unify and Triumph: Polyglot, Diverse, and Self-Consistent Generation of Unit Tests with LLMs](https://arxiv.org/html/2503.16144v1) | 2025 | arXiv |
| 108 | [What You See Is What You Get: Attention-based Self-guided Automatic Unit Test Generation](https://arxiv.org/html/2412.00828v1) | 2025 | ICSE |
| 109 | [A3Test: Assertion-Augmented Automated Test Case Generation](https://researchmgt.monash.edu/ws/files/629132543/621302447-oa.pdf) | 2024 | IST |
| 110 | [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation](https://www.franktip.org/pubs/testpilot2024.pdf) | 2024 | TSE |
| 111 | [An LLM-based Readability Measurement for Unit Tests' Context-aware Inputs](https://arxiv.org/pdf/2407.21369v2) | 2024 | arXiv |
| 112 | [ChatGPT vs SBST: A Comparative Assessment of Unit Test Suite Generation](https://eprints.gla.ac.uk/324030/3/324030.pdf) | 2024 | TSE |
| 113 | [ChatUniTest: A Framework for LLM-Based Test Generation](https://arxiv.org/pdf/2305.04764) | 2024 | FSE |
| 114 | [Code-Aware Prompting: A study of Coverage Guided Test Generation in Regression Setting using LLM](https://arxiv.org/pdf/2402.00097v2) | 2024 | FSE |
| 115 | [CPP-UT-Bench: Can LLMs Write Complex Unit Tests in C++?](https://www.nutanix.com/content/dam/nutanix/en/resources/white-papers/wp-cpp-ut-bench.pdf) | 2024 | NeurIPS |
| 116 | [Design choices made by LLM-based test generators prevent them from finding bugs](https://arxiv.org/html/2412.14137v1) | 2024 | arXiv |
| 117 | [Effective test generation using pre-trained Large Language Models and mutation testing](https://arxiv.org/pdf/2308.16557v1) | 2024 | IST |
| 118 | [Evaluating and Improving ChatGPT for Unit Test Generation](https://mingwei-liu.github.io/assets/pdf/FSE24_chatTester_cameraReady.pdf) | 2024 | FSE |
| 119 | [Evaluation of Large Language Models for Unit Test Generation](https://doi.org/10.1109/ASYU62119.2024.10756954) | 2024 | ASYU |
| 120 | [Harnessing the Power of LLMs: Automating Unit Test Generation for High-Performance Computing](https://arxiv.org/pdf/2407.05202v1) | 2024 | arXiv |
| 121 | [HITS: High-coverage LLM-based Unit Test Generation via Method Slicing](https://arxiv.org/pdf/2408.11324v1) | 2024 | ASE |
| 122 | [Large Language Models as Test Case Generators: Performance Evaluation and Enhancement](https://arxiv.org/pdf/2404.13340) | 2024 | arXiv |
| 123 | [LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation](https://www.seas.upenn.edu/~asnaik/assets/papers/tse24_ticoder.pdf) | 2024 | TSE |
| 124 | [LLM4VV: Developing LLM-driven testsuite for compiler validation](https://arxiv.org/pdf/2310.04963) | 2024 | FGCS |
| 125 | [On the Evaluation of Large Language Models in Unit Test Generation](https://arxiv.org/pdf/2406.18181) | 2024 | ASE |
| 126 | [Optimizing Search-Based Unit Test Generation with Large Language Models: An Empirical Study](https://doi.org/10.1145/3671016.3674813) | 2024 | Internetware |
| 127 | [Parameter-Efficient Fine-Tuning of Large Language Models for Unit Test Generation: An Empirical Study](https://arxiv.org/html/2411.02462v2) | 2024 | arXiv |
| 128 | [TestART: Improving LLM-based Unit Test via Co-evolution of Automated Generation and Repair Iteration](https://arxiv.org/pdf/2408.03095v6) | 2024 | arXiv |
| 129 | [TestSpark: IntelliJ IDEA's Ultimate Test Generation Companion](https://pure.tudelft.nl/ws/portalfiles/portal/206515056/3639478.3640024.pdf) | 2024 | ICSE |
| 130 | [The Program Testing Ability of Large Language Models for Code](https://aclanthology.org/2024.emnlp-industry.3.pdf) | 2024 | EMNLP |
| 131 | [Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation](https://raw.githubusercontent.com/CGCL-codes/PathEval/main/PathEval_Preprint.pdf) | 2024 | ASE |
| 132 | [Unit Test Generation using Generative AI : A Comparative Performance Analysis of Autogeneration Tools](https://arxiv.org/pdf/2312.10622v2) | 2024 | LLM4Code |
| 133 | [Unit Test Generation using Large Language Models for Unity Game Development](https://www.researchgate.net/publication/382296611_Unit_Test_Generation_using_Large_Language_Models_for_Unity_Game_Development) | 2024 | FaSE4Games |
| 134 | [UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing](https://haochen.org/publications/he2024unitsyn.pdf) | 2024 | ISSTA |
| 135 | [Using GitHub Copilot for Test Generation in Python: An Empirical Study](https://azaidman.github.io/publications/elhajiAST2024.pdf) | 2024 | AST |
| 136 | [Using Large Language Models to Generate JUnit Tests: An Empirical Study](https://joannacss.github.io/preprints/ease24-preprint.pdf) | 2024 | EASE |
| 137 | [An initial investigation of ChatGPT unit test generation capability](https://repositorio.ufscar.br/server/api/core/bitstreams/a05e89b4-b1ef-40fe-a42a-95cad4a0f5f8/content) | 2023 | SAST |
| 138 | [CAT-LM Training Language Models on Aligned Code And Tests](https://arxiv.org/pdf/2310.01602) | 2023 | ASE |
| 139 | [CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models](https://www.microsoft.com/en-us/research/uploads/prod/2023/03/codamosa_icse23.pdf) | 2023 | ICSE |
| 140 | [CodeT: Code Generation with Generated Tests](https://arxiv.org/pdf/2207.10397) | 2023 | ICLR |
| 141 | [Exploring the Capability of ChatGPT in Test Generation](https://reu.techconf.org/document/01-Publications/Exploring%20the%20Capability%20of%20ChatGPT%20in%20Test%20Generation.pdf) | 2023 | QRS |
| 142 | [Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting](https://arxiv.org/html/2304.11686v6) | 2023 | ASE |
| 143 | [Prompting Code Interpreter to Write Better Unit Tests on Quixbugs Functions](https://arxiv.org/pdf/2310.00483) | 2023 | arXiv |
| 144 | [Unit Test Case Generation with Transformers and Focal Context](https://arxiv.org/pdf/2009.05617) | 2021 | arXiv |

### Test Oracle Generation

37 studies.

This category includes 28 assertion-oracle, 7 whole-oracle and 2 exceptional-oracle studies. The subcategory for each study is recorded in the data.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Agent-Based Test Assertion Generation via Diverse Perspective Aggregation](https://arxiv.org/html/2608.05822v1) | 2026 | arXiv |
| 2 | [Documentation vs. Code Patterns: What Drives LLM-Based Exception Oracle Generation?](https://arxiv.org/html/2608.00884v1) | 2026 | ASE |
| 3 | [Escaping the Self-Repair Trap: Improving Test Oracle Generation via Dual-Context Awareness](https://arxiv.org/html/2608.05917v1) | 2026 | ASE |
| 4 | [Fail-Aware and Explainable Test Oracle Prediction](https://arxiv.org/html/2607.11342v1) | 2026 | arXiv |
| 5 | [From Business Requirements to Test Assertions: Evaluating LLM-Generated Oracles on Real Bugs](https://arxiv.org/html/2607.10277v1) | 2026 | arXiv |
| 6 | [Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation](https://arxiv.org/html/2506.02943v7) | 2026 | TOSEM |
| 7 | [LLM-Based Invariant Testing for Software Functional Bugs](https://arxiv.org/html/2607.18711v1) | 2026 | ISSRE |
| 8 | [A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing](https://arxiv.org/pdf/2412.16620) | 2025 | ISSTA |
| 9 | [AsserT5: Test Assertion Generation Using a Fine-Tuned Code Language Model](https://arxiv.org/html/2502.02708v1) | 2025 | AST |
| 10 | [AssertionBench: A Benchmark to Evaluate Large-Language Models for Assertion Generation](https://aclanthology.org/2025.findings-naacl.449.pdf) | 2025 | NAACL |
| 11 | [AugmenTest: Enhancing Tests with LLM-Driven Oracles](https://arxiv.org/html/2501.17461v1) | 2025 | ICST |
| 12 | [ChatAssert: LLM-based Test Oracle Generation with External Tools Assistance](https://ihayet.github.io/assets/pdf/chatassert.pdf) | 2025 | TSE |
| 13 | [DeCon: Detecting Incorrect Assertions via Postconditions Generated by a Large Language Model](https://arxiv.org/html/2501.02901v1) | 2025 | arXiv |
| 14 | [Do LLMs Generate Useful Test Oracles? An Empirical Study with an Unbiased Dataset](https://homes.cs.washington.edu/~mernst/pubs/neurosymbolic-oracles-ase2025.pdf) | 2025 | ASE |
| 15 | [Doc2OracLL: Investigating the Impact of Documentation on LLM-based Test Oracle Generation](https://arxiv.org/pdf/2412.09360) | 2025 | FSE |
| 16 | [exLong: Generating Exceptional Behavior Tests with Large Language Models](https://users.ece.utexas.edu/~gligoric/papers/ZhangETAL25exLong.pdf) | 2025 | ICSE |
| 17 | [Exploring Automated Assertion Generation via Large Language Models](https://dl.acm.org/doi/full/10.1145/3699598) | 2025 | TOSEM |
| 18 | [FuzzAug: Data Augmentation by Coverage-guided Fuzzing for Neural Test Generation](https://aclanthology.org/2025.findings-emnlp.847.pdf) | 2025 | EMNLP |
| 19 | [Improving Deep Assertion Generation via Fine-Tuning Retrieval-Augmented Pre-trained Language Models](https://arxiv.org/html/2502.16071v1) | 2025 | TOSEM |
| 20 | [Improving Retrieval-Augmented Deep Assertion Generation via Joint Training](https://arxiv.org/html/2502.10696v2) | 2025 | TSE |
| 21 | [Nexus: Execution-Grounded Multi-Agent Test Oracle Synthesis](https://arxiv.org/html/2510.26423v1) | 2025 | arXiv |
| 22 | [Retrieval-Augmented Fine-Tuning for Improving Retrieve-and-Edit Based Assertion Generation](https://yanmeng.github.io/papers/TSE251.pdf) | 2025 | TSE |
| 23 | [TOGLL: Correct and Strong Test Oracle Generation with LLMs](https://arxiv.org/pdf/2405.03786) | 2025 | ICSE |
| 24 | [Tratto: A Neuro-Symbolic Approach to Deriving Axiomatic Test Oracles](https://arxiv.org/html/2504.04251v1) | 2025 | ISSTA |
| 25 | [An Empirical Study on Focal Methods in Deep-Learning-Based Approaches for Assertion Generation](https://dl.acm.org/doi/full/10.1145/3660785) | 2024 | FSE |
| 26 | [Assessing Evaluation Metrics for Neural Test Oracle Generation](https://www.eecs.yorku.ca/~wangsong/papers/tse24.pdf) | 2024 | TSE |
| 27 | [Chat-like Asserts Prediction with the Support of Large Language Model](https://arxiv.org/pdf/2407.21429) | 2024 | arXiv |
| 28 | [Deep Multiple Assertions Generation](https://doi.org/10.1145/3650105.3652293) | 2024 | FORGE |
| 29 | [Do LLMs generate test oracles that capture the actual or the expected program behaviour?](https://arxiv.org/html/2410.21136v1) | 2024 | arXiv |
| 30 | [Transducer Tuning: Efficient Model Adaptation for Software Tasks Using Code Property Graphs](https://arxiv.org/pdf/2412.13467) | 2024 | arXiv |
| 31 | [Learning deep semantics for test completion](https://www.cs.utexas.edu/~ml/papers/nie.icse23.pdf) | 2023 | ICSE |
| 32 | [Neural-Based Test Oracle Generation: A Large-scale Evaluation and Lessons Learned](https://arxiv.org/pdf/2307.16023v2) | 2023 | FSE |
| 33 | [Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning](https://people.ece.ubc.ca/amesbah/resources/papers/cedar-icse23.pdf) | 2023 | ICSE |
| 34 | [Towards More Realistic Evaluation for Neural Test Oracle Generation](https://kui-liu.github.io/papers/2023-liu-towards.pdf) | 2023 | ISSTA |
| 35 | [Using Transfer Learning for Code-Related Tasks](https://arxiv.org/pdf/2206.08574v1) | 2023 | TSE |
| 36 | [Generating Accurate Assert Statements for Unit Test Cases using Pretrained Transformers](https://arxiv.org/pdf/2009.05634) | 2022 | AST |
| 37 | [TOGA: A Neural Method for Test Oracle Generation](https://arxiv.org/pdf/2109.09262) | 2022 | ICSE |

### Test Augmentation

15 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Automated Test Suite Enhancement Using Large Language Models with Few-shot Prompting](https://arxiv.org/html/2602.12256v1) | 2026 | ICPC |
| 2 | [Change And Cover: Last-Mile, Pull Request-Based Regression Test Augmentation](https://arxiv.org/html/2601.10942v1) | 2026 | ICSE |
| 3 | [E-Test: E’er-Improving Test Suites](https://www.lucadigrazia.com/papers/icse2026.pdf) | 2026 | ICSE |
| 4 | [Generalizing Test Cases for Comprehensive Test Scenario Coverage](https://arxiv.org/html/2604.21771) | 2026 | FSE |
| 5 | [LLMutantKiller: Using Large Language Models to Generate Tests that Kill Mutants](https://www.franktip.org/pubs/issta2026.pdf) | 2026 | ISSTA |
| 6 | [PR-Aware Automated Unit Test Generation: Challenges and Opportunities](https://arxiv.org/html/2605.25285v1) | 2026 | COMPSAC |
| 7 | [Probe to Generate: Program Variant-Guided Test Augmentation for Repository-Level Repair Benchmarks](https://arxiv.org/html/2604.01518v2) | 2026 | ASE |
| 8 | [TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution](https://arxiv.org/html/2607.02469v1) | 2026 | arXiv |
| 9 | [TestTailor: Generating High-Coverage Tests via Path-Proximal Tests with LLMs](https://doi.org/10.1145/3797140) | 2026 | FSE |
| 10 | [Advancing Bug Detection in Fastjson2 with Large Language Models Driven Unit Test Generation](https://arxiv.org/pdf/2410.09414v2) | 2025 | APSEC |
| 11 | [Mutation-Guided LLM-based Test Generation at Meta](https://discovery.ucl.ac.uk/10218052/1/fse25_industry_paper_arXiv.pdf) | 2025 | FSE |
| 12 | [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf) | 2025 | ICLR |
| 13 | [Automated Unit Test Improvement using Large Language Models at Meta](https://discovery.ucl.ac.uk/id/eprint/10199775/1/RPS3.pdf) | 2024 | FSE |
| 14 | [Domain Adaptation for Code Model-based Unit Test Case Generation](https://www.eecs.yorku.ca/~wangsong/papers/issta24.pdf) | 2024 | ISSTA |
| 15 | [CAT-LM Training Language Models on Aligned Code And Tests](https://arxiv.org/pdf/2310.01602) | 2023 | ASE |

### Bug Reproduction

14 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [AssertFlip: Reproducing Bugs via Inversion of LLM-Generated Passing Tests](https://arxiv.org/html/2507.17542v2) | 2026 | ICSE |
| 2 | [Can test cases generated by large language models facilitate automated program repair?](https://doi.org/10.1007/s10664-026-10802-w) | 2026 | EMSE |
| 3 | [DPIAgent: Divide, Protocol, Isolate for Agentic Reproduction Test Generation](https://arxiv.org/html/2608.23341v1) | 2026 | arXiv |
| 4 | [Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection](https://arxiv.org/html/2508.06365v3) | 2026 | ICSE |
| 5 | [How Well does LLM Generate Security Tests](https://arxiv.org/pdf/2310.00710) | 2026 | TSE |
| 6 | [iCoRe: An Iterative Correlation-Aware Retriever for Bug Reproduction Test Generation](https://arxiv.org/html/2604.19224v2) | 2026 | FSE |
| 7 | [Issue2Test: Generating Reproducing Test Cases from Issue Reports](https://arxiv.org/html/2503.16320v4) | 2026 | ICSE |
| 8 | [LLM vs. Human Unit Tests: Fault Detection on Real Python Bugs](https://arxiv.org/html/2606.08588v1) | 2026 | arXiv |
| 9 | [ReProAgent: Tool-Augmented Multi-Stage Agentic Generation of Bug Reproduction Tests from Issue Reports](https://arxiv.org/html/2607.09123v1) | 2026 | arXiv |
| 10 | [Automated Generation of Issue-Reproducing Tests by Combining LLMs and Search-Based Testing](https://arxiv.org/html/2509.01616) | 2025 | ASE |
| 11 | [Otter: Generating Tests from Issues to Validate SWE Patche](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ahmed25b/ahmed25b.pdf) | 2025 | ICML |
| 12 | [Vulnerability-Triggering Test Case Generation from Third-Party Libraries](https://arxiv.org/html/2409.16701v3) | 2025 | FORGE |
| 13 | [Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models](https://orbilu.uni.lu/bitstream/10993/65665/1/3639478.3643119.pdf) | 2024 | ICSE |
| 14 | [Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction](https://arxiv.org/pdf/2209.11515v3) | 2023 | ICSE |

### Test Evolution

13 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Exploring the integration of large language models in industrial test maintenance processes](https://greg4cr.github.io/pdf/26maintenancellm.pdf) | 2026 | JSS |
| 2 | [Leveraging Change Types and Contexts to Guide LLMs for Automated Test Code Updating](https://doi.org/10.1145/3794763.3794816) | 2026 | ICPC |
| 3 | [MuMuTestUp: Mutation-based Multi-Agent Test Case Update](https://arxiv.org/html/2605.19265v1) | 2026 | ISSTA |
| 4 | [TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution](https://arxiv.org/html/2607.02469v1) | 2026 | arXiv |
| 5 | [A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing](https://arxiv.org/pdf/2412.16620) | 2025 | ISSTA |
| 6 | [Automated Test Case Repair Using Language Models](https://arxiv.org/pdf/2401.06765v4) | 2025 | TSE |
| 7 | [Comprehend, Imitate, and then Update: Unleashing the Power of LLMs in Test Suite Evolution](https://cs.nju.edu.cn/yuanyao/static/ase2025.pdf) | 2025 | ASE |
| 8 | [COTE: Predicting Code-to-Test Co-Evolution by Integrating Link Analysis and Pre-Trained Language Model Techniques](https://doi.org/10.1109/TSE.2025.3583027) | 2025 | TSE |
| 9 | [REACCEPT: Automated Co-evolution of Production and Test Code Based on Dynamic Validation and Large Language Models](https://arxiv.org/html/2411.11033v1) | 2025 | ISSTA |
| 10 | [Unit Test Update through LLM-Driven Context Collection and Error-Type-Aware Refinement](https://arxiv.org/html/2509.24419v1) | 2025 | ASE |
| 11 | [UTFix: Change Aware Unit Test Repairing using LLM](https://arxiv.org/html/2503.14924v1) | 2025 | OOPSLA |
| 12 | [Augmenting LLMs to Repair Obsolete Test Cases with Static Collector and Neural Reranker](https://hanada31.github.io/pdf/issre24_synter.pdf) | 2024 | ISSRE |
| 13 | [Identify and Update Test Cases When Production Code Changes: A Transformer-Based Approach](https://xing-hu.github.io/assets/papers/ASE2023CEPROT.pdf) | 2023 | ASE |

### Test Repair

6 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [MultiFileTest: A Multi-File-Level LLM Unit Test Generation Benchmark and Impact of Error Fixing Mechanisms](https://aclanthology.org/2026.findings-acl.1403.pdf) | 2026 | ACL |
| 2 | [VALTEST: Automated Validation of Language Model Generated Test Cases](https://arxiv.org/pdf/2411.08254v3) | 2026 | TSE |
| 3 | [AssertFix: Empowering Automated Assertion Fix via Large Language Models](https://arxiv.org/html/2509.23972v1) | 2025 | arXiv |
| 4 | [FlakyGuard: Automatically Fixing Flaky Tests at Industry Scale](https://arxiv.org/html/2511.14002v1) | 2025 | ASE |
| 5 | [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](https://doi.org/10.1109/ICSE55347.2025.00226) | 2025 | ICSE |
| 6 | [FlakyFix: Using Large Language Models for Predicting Flaky Test Fix Categories and Test Code Repair](https://arxiv.org/html/2307.00012v4) | 2024 | TSE |

### Test Smell Detection

4 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Test smells in LLM-Generated Unit Tests](https://arxiv.org/html/2410.10628v3) | 2026 | TOSEM |
| 2 | [Automated Unit Test Refactoring](https://xing-hu.github.io/assets/papers/FSE25TestRefactoring.pdf) | 2025 | FSE |
| 3 | [Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation](https://arxiv.org/html/2412.14308v1) | 2025 | DeepTest |
| 4 | [Evaluating Large Language Models in Detecting Test Smells](https://sol.sbc.org.br/index.php/sbes/article/download/30411/30217/) | 2024 | SBES |

### Test Readability Improvement

4 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Assertion Messages with Large Language Models (LLMs) for Code](https://arxiv.org/html/2509.19673v1) | 2025 | EASE |
| 2 | [Improving the Readability of Automatically Generated Tests using Large Language Models](https://matteobiagiola.github.io/assets/pdfs/improving-the-readability-of-automatically-generated-tests-using-large-language-models.pdf) | 2025 | ICST |
| 3 | [Leveraging Large Language Models for Enhancing the Understandability of Generated Unit Tests](https://azaidman.github.io/publications/deljouyiICSE2025.pdf) | 2025 | ICSE |
| 4 | [An LLM-based Readability Measurement for Unit Tests' Context-aware Inputs](https://arxiv.org/pdf/2407.21369v2) | 2024 | arXiv |

### Test Completion

3 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Harnessing the Power of LLMs: Automating Unit Test Generation for High-Performance Computing](https://arxiv.org/pdf/2407.05202v1) | 2024 | arXiv |
| 2 | [CAT-LM Training Language Models on Aligned Code And Tests](https://arxiv.org/pdf/2310.01602) | 2023 | ASE |
| 3 | [Learning deep semantics for test completion](https://www.cs.utexas.edu/~ml/papers/nie.icse23.pdf) | 2023 | ICSE |

### Test Migration

2 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Automated Knowledge-Aware Test Reuse](https://dl.acm.org/doi/epdf/10.1145/3808146) | 2026 | FSE |
| 2 | [IntentTester: Intent-Driven Multi-Agent Framework for Cross-Library Test Migration](https://arxiv.org/html/2606.25588) | 2026 | FSE |

### Test Minimization

2 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Can Old Tests Do New Tricks for Resolving SWE Issues?](https://arxiv.org/html/2510.18270v2) | 2026 | FSE |
| 2 | [LTM: Scalable and Black-box Similarity-based Test Suite Minimization based on Language Models](https://arxiv.org/pdf/2304.01397) | 2024 | TSE |

### Test Refactoring

2 studies.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Humanizing Automatically Generated Unit Test Suites with LLM-Based Refactoring](https://arxiv.org/html/2606.28229v2) | 2026 | arXiv |
| 2 | [Automated Unit Test Refactoring](https://xing-hu.github.io/assets/papers/FSE25TestRefactoring.pdf) | 2025 | FSE |

### Test-to-Code Traceability

1 study.

| No. | Title | Year | Venue |
|---|---|---|---|
| 1 | [Method-Level Test-to-Code Traceability Link Construction by Semantic Correlation Learning](https://yanmeng.github.io/papers/TSE241.pdf) | 2024 | TSE |

## Related Surveys

- Wang et al. **Software Testing With Large Language Models: Survey, Landscape, and Vision.** IEEE TSE, 2024. [Paper](https://doi.org/10.1109/TSE.2024.3368208).
- Zhang et al. **Enhancing Automated Unit Test Generation with Large Language Models: A Systematic Literature Review.** ACM TOSEM, 2026.

Adjacent work on automated program repair:

- **A Survey of Learning-based Automated Program Repair.** ACM TOSEM, 2023. [Paper](https://arxiv.org/abs/2301.03270) · [Repository](https://github.com/iSEngLab/AwesomeLearningAPR).
- **Automatic Software Repair: A Bibliography.** ACM CSUR, 2018. [Paper](https://doi.org/10.1145/3105906).
- **Automatic Software Repair: A Survey.** IEEE TSE, 2017. [Paper](https://doi.org/10.1109/TSE.2017.2755013).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=iSEngLab/AwesomeLLM4UT&type=Date)](https://star-history.com/#iSEngLab/AwesomeLLM4UT&Date)

## Extraction Data

The release provides study-level classifications and reproducible descriptive statistics, rather than only a bibliography. No Excel files or internal review notes are included.

| File | Contents |
|---|---|
| [Study records](data/studies.csv) | 228 studies with publication information, tasks, languages, models, strategies, integrated techniques, generation metrics, datasets and public links. |
| [Statistics](data/statistics.csv) | Category counts and explicit denominators. |
| [Category memberships](data/memberships.csv) | Study IDs supporting each category count. |
| [Data documentation](data/README.md) | Field definitions, RQ mappings and coding/counting conventions. |
| [Recomputation script](data/recompute.py) | Recreates the two derived CSV files using Python 3 without dependencies. |

To recompute the statistics from the repository root:

```sh
python3 data/recompute.py
```
