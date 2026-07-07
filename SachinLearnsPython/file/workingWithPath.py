from pathlib import Path
import os
p = path("data")/"students"/"scores.csv"
print(p)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)

p.parent.mkdir(parents=True, exist_ok=True)

if p.exists():
    print(f"Size:{p.stat().st_size} bytes")

for f in Path(".").glob("*.txt"):
    print(f.name)