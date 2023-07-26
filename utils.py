from pathlib import Path
from typing import List


def read_file(path: Path) -> List[str]:
    with open(file=path, mode="r") as fp:
        return list(map(lambda x: x[:-1] if x[-1] == "\n" else x, fp.readlines()))


def read_input(file_dir: Path) -> List[str]:
    return read_file(path=file_dir / "input.txt")


def read_example(file_dir: Path):
    return read_file(path=file_dir / "example.txt")
