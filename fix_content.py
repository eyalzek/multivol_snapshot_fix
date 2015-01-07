#!/usr/bin/python
import os
import shutil

for root, dirs, files in os.walk("./multivol_snapshot"):
    if [True for f in files if f == "content"]:
        newfile = os.path.join(os.path.dirname(root), "file-" + root.split("/").pop())
        newfile_fixed = os.path.join(os.path.dirname(root), root.split("/").pop())
        os.rename(os.path.join(root, "content"), newfile)
        print("moved file to: {}".format(newfile))
        shutil.rmtree(root)
        print("delete directory: {}".format(root))
        os.rename(newfile, newfile_fixed)
        print("{} => {}".format(newfile, newfile_fixed))
