import os, sys

base = r"c:\Users\admin\.cline\phishscope"
for d in sorted(os.listdir(base)):
    p = os.path.join(base, d)
    print(f"=== {d} ===")
    if os.path.isdir(p):
        for f in sorted(os.listdir(p)):
            fp = os.path.join(p, f)
            print(f"  {f} (dir={os.path.isdir(fp)})")
    else:
        print("  (not a dir)")