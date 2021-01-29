# -*- coding: UTF-8 -*-
import numpy as np


def generate_center_fre(num,bw,start_end_fre):
    '''

    :param num: 产生中心频率数量，根据时间段数目来定，len(start_time)
    :param bw: 信号带宽
    :param start_fre: 开始频率
    :param end_fre: 结束频率
    :return:
    '''
    assert bw<=(start_end_fre[1] - start_end_fre[0]),'bw is too big'

    center_fre = np.random.randint(start_end_fre[0] + bw / 2, start_end_fre[1] - bw / 2, num)

    return center_fre




def generate_str_end_fre(signal_num,usrp_center_fre,usrp_rec_sample_rate):
    '''

    :param signal_num: 信号数量
    :param usrp_center_fre: usrp中心频率
    :param usrp_sample_rate: usrp采样率
    :return: [(start_fre，end_fre),(),(),..],数组内的tuple
    '''
    signal_num = signal_num
    usrp_center_fre = usrp_center_fre
    usrp_sample_rate = usrp_rec_sample_rate
    str_end_fre = []

    section_fre = usrp_sample_rate/signal_num
    start_fre = usrp_center_fre - usrp_sample_rate / 2
    for i in range(signal_num):
        end_fre = start_fre+section_fre
        str_end_fre.append((start_fre,end_fre))
        start_fre = start_fre+section_fre

    return str_end_fre

if __name__=='__main__':
    str_end_fre=  generate_str_end_fre(signal_num=5,usrp_center_fre=1.98e9,usrp_sample_rate=40e6)
    print(str_end_fre)

