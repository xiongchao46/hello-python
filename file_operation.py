from __future__ import division
import os
import re

root_path = "/usr"

def find_path(root, paths):
    """ 正则匹配查找特定文件夹所在路径"""
    for root, dirs, files in os.walk(root):
        for dir in dirs:
            math_result = re.match(r'python\d.\d$', dir)
            if math_result == None:
                continue
            paths.append(os.path.join(root, dir))

def search_file(root_path):
    """递归查找指定目录下文件并且记录文件名
    文件大小、文件路径"""
    paths = []
    find_path(root_path, paths)
    for path in paths:
        print("\n{}".format(path))
        folders = []
        files_info = []
        if not os.path.exists(path):
            print("path: {} not exits!".format(path))
            continue
        for root, dirs, files in os.walk(path):
            folders.extend(dirs)
            for f in files:
                file_path = os.path.join(root, f)
                f_size = round(os.path.getsize(file_path), 3)
                files_info.append((f, f_size, file_path)) #[file, size, path]
        display(folders, files_info)


def display(folders, files_info):
    """打印最长文件名的文件、最大存储的文件、文件夹下所有文件的占用存储空间大小"""
    print("Total folders : {}, Total files : {}".format(len(folders), len(files_info)))
    if len(files_info) > 0:
        longest_file = sorted(files_info, key=lambda x:len(x[0]), reverse=True)[0][0]
        largest_file_size = sorted(files_info, key=lambda x: x[1], reverse=True)[0][1]
        largest_file = sorted(files_info, key=lambda x:x[1], reverse=True)[0][2]
        print("Longest file name : {}, length : {}".format(longest_file, len(longest_file)))
        print("Largest file name : {}, size : {}".format(largest_file, str(round(largest_file_size / 1024 / 1024))+"M"))
    print("Total size : {}".format(sum(it[1] for it in files_info)))


def main():
    search_file(root_path)

if __name__ == "__main__":
    main()