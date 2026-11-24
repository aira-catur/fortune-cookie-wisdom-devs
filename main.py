import os
from pathlib import Path

TEXT = "You will inherit the code you once called temporary, and it will outlive every deadline you set for it."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
