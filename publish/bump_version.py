import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: bump_version.py <version>")
    sys.exit(1)

version = sys.argv[1]
Path("VERSION").write_text(version + "\n", encoding="utf-8")
print(f"Version bumped to {version}")
