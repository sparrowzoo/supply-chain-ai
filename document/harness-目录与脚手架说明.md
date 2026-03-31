# harness/ 目录与智能工程脚手架扩展说明

## 一、harness/ 目录定位

harness/ 目录用于存放自动化测试桩、集成测试脚本、回归验证工具和工程级质量保障资源，是项目“稳健性与可回归性”的核心支撑。

- **目标**：让每一次代码变更都能被自动验证，支撑 TDD（测试驱动开发）和循环反馈。
- **内容建议**：
  - test_harness.py / test_harness/：自定义测试桩、mock、集成测试脚本
  - pipeline/：CI/CD 流水线相关脚本（如 GitHub Actions、Jenkinsfile 等）
  - 回归测试用例、数据生成脚本、自动化验证工具

## 二、脚手架目录结构（含 harness/）

```
supply-chain-forecast/
├── .github/
├── .vscode/
├── config/
├── data/
├── document/
├── harness/                # ⭐ 自动化测试桩与工程保障
├── logs/
├── models/
├── notebooks/
├── reports/
├── sales_forecast/
├── tests/
├── template/
├── pyproject.toml
├── Makefile
├── Dockerfile
├── README.md
└── ...
```

## 三、harness/ 典型内容举例

- test_harness.py：主测试桩入口，集成各类 mock、集成测试、回归验证
- pipeline/github-actions.yml：CI/CD 自动化脚本
- data_generator.py：自动化测试数据生成
- regression_suite/：回归测试用例集合

## 四、与 tests/ 区别
- tests/ 侧重于单元测试、功能测试，通常由 pytest 驱动，关注代码正确性。
- harness/ 侧重于工程级自动化、集成、回归、端到端验证，关注系统稳健性与交付安全。

## 五、最佳实践
- harness/ 目录下的脚本应可被 CI/CD 自动调用，支持一键验证。
- 建议结合 TDD，先写 harness/ 下的集成/回归测试，再开发实现。
- harness/ 可与 Context Engine、Prompt Engine 协同，形成完整的智能工程闭环。

---

> harness/ 目录是现代 AI/ML 项目工程化、可维护、可回归的关键保障。建议每个团队根据自身业务和交付要求，持续完善该目录内容。
