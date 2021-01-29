#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017-2018 Ettus Research, a National Instruments Company
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""
RX samples to file using Python API
"""

import argparse
import numpy as np
import uhd
import datetime,time
import socket
import os
import sys

se_ip_port = ('192.168.11.207', 9589)
cl_ip_port = ('192.168.11.211', 9580)

class Logger(object):

    def __init__(self, stream=sys.stdout):
        output_dir = "log/time.strftime('%Y-%m-%d-%H-%M')"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H-%M'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def parse_args():
    """Parse the command line arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--centerfre",required=True, type=float)
    parser.add_argument("-r", "--rate", required=True, type=float)

    return parser.parse_args()

def main():
    args = parse_args()

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    udp.bind(se_ip_port)
    

    """RX samples and write to file"""
    usrp_sample_rate = args.rate
    center_fre = args.centerfre
    usrp_addr = 'addr=192.168.10.29'
    duration = 6.8
    gain=10
    #配置usrp
    usrp = uhd.usrp.MultiUSRP(usrp_addr)
    num_samps = int(np.ceil(duration*usrp_sample_rate))

    udp.sendto('1', cl_ip_port)

    while True:
        data = udp.recv(1024)
        if data=='0':
            time.sleep(0.37)
            break
        if data=='2':
            udp.close()
            print '2'
            sys.exit(0)

    
    print('receive start:', datetime.datetime.now().strftime('%H:%M:%S.%f'))
    samps = usrp.recv_num_samps(num_samps, center_fre, usrp_sample_rate, [0],gain)

    output_name = 'raw/' +datetime.datetime.now().strftime(('%Y-%m-%d-%H%M%S'))+'.txt'
    #output_name = 'raw/record.txt'
    with open(output_name, 'wb') as out_file:
        samps.tofile(out_file)
        
 
    udp.close() #关闭UDP服务


if __name__ == "__main__":
    # sys.stderr = Logger(sys.stderr)  # 将错误信息记录到log
    main()

