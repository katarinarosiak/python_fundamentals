import os

print(os.getcwd())  # print current directory

# os.chdir("/usr/bin/python3/home/katarina/launch_school/")  # change directory
os.chdir("/home/katarina/Desktop/")
print(os.getcwd())
print(os.listdir())  # list all directories
os.mkdir("test_directory")  # create a new directory
