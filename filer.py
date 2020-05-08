from __future__ import print_function
from pathlib import Path
import os, sys, shutil, subprocess, random, string

def random_string(length):
    return ''.join(random.choice(string.printable) for m in xrange(length))

# look in this directory
path = Path('.')
for p in path.iterdir():
    print(p)

# create a new directory
# startdir = str(raw_input('Starting directory name: '))
startdir = "tmp"
os.mkdir(startdir)

# create a some sample files to manipulate
# number = input("How many files? ")
number = 10
for i in range(number):
    s = random_string(100)
    # print(s)
    txtname = startdir + "/output"  + str(i) + ".txt"
    pyname = startdir + "/output"  + str(i) + ".py"
    print("Write " + txtname)
    with open(txtname, "w") as text_file:
        text_file.write(s)
    with open(pyname, "w") as text_file:
        text_file.write(s)

# create a new directory
# copy only *.py files
# newdir = str(raw_input('New directory name: '))
newdir = 'newdir'
shutil.copytree(startdir, newdir, ignore=shutil.ignore_patterns('*.txt'))


    