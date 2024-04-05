#write a function to read in filenames from a location and copy the data to a new location

import os
import shutil
import re


def rename_file(fname):
    #rename the filenames and return it
    newFname = re.sub(r'(AB|BB) \((\d+)\) g\.tif', r'\1_\2.tif', fname)
    return newFname

def copy_data(src, dest):
    #check if dest exists, if not create it
    if not os.path.exists(dest):
        os.makedirs(dest)
        print(f"Created {dest}")
    for root, dirs, files in os.walk(src):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest, rename_file(file))
            shutil.copyfile(src_file, dest_file)
            

if __name__ == "__main__":
    src = "/Users/hsuyab/Documents/GitHub/actin_seg/data/A_B_Gray"
    dest = "/Users/hsuyab/Documents/GitHub/actin_seg/data/data_ab_gray"
    copy_data(src, dest)

