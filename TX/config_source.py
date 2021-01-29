# -*- coding: UTF-8 -*-
from generate_time import generate_time
from generate_fre import generate_center_fre,generate_str_end_fre
from generate_file import generate_file
import json
import datetime

def config_source(signal_num,usrp_sample_rate,usrp_center_fre=2.012e9,usrp_rec_sample_rate=20e6,duration_time=10,skip_fre=False):

    str_end_fre = generate_str_end_fre(signal_num,usrp_center_fre=usrp_center_fre,usrp_rec_sample_rate=usrp_rec_sample_rate)
    jsontext = {'signal_num':signal_num}
    bandwidth = [x/8 for x in usrp_sample_rate]  #信号源八倍过采样，所以除8得到信号的带宽
    for num_sig in range(signal_num):
        jsontext.update({'signal_block_{}'.format(str(num_sig)):[]})
        start_time, end_time = generate_time(duration_time)
        center_fres = generate_center_fre(1, bandwidth[num_sig], str_end_fre[num_sig])
        filepath, mod = generate_file(root='/home/qxslab/lcg/dataset_radioml/dataset_all_gnuradio')
        for i in range(len(start_time)):
            if skip_fre:
                center_fres = generate_center_fre(1, bandwidth[num_sig], str_end_fre[num_sig])
            jsontext['signal_block_{}'.format(str(num_sig))].append({'start_time': float(start_time[i]), 'end_time': float(end_time[i]),
                                              'center_fre':float(center_fres), 'bandwidth':float(bandwidth[num_sig]),
                                              'modulation':mod,'filepath':filepath})

    return jsontext

def unpack_json(jsontext,num_blc):
    signal_data = jsontext
    x = signal_data['signal_block_{}'.format(num_blc)]
    start_time = []
    end_time = []
    center_fre = []
    filepath = []

    for j in range(len(x)):
        start_time.append(x[j]['start_time'])
        end_time.append(x[j]['end_time'])
        center_fre.append(x[j]['center_fre'])
        filepath.append(x[j]['filepath'])


    return start_time,end_time,center_fre,filepath


if __name__ == '__main__':
    signal_data = config_source(2,[40e6,40e6],duration_time=6.8)

    x = signal_data['signal_block_{}'.format(0)]
    start_time = []
    end_time = []
    center_fre = []
    filepath = []
    bandwidth = []
    for j in range(len(x)):
        start_time.append(x[j]['start_time'])
        end_time.append(x[j]['end_time'])
        center_fre.append(x[j]['center_fre'])
        filepath.append(x[j]['filepath'])
        bandwidth.append(x[j]['bandwidth'])
    print(start_time)
    print(end_time)
    print(bandwidth)
    print(center_fre)
    print(filepath)


