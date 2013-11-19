import os
import sys
import shutil

def copy_iteration(src_path, dst_path):
  #src_path = os.path.join(src_path, dir_name)
  #dst_path = os.path.join(dst_path, dir_name)
    #src_path = src_path + dir_name + '/'
    #dst_path = dst_path + dir_name + '/'
  if not os.path.exists(dst_path):
    os.makedirs(dst_path)

  fileList = os.listdir(src_path)

  for files in fileList:
    files_path = os.path.join(src_path, files)
    if os.path.isdir(files_path):
      src_path = os.path.join(src_path, files)
      dst_path = os.path.join(dst_path, files)
      copy_iteration(src_path, dst_path)
      continue
    shutil.copy2(files_path, dst_path)

if not os.path.exists("directory"):
  os.makedirs("directory")

base_path = os.path.dirname(__file__)
direct_path = os.path.join(base_path, "targets_files")
django_path = os.path.join(base_path, "targets_files/django_dir/")
target_path = os.path.join(base_path, "directory")

if not os.path.exists(direct_path):
  print "direct_dir does not exist!"
  sys.exit(0)


#direct_fileList = os.listdir(direct_path)
#print direct_fileList
#direct_fileList = [direct_path+filename for filename in direct_fileList]
#print direct_fileList

#for files in direct_fileList:
  #if os.path.isdir(direct_path + files):
  	#print files
  	#continue
  	#copy_iteration(files, direct_path, "directory/")
  	#continue
  #print files
  #shutil.copy2(direct_path + files, "directory/")
#copy_iteration(direct_path, target_path)
shutil.rmtree('directory')

print "I make it!"
