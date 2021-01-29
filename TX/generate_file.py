# -*- coding: UTF-8 -*-
import os
import numpy as np


def generate_file(root):
    MOD = ['32PSK', '16APSK', '32QAM', 'FM', 'GMSK', '32APSK', 'OQPSK', '8ASK',
     'BPSK', '8PSK', 'AM-SSB-SC', '4ASK', '16PSK', '64APSK', '128QAM', '128APSK', 'AM-DSB-SC',
     'AM-SSB-WC', '64QAM', 'QPSK', '256QAM', 'AM-DSB-WC', 'OOK', '16QAM']
    SNR = range(-20,32,2)

    root = root
    mod = MOD[np.random.randint(0,24,1).item()]
    snr = SNR[np.random.randint(0,26,1).item()]
    num = np.random.randint(0,4096,1).item()

    filepath = os.path.join(root,mod,str(snr),'{}_{}dB_{}.csv'.format(mod,snr,num))

    return filepath,mod
