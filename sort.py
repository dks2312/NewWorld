
#한글깨짐
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os,re,copy

# 디렉토리안에 파일 개수를 반환 파일일땐 0
def dir_Count(dir_name):
  if os.path.isdir(os.path.abspath(dir_name)): 
    count = len(os.listdir(dir_name))
  else: 
    count = -1

  return count

# 디렉토리 경로를 받아 그 안에 있는 파일, 디렉토리의 파일 개수에 따라 정렬 파일일땐 빈 리스트 반환
def sort_file_Count(directory_route):
  if os.path.isdir(directory_route):
    file_name_list = os.listdir(directory_route)
    file_Count_list = list()

    for file_name in file_name_list:
      file_Count_list.append(dir_Count(file_name))

    file_Count_list.sort(reverse=True)

    for count in file_Count_list:
      for file_name in file_name_list:
        if count == dir_Count(file_name):
          file_Count_list[file_Count_list.index(count)] = file_name + ":" + str(count)
                    
    return file_Count_list
  else: 
    return list()

print(sort_file_Count(os.getcwd()))
