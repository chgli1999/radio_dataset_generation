#与图片集进行比较，删除多余的标注文件

import os


root = os.getcwd()
data1_path = os.path.join(root,'ImageSet')
file1_list = os.listdir(data1_path)

test_list = []
for file in file1_list:
    a = file.split('.')
    test_list.append(a[0])

data2_path = os.path.join(root,'Annotations')
file2_list = os.listdir(data2_path)

for i in file2_list:
    num = (i.split('.'))[0]
    if num in test_list:
        continue
    else:
        os.remove(os.path.join(data2_path, i))