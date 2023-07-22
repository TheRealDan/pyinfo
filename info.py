import os
import sys
import collections

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

path = sys.path[0]
folders = os.listdir(path)

total = 0;
results = {}
for folder in folders:
    if (folder == "info.py"):
        continue;
    bits = get_size(path + "\\" + folder)
    total += bits;
    size = ("%0.2f" % (bits / 1000000000)) + " GB" if bits > 1000000 else "1 MB"
    results[bits] = folder + ": " + size

sortedResults = dict(sorted(results.items()))
for k, v in sortedResults.items():
    print(v)

print("Total: " + ("%0.2f" % (total / 1000000000)) + " GB");

input("Press ENTER to continue...")