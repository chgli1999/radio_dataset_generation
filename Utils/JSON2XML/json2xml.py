
# -*- coding: utf8 -*-
import os
import json
import numpy as np
from pascal_voc_io import PascalVocWriter


def filepath(train_path,json_path):
    train_name = sorted([file.split(".")[0] for file in os.listdir(train_path)])
    json_name = sorted([file.split(".")[0] for file in os.listdir(json_path)])
    return train_name,json_name


def read_json(filename):
    with open(filename,'r') as f :
        data = json.load(f)
    signal_num = data['signal_num']
    boxes_data = []
    mods_classes = []
    for num in range(signal_num):
        signal_data = data['signal_block_{}'.format(num)]
        box_data = np.zeros((len(signal_data), 4))
        mod_classes = []
        for i in range(len(signal_data)):
            temp_data = signal_data[i]
            box_data[i,0]=(temp_data['start_time'])    #信号开始时间
            box_data[i,1]=(temp_data['end_time'])      #信号结束时间
            box_data[i,2]=(temp_data['center_fre'])    #信号中心频率
            box_data[i,3]=(temp_data['bandwidth'])     #信号带宽
            mod_classes.append(temp_data['modulation'])  #信号调制模式
        boxes_data.append(box_data)
        mods_classes.append(mod_classes)

    return boxes_data,mods_classes

def trans(boxes,duration_time,usrp_center_fre = 2.002e9,whole_bd=40e6,img_size=(512,512)):
    '''
    转换为x_min,y_min,x_max,y_max
    :param boxes:
    :param usrp_center_fre:
    :param duration_time:
    :param whole_bd:
    :return:
    '''

    temp_param = np.zeros(boxes.shape)
    box = boxes
    start_fre = usrp_center_fre-whole_bd/2
    for i in range(box.shape[0]):
        start_time = box[i,0]/duration_time
        end_time = box[i,1] / duration_time
        center_fre = (box[i,2]-start_fre) / whole_bd
        bandwidth = box[i,3] / whole_bd

        temp_param[i,0] = np.ceil((center_fre - bandwidth/2)* img_size[0]) #xmin
        temp_param[i,1] = np.ceil(start_time* img_size[1]) #ymin
        temp_param[i,2] = np.ceil((center_fre + bandwidth/2)* img_size[0]) #xmax
        temp_param[i,3] = np.ceil(end_time* img_size[1]) #ymax



    return temp_param


if __name__=='__main__':
    #--------------该系列参数根据usrp配置模式及时更正-----
    usrp_rec_center_fre = 1.982e9
    duration_time = 6.71
    bandwidth = 40e6
    img_size = (512, 512, 1) #瀑布图的长、宽、深度
    dir = 'Annotations' #目标存储目录名，不需要'/'
    #-----------------------------------------------
    root = os.getcwd()
    train_path = 'amplitude'   #
    json_path = 'json'
    foldername = 'train'

    train_file,json_file=filepath(train_path,json_path)

    for i in range(0, len(train_file)):
        filename =train_file[i]
        local_img_path = os.path.join(root,train_path,filename+'.png')
        pascol_voc = PascalVocWriter(foldername, filename, img_size,localImgPath=local_img_path)
        Boxes, Classes = read_json('json/' + json_file[i] + '.json')
        for sgn_num in range(len(Boxes)):
            classes = Classes[sgn_num]
            boxes = trans(Boxes[sgn_num], usrp_center_fre=usrp_rec_center_fre, duration_time=duration_time, whole_bd=bandwidth)
            for j in range(boxes.shape[0]):
                box = boxes[j]
                mod_class = classes[j]
                pascol_voc.addBndBox(box[0],box[1],box[2],box[3],mod_class,0)

        pascol_voc.save(dir)

