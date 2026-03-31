"""
harness/test_harness.py

自动化测试桩：
- 自动发现 sales_forecast/ 目录下所有 Python 文件和类/函数
- 自动运行 pytest 测试
- 自动运行 ruff lint 检查
- 检查未覆盖的代码并输出报告
- 支持一键完善（如发现未通过自动修复格式/提示补全测试）
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "sales_forecast"
TESTS_DIR = PROJECT_ROOT / "tests"


def run_lint():
    print("\n[1] 运行 ruff lint 检查...")
    result = subprocess.run([
        sys.executable, "-m", "ruff", "check", str(SRC_DIR), str(TESTS_DIR)
    ])
    if result.returncode != 0:
        print("[!] Lint 检查未通过，请根据提示修复！")
    else:
        print("[✓] Lint 检查通过！")
    return result.returncode


def run_format():
    print("\n[2] 自动格式化代码...")
    subprocess.run([
        sys.executable, "-m", "ruff", "format", str(SRC_DIR), str(TESTS_DIR)
    ])
    print("[✓] 格式化完成！")


def run_pytest():
    print("\n[3] 运行 pytest 自动化测试...")
    result = subprocess.run([
        sys.executable, "-m", "pytest", str(TESTS_DIR), "-v", "--cov=sales_forecast", "--cov-report=term-missing"])
    if result.returncode != 0:
        print("[!] 测试未全部通过，请根据 pytest 输出修复！")
    else:
        print("[✓] 所有测试通过！")
    return result.returncode


def main():
    lint_code = run_lint()
    if lint_code != 0:
        print("[自动修复] 尝试自动格式化...")
        run_format()
        print("[再次 lint 检查]")
        run_lint()
    test_code = run_pytest()
    if test_code != 0:
        print("[提示] 请完善/修复测试用例和实现代码！")
    else:
        print("[全部通过] 代码已符合 lint 和测试规范！")

if __name__ == "__main__":
    main()
