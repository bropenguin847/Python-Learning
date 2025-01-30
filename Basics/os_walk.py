"""
os.walk() in Python

OS.walk() generate the file names in a directory tree by walking the tree
either top-down or bottom-up. For each directory in the tree rooted at directory top
(including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

root : Prints out directories only from what you specified.
dirs : Prints out sub-directories from root.
files : Prints out all files from root and directories.

"""
import os

if __name__ == '__main__':
    for (root, dirs, files) in os.walk('.', topdown=True):
        print(f'This is the root: {root}')
        print(f'This is the sub directories from root{dirs}')
        print(f'These are all files from root and dir{files}')

# Program to find the python files in the directory tree,
# that means we need to find the files that ends with .py extension.
pythonFiles = [file for dirs in os.walk('.', topdown=True)
                    for file in dirs[2] if file.endswith(".py")]
print('python files in the directory tree are ')

for file in pythonFiles:
    print(file)
