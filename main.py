import os

LINE = "Progress was blocked by a dependency named Me, which has been marked blocked for three business days."


def main() -> None:
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
