#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Usrp Tx 4
# Generated: Mon Jan 18 19:55:28 2021
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
import time
import sched
##----
from config_source import config_source,unpack_json
import datetime
import socket
import json
import argparse
se_ip_port=('192.168.11.207',9589)
cl_ip_port=('192.168.11.211',9580)

class usrp_tx_4(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Usrp Tx 4")

        ##################################################
        # Variables
        ##################################################
        self.usrp_samp_rate_3 = usrp_samp_rate_3 = 40e6
        self.usrp_samp_rate_2 = usrp_samp_rate_2 = 40e6
        self.usrp_samp_rate_1 = usrp_samp_rate_1 = 40e6
        self.usrp_samp_rate_0 = usrp_samp_rate_0 = 40e6
        self.usrp_gain_3 = usrp_gain_3 = 0
        self.usrp_gain_2 = usrp_gain_2 = 0
        self.usrp_gain_1 = usrp_gain_1 = 0
        self.usrp_gain_0 = usrp_gain_0 = 0
        self.usrp_center_fre_3 = usrp_center_fre_3 = 2.002e9
        self.usrp_center_fre_2 = usrp_center_fre_2 = 2.002e9
        self.usrp_center_fre_1 = usrp_center_fre_1 = 1.992e9
        self.usrp_center_fre_0 = usrp_center_fre_0 = 2.012e9
        self.usrp_addr_3 = usrp_addr_3 = 'addr0=192.168.10.13'
        self.usrp_addr_2 = usrp_addr_2 = 'addr0=192.168.10.18'
        self.usrp_addr_1 = usrp_addr_1 = 'addr0=192.168.10.17'
        self.usrp_addr_0 = usrp_addr_0 = 'addr0=192.168.10.16'
        self.signal_source_path_3 = signal_source_path_3 = '/home/qxslab/lcg/dataset_radioml/dataset_all_gnuradio/4ASK/30/4ASK_30dB_0.csv'
        self.signal_source_path_2 = signal_source_path_2 = '/home/qxslab/lcg/dataset_radioml/dataset_all_gnuradio/4ASK/30/4ASK_30dB_0.csv'
        self.signal_source_path_1 = signal_source_path_1 ='/home/qxslab/lcg/dataset_radioml/dataset_all_gnuradio/4ASK/30/4ASK_30dB_0.csv'
        self.signal_source_path_0 = signal_source_path_0 = '/home/qxslab/lcg/dataset_radioml/dataset_all_gnuradio/4ASK/30/4ASK_30dB_0.csv'
        self.choose_val_3 = choose_val_3 = 1
        self.choose_val_2 = choose_val_2 = 1
        self.choose_val_1 = choose_val_1 = 1
        self.choose_val_0 = choose_val_0 = 1

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_3 = uhd.usrp_sink(
        	",".join((usrp_addr_3, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_3.set_samp_rate(usrp_samp_rate_3)
        self.uhd_usrp_sink_3.set_center_freq(usrp_center_fre_3, 0)
        self.uhd_usrp_sink_3.set_gain(usrp_gain_3, 0)
        self.uhd_usrp_sink_3.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_2 = uhd.usrp_sink(
        	",".join((usrp_addr_2, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_2.set_samp_rate(usrp_samp_rate_2)
        self.uhd_usrp_sink_2.set_center_freq(usrp_center_fre_2, 0)
        self.uhd_usrp_sink_2.set_gain(usrp_gain_2, 0)
        self.uhd_usrp_sink_2.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_1 = uhd.usrp_sink(
        	",".join((usrp_addr_1, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_1.set_samp_rate(usrp_samp_rate_1)
        self.uhd_usrp_sink_1.set_center_freq(usrp_center_fre_1, 0)
        self.uhd_usrp_sink_1.set_gain(usrp_gain_1, 0)
        self.uhd_usrp_sink_1.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join((usrp_addr_0, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(usrp_samp_rate_0)
        self.uhd_usrp_sink_0.set_center_freq(usrp_center_fre_0, 0)
        self.uhd_usrp_sink_0.set_gain(usrp_gain_0, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.selector_3 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=choose_val_3,
        	output_index=0,
        )
        self.selector_2 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=choose_val_2,
        	output_index=0,
        )
        self.selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=choose_val_1,
        	output_index=0,
        )
        self.selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=choose_val_0,
        	output_index=0,
        )
        self.radio_source_3 = blocks.file_source(gr.sizeof_gr_complex*1, signal_source_path_3, True)
        self.radio_source_3.set_begin_tag(pmt.PMT_NIL)
        self.radio_source_2 = blocks.file_source(gr.sizeof_gr_complex*1, signal_source_path_2, True)
        self.radio_source_2.set_begin_tag(pmt.PMT_NIL)
        self.radio_source_1 = blocks.file_source(gr.sizeof_gr_complex*1, signal_source_path_1, True)
        self.radio_source_1.set_begin_tag(pmt.PMT_NIL)
        self.radio_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, signal_source_path_0, True)
        self.radio_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_3 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_2 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_2, 0), (self.selector_2, 1))
        self.connect((self.analog_const_source_3, 0), (self.selector_3, 1))
        self.connect((self.analog_const_source_x_0, 0), (self.selector_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.selector_1, 1))
        self.connect((self.radio_source_0, 0), (self.selector_0, 0))
        self.connect((self.radio_source_1, 0), (self.selector_1, 0))
        self.connect((self.radio_source_2, 0), (self.selector_2, 0))
        self.connect((self.radio_source_3, 0), (self.selector_3, 0))
        self.connect((self.selector_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.selector_1, 0), (self.uhd_usrp_sink_1, 0))
        self.connect((self.selector_2, 0), (self.uhd_usrp_sink_2, 0))
        self.connect((self.selector_3, 0), (self.uhd_usrp_sink_3, 0))

    def get_usrp_samp_rate_3(self):
        return self.usrp_samp_rate_3

    def set_usrp_samp_rate_3(self, usrp_samp_rate_3):
        self.usrp_samp_rate_3 = usrp_samp_rate_3
        self.uhd_usrp_sink_3.set_samp_rate(self.usrp_samp_rate_3)

    def get_usrp_samp_rate_2(self):
        return self.usrp_samp_rate_2

    def set_usrp_samp_rate_2(self, usrp_samp_rate_2):
        self.usrp_samp_rate_2 = usrp_samp_rate_2
        self.uhd_usrp_sink_2.set_samp_rate(self.usrp_samp_rate_2)

    def get_usrp_samp_rate_1(self):
        return self.usrp_samp_rate_1

    def set_usrp_samp_rate_1(self, usrp_samp_rate_1):
        self.usrp_samp_rate_1 = usrp_samp_rate_1
        self.uhd_usrp_sink_1.set_samp_rate(self.usrp_samp_rate_1)

    def get_usrp_samp_rate_0(self):
        return self.usrp_samp_rate_0

    def set_usrp_samp_rate_0(self, usrp_samp_rate_0):
        self.usrp_samp_rate_0 = usrp_samp_rate_0
        self.uhd_usrp_sink_0.set_samp_rate(self.usrp_samp_rate_0)

    def get_usrp_gain_3(self):
        return self.usrp_gain_3

    def set_usrp_gain_3(self, usrp_gain_3):
        self.usrp_gain_3 = usrp_gain_3
        self.uhd_usrp_sink_3.set_gain(self.usrp_gain_3, 0)


    def get_usrp_gain_2(self):
        return self.usrp_gain_2

    def set_usrp_gain_2(self, usrp_gain_2):
        self.usrp_gain_2 = usrp_gain_2
        self.uhd_usrp_sink_2.set_gain(self.usrp_gain_2, 0)


    def get_usrp_gain_1(self):
        return self.usrp_gain_1

    def set_usrp_gain_1(self, usrp_gain_1):
        self.usrp_gain_1 = usrp_gain_1
        self.uhd_usrp_sink_1.set_gain(self.usrp_gain_1, 0)


    def get_usrp_gain_0(self):
        return self.usrp_gain_0

    def set_usrp_gain_0(self, usrp_gain_0):
        self.usrp_gain_0 = usrp_gain_0
        self.uhd_usrp_sink_0.set_gain(self.usrp_gain_0, 0)


    def get_usrp_center_fre_3(self):
        return self.usrp_center_fre_3

    def set_usrp_center_fre_3(self, usrp_center_fre_3):
        self.usrp_center_fre_3 = usrp_center_fre_3
        self.uhd_usrp_sink_3.set_center_freq(self.usrp_center_fre_3, 0)

    def get_usrp_center_fre_2(self):
        return self.usrp_center_fre_2

    def set_usrp_center_fre_2(self, usrp_center_fre_2):
        self.usrp_center_fre_2 = usrp_center_fre_2
        self.uhd_usrp_sink_2.set_center_freq(self.usrp_center_fre_2, 0)

    def get_usrp_center_fre_1(self):
        return self.usrp_center_fre_1

    def set_usrp_center_fre_1(self, usrp_center_fre_1):
        self.usrp_center_fre_1 = usrp_center_fre_1
        self.uhd_usrp_sink_1.set_center_freq(self.usrp_center_fre_1, 0)

    def get_usrp_center_fre_0(self):
        return self.usrp_center_fre_0

    def set_usrp_center_fre_0(self, usrp_center_fre_0):
        self.usrp_center_fre_0 = usrp_center_fre_0
        self.uhd_usrp_sink_0.set_center_freq(self.usrp_center_fre_0, 0)

    def get_usrp_addr_3(self):
        return self.usrp_addr_3

    def set_usrp_addr_3(self, usrp_addr_3):
        self.usrp_addr_3 = usrp_addr_3

    def get_usrp_addr_2(self):
        return self.usrp_addr_2

    def set_usrp_addr_2(self, usrp_addr_2):
        self.usrp_addr_2 = usrp_addr_2

    def get_usrp_addr_1(self):
        return self.usrp_addr_1

    def set_usrp_addr_1(self, usrp_addr_1):
        self.usrp_addr_1 = usrp_addr_1

    def get_usrp_addr_0(self):
        return self.usrp_addr_0

    def set_usrp_addr_0(self, usrp_addr_0):
        self.usrp_addr_0 = usrp_addr_0

    def get_signal_source_path_3(self):
        return self.signal_source_path_3

    def set_signal_source_path_3(self, signal_source_path_3):
        self.signal_source_path_3 = signal_source_path_3
        self.radio_source_3.open(self.signal_source_path_3, True)

    def get_signal_source_path_2(self):
        return self.signal_source_path_2

    def set_signal_source_path_2(self, signal_source_path_2):
        self.signal_source_path_2 = signal_source_path_2
        self.radio_source_2.open(self.signal_source_path_2, True)

    def get_signal_source_path_1(self):
        return self.signal_source_path_1

    def set_signal_source_path_1(self, signal_source_path_1):
        self.signal_source_path_1 = signal_source_path_1
        self.radio_source_1.open(self.signal_source_path_1, True)

    def get_signal_source_path_0(self):
        return self.signal_source_path_0

    def set_signal_source_path_0(self, signal_source_path_0):
        self.signal_source_path_0 = signal_source_path_0
        self.radio_source_0.open(self.signal_source_path_0, True)

    def get_choose_val_3(self):
        return self.choose_val_3

    def set_choose_val_3(self, choose_val_3):
        self.choose_val_3 = choose_val_3
        self.selector_3.set_input_index(int(self.choose_val_3))

    def get_choose_val_2(self):
        return self.choose_val_2

    def set_choose_val_2(self, choose_val_2):
        self.choose_val_2 = choose_val_2
        self.selector_2.set_input_index(int(self.choose_val_2))

    def get_choose_val_1(self):
        return self.choose_val_1

    def set_choose_val_1(self, choose_val_1):
        self.choose_val_1 = choose_val_1
        self.selector_1.set_input_index(int(self.choose_val_1))

    def get_choose_val_0(self):
        return self.choose_val_0

    def set_choose_val_0(self, choose_val_0):
        self.choose_val_0 = choose_val_0
        self.selector_0.set_input_index(int(self.choose_val_0))

def start_block_0(top_block_cls,center_fre,filepath):
    top_block_cls.set_signal_source_path_0(filepath)
    top_block_cls.set_usrp_center_fre_0(center_fre)
    top_block_cls.set_choose_val_0(0)


def end_block_0(top_block_cls):
    top_block_cls.set_choose_val_0(1)


def set_param_0(s,top_block_cls,json,num,dt=0):

    start_time, end_time, center_fres, filepath = unpack_json(json,num)

    for i in range(len(start_time)):
        s.enter(start_time[i]+dt,10*(num+1),start_block_0,(top_block_cls,center_fres[i],filepath[i]))
        s.enter(end_time[i]+dt,1*(num+1),end_block_0,(top_block_cls,))

def start_block_1(top_block_cls,center_fre,filepath):
    top_block_cls.set_signal_source_path_1(filepath)
    top_block_cls.set_usrp_center_fre_1(center_fre)
    top_block_cls.set_choose_val_1(0)


def end_block_1(top_block_cls):
    top_block_cls.set_choose_val_1(1)


def set_param_1(s,top_block_cls,json,num,dt=0):

    start_time, end_time, center_fres, filepath = unpack_json(json,num)

    for i in range(len(start_time)):
        s.enter(start_time[i]+dt,10*(num+1),start_block_1,(top_block_cls,center_fres[i],filepath[i]))
        s.enter(end_time[i]+dt,1*(num+1),end_block_1,(top_block_cls,))

def start_block_2(top_block_cls,center_fre,filepath):
    top_block_cls.set_signal_source_path_2(filepath)
    top_block_cls.set_usrp_center_fre_2(center_fre)
    top_block_cls.set_choose_val_2(0)


def end_block_2(top_block_cls):
    top_block_cls.set_choose_val_2(1)


def set_param_2(s,top_block_cls,json,num,dt=0):

    start_time, end_time, center_fres, filepath = unpack_json(json,num)

    for i in range(len(start_time)):
        s.enter(start_time[i]+dt,10*(num+1),start_block_2,(top_block_cls,center_fres[i],filepath[i]))
        s.enter(end_time[i]+dt,1*(num+1),end_block_2,(top_block_cls,))

def start_block_3(top_block_cls,center_fre,filepath):
    top_block_cls.set_signal_source_path_3(filepath)
    top_block_cls.set_usrp_center_fre_3(center_fre)
    top_block_cls.set_choose_val_3(0)


def end_block_3(top_block_cls):
    top_block_cls.set_choose_val_3(1)


def set_param_3(s,top_block_cls,json,num,dt=0):

    start_time, end_time, center_fres, filepath = unpack_json(json,num)

    for i in range(len(start_time)):
        s.enter(start_time[i]+dt,10*(num+1),start_block_3,(top_block_cls,center_fres[i],filepath[i]))
        s.enter(end_time[i]+dt,1*(num+1),end_block_3,(top_block_cls,))


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

def main(top_block_cls=usrp_tx_4, options=None):
    args = parse_args()


    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    udp.bind(cl_ip_port)
    usrp_addr = ['addr=192.168.10.18','addr=192.168.10.17','addr=192.168.10.16','addr=192.168.10.13']
    usrp_samp_rate = args.rate
    assert len(usrp_samp_rate)==4,'Error!Need 4 Sample Rate For 4 USRPs'
    signal_num = 4
    # 根据USRP配置参数进行修改
    center_fres = args.usrpcenterfre
    sample_rate = args.usrprate
    tb = top_block_cls()

    tb.set_usrp_addr_0(usrp_addr[0])
    tb.set_usrp_addr_1(usrp_addr[1])
    tb.set_usrp_addr_2(usrp_addr[2])
    tb.set_usrp_addr_3(usrp_addr[3])
    tb.set_usrp_samp_rate_0(usrp_samp_rate[0])
    tb.set_usrp_samp_rate_1(usrp_samp_rate[1])
    tb.set_usrp_samp_rate_2(usrp_samp_rate[2])
    tb.set_usrp_samp_rate_3(usrp_samp_rate[3])
    tb.start()
    print '+===============signal4================+'
    send_num = 0
    for i in range(args.cycle):

        jsontext = config_source(signal_num, usrp_samp_rate, usrp_center_fre=center_fres,usrp_rec_sample_rate=sample_rate, duration_time=6.71,skip_fre=args.skip)
        jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '))
        filename = 'json/' + datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S') + '.json'
        f = open(filename, 'w')
        f.write(jsondata)
        f.close()

        s = sched.scheduler(time.time, time.sleep)

        set_param_0(s, tb, jsontext, 0,args.dt[0])
        set_param_1(s, tb, jsontext, 1,args.dt[1])
        set_param_2(s, tb, jsontext, 2,args.dt[2])
        set_param_3(s, tb, jsontext, 3,args.dt[3])

        udp.sendto('0', se_ip_port)

        print '+--------------------------------+'
        print 'run Time', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        send_num += 1
        print send_num
        s.run()
        while True:
            data = udp.recv(1024)
            if data == '1':
                break
    udp.sendto('2', se_ip_port)
    udp.close()
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
