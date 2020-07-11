import os
import glob
def remove(format):
    return glob.glob('*.' + format)
forms=['jpg','txt']
for form in forms:
    files=remove(form)
    for file in files:
        os.remove(file)