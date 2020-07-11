import os
import glob
def remove(format):
    return glob.glob('*.' + format)
forms=['mp4']
for form in forms:
    files=remove(form)
    for file in files:
        os.remove(file)