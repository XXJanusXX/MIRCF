#!/usr/bin/env python3
"""
Pre-commit hook to forbid dict unpacking with overrides, e.g.:

    dict(**cfg, mode=t)

This pattern is unsafe and caused CI/runtime failures in MIRCF notebooks.
The hook scans .ipynb files and fails if such usage is detected.
"""

import json
import re
import sys
from pathlib import Path

# Regex detects dict(**something, key=value)
UNSAFE_PATTERN = re.compile(
    r"dict\s*\(\s*\*\*[^,]+,\s*[^=]+=",
    re.MULTILINE,
)

def scan_notebook(path: Path) -> list[str]:
    errors = []
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{path}: invalid JSON ({e})"]

    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if UNSAFE_PATTERN.search(source):
            errors.append(
                f"{path}: cell {i} contains unsafe dict(**cfg, ...) override"
            )
    return errors

def main(argv: list[str]) -> int:
    files = [Path(p) for p in argv if p.endswith(".ipynb")]
    all_errors = []
    for f in files:
        all_errors.extend(scan_notebook(f))

    if all_errors:
        print("ERROR: Unsafe dict unpacking detected:\n")
        for e in all_errors:
            print("  -", e)
        print(
            "\nFix by using explicit copies, e.g.:\n"
            "  cfg_t = cfg.copy(); cfg_t['mode'] = t"
        )
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
