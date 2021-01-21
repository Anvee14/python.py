import os
import shutil
path = 'C:/Users/anvee/my_git_projects/'
print(os.listdir(path))
source = 'C:/Users/anvee/my_git_projects/Python/Data.txt'
dst = 'C:/Users/anvee/my_git_projects/Python/test'
copy = shutil.copy(source,dst)
print()
