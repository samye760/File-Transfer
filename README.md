# File-Transfer

This script utilizes command line input to take an input file with the contents being file names to be transfered, and the result is to transfer those files to the specified directory. Very useful if a directory has thousands of files and you need to copy a significant subset of those files. This task would take forever to do manually, but can be handled if a few seconds with this script. Uses Python built in modules [shutil](https://docs.python.org/3/library/shutil.html) and [os](https://docs.python.org/3/library/os.html) to interact with the Operating System/File System.

## Usage

The first argument to the script should be the directory that the files are housed in. The second argument should be the filename (with path if it's in a different directory than the script), and the third argument is the output file with the path that the copied files will be placed.
