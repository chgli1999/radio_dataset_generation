#绘制出图片以及其GTBOXs
# -*- coding: utf-8 -*-
#！/usr/bin/env python2
import collections
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import json
import os


MOD = ['32PSK', '16APSK', '32QAM', 'FM', 'GMSK', '32APSK', 'OQPSK', '8ASK',
     'BPSK', '8PSK', 'AM-SSB-SC', '4ASK', '16PSK', '64APSK', '128QAM', '128APSK', 'AM-DSB-SC',
     'AM-SSB-WC', '64QAM', 'QPSK', '256QAM', 'AM-DSB-WC', 'OOK', '16QAM']

STANDARD_COLORS = [
     'Chartreuse', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque',
    'BlanchedAlmond', 'BlueViolet', 'BurlyWood','AntiqueWhite',
    'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan',
    'DarkCyan', 'DarkGoldenRod', 'DarkGrey', 'DarkKhaki', 'DarkOrange',
    'DarkOrchid', 'DarkSalmon', 'DarkTurquoise', 'DarkViolet',
    'DeepPink',  'DodgerBlue', 'FireBrick', 'FloralWhite',
     'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod',
    'Salmon', 'Tan', 'HoneyDew', 'HotPink', 'IndianRed', 'Ivory', 'Khaki',
    'Lavender', 'LavenderBlush',  'LemonChiffon',
    'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey',
     'LightPink', 'LightSalmon','LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime',
    'Linen', 'Magenta', 'MediumAquaMarine', 'MediumOrchid',
    'MediumPurple', 'MediumTurquoise', 'MediumVioletRed', 'MintCream', 'MistyRose', 'Moccasin',
    'NavajoWhite', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed',
    'Orchid', 'PaleGoldenRod', 'PaleTurquoise', 'PaleVioletRed',
    'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple',
    'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'SandyBrown',
    'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue',
    'SlateGray', 'SlateGrey', 'Snow', 'SteelBlue',
    'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
    'WhiteSmoke']

def box_and_text(boxes, classes, box_to_display_str_map, box_to_color_map):
    for i in range(boxes.shape[0]):
        box = tuple(boxes[i].tolist())  # numpy -> list -> tuple
        class_name = classes[i]
        display_str = str(class_name)
        display_str = '{}'.format(display_str)
        box_to_display_str_map[box].append(display_str)
        box_to_color_map[box] = STANDARD_COLORS[MOD.index(classes[i])]


def draw_text(draw, box_to_display_str_map, box, left, right, top, bottom, color):
    try:
        font = ImageFont.truetype('arial.ttf', 24)
    except IOError:
        font = ImageFont.load_default()

    # If the total height of the display strings added to the top of the bounding
    # box exceeds the top of the image, stack the strings below the bounding box
    # instead of above.
    display_str_heights = [font.getsize(ds)[1] for ds in box_to_display_str_map[box]]
    # Each display_str has a top and bottom margin of 0.05x.
    total_display_str_height = (1 + 2 * 0.05) * sum(display_str_heights)

    if top > total_display_str_height:
        text_bottom = top
    else:
        text_bottom = bottom + total_display_str_height
    # Reverse list and print from bottom to top.
    for display_str in box_to_display_str_map[box][::-1]:
        text_width, text_height = font.getsize(display_str)
        margin = np.ceil(0.05 * text_height)
        draw.rectangle([(left, text_bottom - text_height - 2 * margin),
                        (left + text_width, text_bottom)], fill=color)
        draw.text((left + margin, text_bottom - text_height - margin),
                  display_str,
                  fill='black',
                  font=font)
        text_bottom -= text_height - 2 * margin


def draw_box(image, boxes, classes, line_thickness=3):
    box_to_display_str_map = collections.defaultdict(list)
    box_to_color_map = collections.defaultdict(str)

    box_and_text(boxes, classes, box_to_display_str_map, box_to_color_map)

    # Draw all boxes onto image.
    draw = ImageDraw.Draw(image)
    im_width, im_height = image.size
    for box, color in box_to_color_map.items():
        xmin, ymin, xmax, ymax = box
        (left, right, top, bottom) = (xmin * 1, xmax * 1,
                                      ymin * 1, ymax * 1)
        draw.line([(left, top), (left, bottom), (right, bottom),
                   (right, top), (left, top)], width=line_thickness, fill=color)
        draw_text(draw, box_to_display_str_map, box, left, right, top, bottom, color)

def trans(boxes,duration_time,usrp_center_fre = 2.002e9,whole_bd=40e6):
    '''
    转换为x_min,y_min,x_max,y_max
    :param boxes:
    :param usrp_center_fre:
    :param duration_time:
    :param whole_bd:
    :return:
    '''
    trans_param =[]
    for num in range(len(boxes)):
        temp_param = np.zeros(boxes[num].shape)
        box = boxes[num]
        start_fre = usrp_center_fre-whole_bd/2
        for i in range(box.shape[0]):
            start_time = box[i,0]/duration_time
            end_time = box[i,1] / duration_time
            center_fre = (box[i,2]-start_fre) / whole_bd
            bandwidth = box[i,3] / whole_bd

            temp_param[i,0] = center_fre - bandwidth/2
            temp_param[i,1] = start_time
            temp_param[i,2] = center_fre + bandwidth/2
            temp_param[i,3] = end_time
        trans_param.append(temp_param)

    return trans_param

def param_to_img(boxes,img_size):
    boxes[:, [0, 2]] = boxes[:, [0, 2]] * img_size[0]
    boxes[:, [1, 3]] = boxes[:, [1, 3]] * img_size[1]

    return boxes

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

def filepath(train_path,json_path):
    train_name = sorted([file.split(".")[0] for file in os.listdir(train_path)])
    json_name = sorted([file.split(".")[0] for file in os.listdir(json_path)])
    return train_name,json_name

if __name__ == '__main__':
    # --------------该系列参数根据usrp配置模式及时更正-----
    usrp_rec_center_fre = 2.012e9
    duration_time = 6.71
    bandwidth = 20e6

    train_path= 'train/'
    json_path='json/'

    train_file,json_file = filepath(train_path,json_path)
    for i in range(len(train_file)):
        original_img = Image.open('train/'+train_file[i]+'.png')
        original_img_size = original_img.size
        boxes,classes = read_json('json/'+json_file[i]+'.json')
        
        boxes = trans(boxes,usrp_center_fre = usrp_rec_center_fre,duration_time=duration_time,whole_bd=bandwidth)
        
        for j in range(len(boxes)):
            box = boxes[j]
            mod_class = classes[j]
            box = param_to_img(box,original_img_size)
            draw_box(original_img,box,mod_class)
        plt.imshow(original_img)
        plt.savefig('plot/'+json_file[i]+'.png')
	print 'plot finished!'
