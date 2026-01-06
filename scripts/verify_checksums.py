#!/usr/bin/env python3
import hashlib
import sys
from pathlib import Path

CHECKSUM_FILE = Path("checksums.txt")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not CHECKSUM_FILE.exists():
        print("ERROR: checksums.txt not found")
        sys.exit(1)

    failed = False

    for line in CHECKSUM_FILE.read_text().splitlines():
        if not line.strip():
            continue
        expected, relpath = line.split("  ")
        path = Path(relpath)

        if not path.exists():
            print(f"ERROR: Missing file: {path}")
            failed = True
            continue

        actual = sha256(path)
        if actual != expected:
            print(f"ERROR: Checksum mismatch: {path}")
            failed = True

    if failed:
        sys.exit(1)

    print("All checksums verified successfully.")

if __name__ == "__main__":
    main()
