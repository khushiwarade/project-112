import os
import shutil
from_dir ="C:/Users/user/Downloads"
to_dir ="C:/Users/user/Desktop/document_file"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for C:/Users/user/Downloads in list_of_files:
    name,extension=os.path.splitext(C:/Users/user/Downloads)
    if extension == "":
        if extension in ['.txt','.doc','docx','.pdf']
        path1 = from_dir "C:/Users/user/Downloads"
        path2 = to_dir ="C:/Users/user/Desktop/document_file"
        path3 = to_dir ="C:/Users/user/Desktop/document_file+C:/Users/user/Downloads"
        

        if os.path.exists(path2):
          print("Moving " + C:/Users/user/Downloads + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + C:/Users/user/Downloads + ".....")
          shutil.move(path1, path3)
