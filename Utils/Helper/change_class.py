import os
import xml.etree.ElementTree as ET


if __name__ == "__main__":

    root = os.getcwd()
    change_name = 'Signal'
    annotations_root = os.path.join(root, "Annotations")
    imagesets_root = os.path.join(root, "ImageSets", "Main")
    txt_list = os.path.join(root, "train.txt")

    with open(txt_list) as read:
        xml_list = [os.path.join(root, line.strip() + ".xml")
                    for line in read.readlines()]

    for i in range(len(xml_list)):
        tree = ET.parse(xml_list[i])
        root = tree.getroot()
        object=root.findall('object')
        #查找所有的object的name节点并修改为想要的名字
        for j in range(len(object)):
            object[j].find('name').text =change_name

        tree.write(xml_list[i], encoding="utf-8", xml_declaration=True)


