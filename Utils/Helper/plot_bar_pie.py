#绘制数据集的分布图


import os
import xml.etree.ElementTree as ET
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = ['DengXian', 'sans-serif']
dict = {}

def filepath(path):
    file_name = sorted([file.split(".")[0] for file in os.listdir(path)])
    return file_name

def autolabel(ax,rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

if __name__ == "__main__":
    root = os.getcwd()
    anno_path = os.path.join(root,'Annotations')
    anno_list = filepath(anno_path)
    xml_list = [os.path.join(anno_path, line.strip() + ".xml")
                    for line in anno_list]

    for i in range(len(xml_list)):
        tree = ET.parse(xml_list[i])
        root = tree.getroot()
        object = root.findall('object')

        for j in range(len(object)):
            Mod=object[j].find('name').text
            dict[Mod] = dict.get(Mod, 0) + 1

    sample_key_list=list(dict.keys())
    sample_value_list=list(dict.values())

    fig, axs = plt.subplots(1, 2)
    axs[0].pie(x=sample_value_list, labels=sample_key_list, autopct='%3.1f %%')
    axs[0].set_title(label='调制类型分布统计图',
                 loc='center',
                 pad=None,
                 fontdict={'color': 'black'}
                 )
    autolabel(axs[1],plt.bar(range(len(sample_key_list)), sample_value_list, color='rgb', tick_label=sample_key_list))
    axs[1].set_title(label='调制类型分布直方图',
                     loc='center',
                     pad=None,
                     fontdict={'color': 'black'}
                     )
    fig.suptitle('调制类型总数:{}类'.format(len(sample_key_list)),fontsize=15)
    plt.xticks(rotation=70,fontsize=8)
    plt.show()
