from pathlib import Path
import site
import os
import sys

curr_dir=Path(__file__).parent
root_dir = curr_dir.parent  #ATSC 448 folder
data_dir= root_dir / 'BV/data'

if not data_dir.is_dir():
    print(f"in context.py, was expecting to find {data_dir}\n"
          f"need to create it")
# processed_dir.mkdir(parents=True, exist_ok=True)
# raw_dir.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, root_dir)

sep = "*" * 30
print(
    (
        f"{sep}\ncontext imported. Front of path:\n"
        f"{sys.path[0]}\n{sys.path[1]}\n{sep}\n"
    )
)
site.removeduppaths()


