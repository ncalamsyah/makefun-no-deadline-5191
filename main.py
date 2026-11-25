import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Progress was blocked by a dependency named Me, which has been marked blocked for three business days.")
