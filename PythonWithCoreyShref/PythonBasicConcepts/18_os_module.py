import os
from datetime import datetime

# print(dir(os))
print(os.getcwd()) # get current working directory
os.chdir('/home/mahesh/Documents') # change directory method 
print(os.getcwd())
print(os.listdir())   #list of directories and files in the current directory
#os.mkdir('OS-Demo-2') #mkdir is not allowed to create multiple directory or subdirectory with in a folder
os.makedirs('OS-Demo-2/Sub-Dir-1')

os.rmdir('OS-Demo-2') # it can't remove intermediate directories.
os.removedirs('OS-Demo-2/Sub-Dir-1')

print(os.listdir())

# rename file 
os.rename('test.txt', 'demo.txt')

# to get details of file
print(os.state('demo.txt'))
mod_time = os.state('demo.txt').st_mtime # last modified date
print(datetime.fromtimestamp(mod_time))

 #  a generator yield a tuple with 3 values walking the directory tree for each directory it's yields directory path the directory with in the path
for dirpath, dirname, filenames in os.walk('/home/mahesh/Documents'):
    print("current path: ", dirpath)
    print("Directories Path: ",dirname)
    print('Files: ',filenames)
    print()
    

# Access home directory location by grabbing environment variable

print(os.environ.get('HOME'))


file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

os.path.split('/tmp/text.txt')

# whether the path exist or not 
print(os.path.exists('/tmp/text.txt')) # return false

# whether it is directory
print(os.path.isdir('/tmp/fgdfgdf'))

 