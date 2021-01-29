#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Usrp Signal Tx
# Generated: Mon Jan 18 10:18:19 2021
# GNU Radio version: 3.7.12.0
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import pmt
import sched
import argparse
##----
from config_source import config_source,unpack_json
import datetime
import socket
import json

se_ip_port=('192.168.11.207',9589)
cl_ip_port=('192.168.11.211',9580)

import time
import os
import sys

class Logger(object):

    def __init__(self, stream=sys.stdout):
        output_dir = "log"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H-%M-%S'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

class usrp_signal_tx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Usrp Signal Tx")

        ##################################################
        # Variables
        ##################################################
        self.usrp_samp_rate = usrp_samp_rate = 40e6
        self.usrp_gain = usrp_gain = 0
        self.usrp_center_fre = usrp_center_fre = 2.002e9
        self.usrp_addr = usrp_addr = 'addr=192.168.10.18'
        self.signal_source_path = signal_source_path = '/home/qxslab/lcg/dataset_radioml/dataset_all_gnuradio/4ASK/30/4ASK_30dB_0.csv'
        self.choose_val = choose_val = 1

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join((usrp_addr, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(usrp_samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(usrp_center_fre, 0)
        self.uhd_usrp_sink_0.set_gain(usrp_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=choose_val,
        	output_index=0,
        )
        self.radio_source = blocks.file_source(gr.sizeof_gr_complex*1, signal_source_path, True)
        self.radio_source.set_begin_tag(pmt.PMT_NIL)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.selector_1, 1))
        self.connect((self.radio_source, 0), (self.selector_1, 0))
        self.connect((self.selector_1, 0), (self.uhd_usrp_sink_0, 0))

    def get_usrp_samp_rate(self):
        return self.usrp_samp_rate

    def set_usrp_samp_rate(self, usrp_samp_rate):
        self.usrp_samp_rate = usrp_samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.usrp_samp_rate)

    def get_usrp_gain(self):
        return self.usrp_gain

    def set_usrp_gain(self, usrp_gain):
        self.usrp_gain = usrp_gain
        self.uhd_usrp_sink_0.set_gain(self.usrp_gain, 0)


    def get_usrp_center_fre(self):
        return self.usrp_center_fre

    def set_usrp_center_fre(self, usrp_center_fre):
        self.usrp_center_fre = usrp_center_fre
        self.uhd_usrp_sink_0.set_center_freq(self.usrp_center_fre, 0)

    def get_usrp_addr(self):
        return self.usrp_addr

    def set_usrp_addr(self, usrp_addr):
        self.usrp_addr = usrp_addr

    def get_signal_source_path(self):
        return self.signal_source_path

    def set_signal_source_path(self, signal_source_path):
        self.signal_source_path = signal_source_path
        self.radio_source.open(self.signal_source_path, True)

    def get_choose_val(self):
        return self.choose_val

    def set_choose_val(self, choose_val):
        self.choose_val = choose_val
        self.selector_1.set_input_index(int(self.choose_val))

def start_block(top_block_cls,center_fre,filepath):

    top_block_cls.set_signal_source_path(filepath)
    top_block_cls.set_usrp_center_fre(center_fre)
    top_block_cls.set_choose_val(0)
    

def end_block(top_block_cls):
    top_block_cls.set_choose_val(1)
    

def set_param(s,top_block_cls,json,num,dt):

    start_time, end_time, center_fres, filepath = unpack_json(json,num)

    for i in range(len(start_time)):
        s.enter(start_time[i]+dt,2,start_block,(top_block_cls,center_fres[i],filepath[i]))
        s.enter(end_time[i]+dt,1,end_block,(top_block_cls,))

def parse_args():
    """Parse the command line arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cycle", type=int, required=True)
    parser.add_argument("-d", "--dt", nargs='+', type=float)
    parser.add_argument("-r", "--rate", nargs='+', type=float)
    parser.add_argument("-s", "--skip", type=bool, default=False)
    parser.add_argument("-uc", "--usrpcenterfre", required=True, type=float)
    parser.add_argument("-ur", "--usrprate", required=True, type=float)
    return parser.parse_args()

def main(top_block_cls=usrp_signal_tx, options=None):
    args = parse_args()

    #打开UDP服务，监听端口
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    udp.bind(cl_ip_port)

    usrp_addr = 'addr=192.168.10.18'
    usrp_samp_rate = args.rate
    assert len(usrp_samp_rate) == 1, 'Error!Need 1 Sample Rate For 1 USRP'
    #设置发射信号数目
    signal_num = 1
    #根据USRP配置参数进行修改
    center_fres=args.usrpcenterfre
    sample_rate=args.usrprate
    tb = top_block_cls()
    tb.set_usrp_addr(usrp_addr)
    tb.set_usrp_samp_rate(usrp_samp_rate[0])
    tb.start()
    print '+===============signal1================+'
    send_num = 0
    for i in range(args.cycle):

        jsontext = config_source(signal_num,usrp_samp_rate,usrp_center_fre=center_fres,usrp_rec_sample_rate=sample_rate,duration_time=6.71,skip_fre=args.skip)
        jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '))
        filename = 'json/' + datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '.json'
        f = open(filename, 'w')
        f.write(jsondata)
        f.close()

        s = sched.scheduler(time.time, time.sleep)

        set_param(s,tb,jsontext,0,args.dt[0])

	    #UDP通信，告知rec端准备接收
        udp.sendto('0', se_ip_port)

        print '+--------------------------------+'
        print 'run Time', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        send_num +=1
        print send_num
        s.run()
	    #发送完毕，等待接受端再次发送的指令
        while True:
            data = udp.recv(1024)
            if data =='1':
                break

    udp.sendto('2', se_ip_port)
    udp.close()
    tb.stop()
    tb.wait()


if __name__ == '__main__':

    #sys.stdout = Logger(sys.stdout)  # 将输出记录到log
    main()
