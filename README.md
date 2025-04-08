<h1 align = "center">🤖 Awesome LLM for APR</h1>
<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg"></a>
  <a href="https://arxiv.org/abs/2405.01466"><img src="https://img.shields.io/badge/arXiv-2405.01466-blue.svg"></a>
  <img src="https://img.shields.io/github/stars/iSEngLab/AwesomeLLM4UT?color=yellow&label=Stars">
  <img src="https://img.shields.io/badge/PRs-Welcome-red">
  <img src="https://img.shields.io/github/last-commit/iSEngLab/AwesomeLLM4APR">
</p>


## 📖 Contents

- [👏 Citation](#-citation)
- [🔹 Unit Testing Tasks](#-papers-categorized-by-unit-testing-task)
  - [Test Generation](#-test-generation)
  - [Assertion Generation](#-assertion-generation)
  - [Oracle Generation](#-oracle-generation)
  - [Test Evolution](#-test-evolution)
  - [Bug Reproduction](#-bug-reproduction)
  - [Test Smell](#-test-smell)
  - [Test Completion](#-test-completion)
  - [Test Readability](#-test-readability)
  - [Outdated Test Identify](#-outdated-test-identify)
  - [Test Refactoring](#-test-refactoring)
  - [Test Validation](#-test-validation)
  - [Test Minimization](#-test-minimization)
  - [Test-to-Code Traceability](#-test-to-code-traceability)
- [🤔 Related Surveys](#-related-surveys)
- [📈 Star History](#-star-history)



## 👏 Citation

```bibtex
@article{zhang2024survey,
  title={A Systematic Literature Review on Large Language Models for Automated Program Repair},
  author={Zhang, Quanjun and Fang, Chunrong and Xie, Yang and Ma, Yuxiang and Sun, Weisong and Yang, Yun and Chen, Zhenyu},
  journal={arXiv preprint arXiv:2405.01466}
  year={2024}
}

```


# 📚 Papers Categorized by Unit Testing Task


## 🔹 Test Generation

| Title | Year | Venue |
|-------|------|-------|
| Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation | 2025 | ICSE@DeepTest |
| RUG: Turbo LLM for Rust Unit Test Generation | 2025 | ICSE |
| What You See Is What You Get: Attention-based Self-guided Automatic Unit Test Generation | 2025 | ICSE |
| Enhancing LLM's Ability to Generate More Repository-Aware Unit Tests Through Precise Contextual Information Injection | 2025 | ArXiv |
| Test Wars: A Comparative Study of SBST, Symbolic Execution, and LLM-Based Approaches to Unit Test Generation | 2025 | ICST |
| CITYWALK: Enhancing LLM-Based C++ Unit Test Generation via Project-Dependency Awareness and Language-Specific Knowledge | 2025 | ArXiv |
| A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing | 2025 | ISSTA |
| Dynamic Scaling of Unit Tests for Code Reward Modeling | 2025 | ArXiv |
| The Prompt Alchemist: Automated LLM-Tailored Prompt Optimization for Test Case Generation | 2025 | ArXiv |
| Mutation-Guided LLM-based Test Generation at Meta | 2025 | ArXiv |
| STRUT: Structured Seed Case Guided Unit Test Generation for C Programs using LLMs | 2025 | ISSTA |
| LLM-based Unit Test Generation for Dynamically-Typed Programs | 2025 | ArXiv |
| A3Test: Assertion-Augmented Automated Test Case Generation | 2024 | IST |
| ChatUniTest: A Framework for LLM-Based Test Generation | 2024 | FSE |
| On the Evaluation of Large Language Models in Unit Test Generation | 2024 | ASE |
| An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation | 2024 | TSE |
| Enhancing LLM-based Test Generation for  Hard-to-Cover Branches via Program Analysis | 2024 | ArXiv |
| LLM-Powered Test Case Generation for Detecting Tricky Bugs | 2024 | ArXiv |
| Evaluating and Improving ChatGPT for Unit Test Generation | 2024 | FSE |
| CasModaTest: A Cascaded and Model-agnostic Self-directed Framework for Unit Test Generation | 2024 | ArXiv |
| Large-scale, Independent and Comprehensive study of the power of LLMs for test case generation | 2024 | ASE |
| Effective test generation using pre-trained Large Language Models and mutation testing | 2024 | IST |
| Optimizing Search-Based Unit Test Generation with Large Language Models: An Empirical Study | 2024 | Internetware |
| Domain Adaptation for Code Model-based Unit Test Case Generation | 2024 | ISSTA |
| LLM-based Unit Test Generation via Property Retrieval | 2024 | ArXiv |
| TestBench: Evaluating Class-Level Test Case Generation Capability of Large Language Models | 2024 | ArXiv |
| Retrieval-Augmented Test Generation: How Far Are We? | 2024 | ArXiv |
| Rethinking the Influence of Source Code on Test Case Generation | 2024 | ArXiv |
| HITS: High-coverage LLM-based Unit Test Generation via Method Slicing | 2024 | ASE |
| A System for Automated Unit Test Generation Using Large Language Models and Assessment of Generated Test Suites | 2024 | ArXiv |
| TestART: Improving LLM-based Unit Test via Co-evolution of Automated Generation and Repair Iteration | 2024 | ArXiv |
| Harnessing the Power of LLMs: Automating Unit Test Generation for High-Performance Computing | 2024 | ArXiv |
| CoverUp: Coverage-Guided LLM-Based Test Generation | 2024 | ArXiv |
| Enhancing Large Language Models for Text-to-Testcase Generation | 2024 | ArXiv |
| Automated Unit Test Improvement using Large Language Models at Meta | 2024 | FSE |
| Code-Aware Prompting: A study of Coverage Guided Test Generation in Regression Setting using LLM | 2024 | FSE |
| Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models | 2024 | ICSE |
| Using Large Language Models to Generate JUnit Tests: An Empirical Study | 2024 | EASE |
| ChatGPT vs SBST: A Comparative Assessment of Unit Test Suite Generation | 2024 | TSE |
| TestSpark: IntelliJ IDEA's Ultimate Test Generation Companion | 2024 | ICSE-Companion |
| Towards Understanding the Effectiveness of Large Language Models on Directed Test Input Generation | 2024 | ASE |
| Unit Test Generation using Large Language Models for Unity Game Development | 2024 | FaSE4Games |
| Data Augmentation by Fuzzing for Neural Test Generation | 2024 | ArXiv |
| ASTER: Natural and Multi-language Unit Test Generation with LLMs | 2024 | ICSE-SEIP |
| Unit Test Generation using Generative AI : A Comparative Performance Analysis of Autogeneration Tools | 2024 | LLM4Code(workshop) |
| Advancing Bug Detection in Fastjson2 with Large Language Models Driven Unit Test Generation | 2024 | ArXiv |
| Evaluation of Large Language Models for Unit Test Generation | 2024 | ASYU |
| CPP-UT-Bench: Can LLMs Write Complex Unit Tests in C++? | 2024 | ArXiv |
| Unit Test Generation for Vulnerability Exploitation in Java Third-Party Libraries | 2024 | ArXiv |
| UniTSyn: A Large-Scale Dataset Capable of Enhancing the Prowess of Large Language Models for Program Testing | 2024 | ISSTA |
| Parameter-Efficient Fine-Tuning of Large Language Models for Unit Test Generation: An Empirical Study | 2024 | ArXiv |
| Design choices made by LLM-based test generators prevent them from finding bugs | 2024 | ArXiv |
| TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark | 2024 | ArXiv |
| Automating Autograding: Large Language Models as Test Suite Generators for Introductory Programming | 2024 | JCAL |
| LLM4VV: Developing LLM-driven testsuite for compiler validation | 2024 | FGCS |
| VALTEST: Automated Validation of Language Model Generated Test Cases | 2024 | ArXiv |
| Large Language Models as Test Case Generators: Performance Evaluation and Enhancement | 2024 | ArXiv |
| LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation | 2024 | TSE |
| TDD-Bench Verified: Can LLMs Generate Tests for Issues Before They Get Resolved | 2024 | ArXiv |
| PyTester: Deep Reinforcement Learning for Text-to-Testcase Generation | 2024 | ArXiv |
| Using GitHub Copilot for Test Generation in Python: An Empirical Study | 2024 | AST |
| CAT-LM Training Language Models on Aligned Code And Tests | 2023 | ASE |
| Prompting Code Interpreter to Write Better Unit Tests on Quixbugs Functions | 2023 | ArXiv |
| An initial investigation of ChatGPT unit test generation capability | 2023 | SAST |
| Exploring the Capability of ChatGPT in Test Generation | 2023 | QRS |
| Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction | 2023 | ICSE |
| How Well does LLM Generate Security Tests | 2023 | ArXiv |
| CodeT: Code Generation with Generated Tests | 2023 | ICLR |
| CodaMosa: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models | 2023 | ICSE |
| Nuances are the Key: Unlocking ChatGPT to Find Failure-Inducing Tests with Differential Prompting | 2023 | ASE |
| Unit Test Case Generation with Transformers and Focal Context | 2021 | ArXiv |

## 🔹 Assertion Generation

| Title | Year | Venue |
|-------|------|-------|
| A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing | 2025 | ISSTA |
| DeCon: Detecting Incorrect Assertions via Postconditions Generated by a Large Language Model | 2025 | ArXiv |
| Improving Retrieval-Augmented Deep Assertion Generation via Joint Training | 2025 | TSE |
| Improving Deep Assertion Generation via Fine-Tuning Retrieval-Augmented Pre-trained Language Models | 2025 | TOSEM |
| Exploring Automated Assertion Generation via Large Language Models | 2024 | TOSEM |
| AssertionBench: A Benchmark to Evaluate Large-Language Models for Assertion Generation | 2024 | ArXiv |
| Chat-like Asserts Prediction with the Support of Large Language Model | 2024 | ArXiv |
| Transducer Tuning: Efficient Model Adaptation for Software Tasks Using Code Property Graphs | 2024 | ArXiv |
| Deep Multiple Assertions Generation | 2024 | FORGE |
| Assertify: Utilizing Large Language Models to Generate Assertions for Production Code | 2024 | ArXiv |
| An Empirical Study on Focal Methods in Deep-Learning-Based Approaches for Assertion Generation | 2024 | FSE |
| Retrieval-Based Prompt Selection for Code-Related Few-Shot Learning | 2023 | ICSE |
| Using Transfer Learning for Code-Related Tasks | 2023 | TSE |
| Generating Accurate Assert Statements for Unit Test Cases using Pretrained Transformers | 2022 | AST |
| On Learning Meaningful Assert Statements for Unit Test Cases | 2020 | ICSE |

## 🔹 Oracle Generation

| Title | Year | Venue |
|-------|------|-------|
| TOGLL: Correct and Strong Test Oracle Generation with LLMs | 2025 | ICSE |
| AugmenTest: Enhancing Tests with LLM-Driven Oracles | 2025 | ICST |
| exLong: Generating Exceptional Behavior Tests with Large Language Models | 2025 | ICSE |
| Doc2Oracle: Investigating the Impact of Javadoc Comments on Test Oracle Generation | 2024 | ArXiv |
| Do LLMs generate test oracles that capture the actual or the expected program behaviour? | 2024 | ArXiv |
| Towards More Realistic Evaluation for Neural Test Oracle Generation | 2024 | ISSTA |
| Assessing Evaluation Metrics for Neural Test Oracle Generation | 2024 | TSE |
| ChatAssert: LLM-based Test Oracle Generation with External Tools Assistance | 2023 | TSE |
| Neural-Based Test Oracle Generation: A Large-scale Evaluation and Lessons Learned | 2023 | FSE |
| TOGA: A Neural Method for Test Oracle Generation | 2022 | ICSE |

## 🔹 Test Evolution

| Title | Year | Venue |
|-------|------|-------|
| Automated Test Case Repair Using Language Models | 2025 | TSE |
| A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing | 2025 | ISSTA |
| REACCEPT: Automated Co-evolution of Production and Test Code Based on Dynamic Validation and Large Language Models | 2025 | ISSTA |
| Augmenting LLMs to Repair Obsolete Test Cases with Static Collector and Neural Reranker | 2024 | ISSRE |
| Identify and Update Test Cases When Production Code Changes: A Transformer-Based Approach | 2023 | ASE |

## 🔹 Bug Reproduction

| Title | Year | Venue |
|-------|------|-------|
| What You See Is What You Get: Attention-based Self-guided Automatic Unit Test Generation | 2025 | ICSE |
| Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models | 2024 | ICSE |
| Advancing Bug Detection in Fastjson2 with Large Language Models Driven Unit Test Generation | 2024 | ArXiv |
| Unit Test Generation for Vulnerability Exploitation in Java Third-Party Libraries | 2024 | ArXiv |
| Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction | 2023 | ICSE |

## 🔹 Test Smell

| Title | Year | Venue |
|-------|------|-------|
| Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation | 2025 | ICSE@DeepTest |
| Automated Unit Test Refactoring | 2025 | FSE |
| Test smells in LLM-Generated Unit Tests | 2024 | ArXiv |
| Evaluating Large Language Models in Detecting Test Smells | 2024 | SBES |

## 🔹 Test Completion

| Title | Year | Venue |
|-------|------|-------|
| TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark | 2024 | ArXiv |
| CAT-LM Training Language Models on Aligned Code And Tests | 2023 | ASE |
| Learning deep semantics for test completion | 2023 | ICSE |

## 🔹 Test Readability

| Title | Year | Venue |
|-------|------|-------|
| Leveraging Large Language Models for Enhancing the Understandability of Generated Unit Tests | 2025 | ICSE |
| Improving the Readability of Automatically Generated Tests using Large Language Models | 2025 | ICST |
| An LLM-based Readability Measurement for Unit Tests' Context-aware Inputs | 2024 | ArXiv |

## 🔹 Outdated Test Identify

| Title | Year | Venue |
|-------|------|-------|
| Identify and Update Test Cases When Production Code Changes: A Transformer-Based Approach | 2023 | ASE |

## 🔹 Test Refactoring

| Title | Year | Venue |
|-------|------|-------|
| Automated Unit Test Refactoring | 2025 | FSE |

## 🔹 Test Validation

| Title | Year | Venue |
|-------|------|-------|
| VALTEST: Automated Validation of Language Model Generated Test Cases | 2024 | ArXiv |

## 🔹 Test Minimization

| Title | Year | Venue |
|-------|------|-------|
| LTM: Scalable and Black-box Similarity-based Test Suite Minimization based on Language Models | 2024 | TSE |

## 🔹 Test-to-Code Traceability

| Title | Year | Venue |
|-------|------|-------|
| Method-Level Test-to-Code Traceability Link Construction by Semantic Correlation Learning | 2024 | TSE |



## 🤔 Related Surveys

1. A Survey of Learning-based Automated Program Repair [2023-TOSEM] [[paper](https://arxiv.org/abs/2301.03270)] [[repo](https://github.com/iSEngLab/AwesomeLearningAPR)]
2. Automatic Software Repair: A Bibliography [2018-CSUR] [paper](https://dl.acm.org/doi/10.1145/3105906)]
3. Automatic Software Repair: A Survey [2017-TSE] [paper](https://dl.acm.org/doi/10.1109/TSE.2017.2755013)]

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=iSEngLab/AwesomeLLM4UT&type=Date)](https://star-history.com/#iSEngLab/AwesomeLLM4UT&Date)
