# -*- coding: UTF-8 -*-
import numpy as np


def generate_time(duration_time):
    '''

    :param all_time: duration_time时间窗口长度，默认10s
    :return: start_time,end_time，数组，每一组对应开始和结束时间
    '''
    all_time = 100 #生成时间序列基本值100
    used_time = 5*duration_time #最小时间块长度
    assert all_time>50,"time is too short"
    times = all_time/float(duration_time)
    duration_time = np.random.randint(used_time,all_time-10,1).item()
    last_time =all_time - duration_time
    start_time = [0]
    end_time = [0]
    temp_time=0

    while 1:
        if last_time<=5:
            break
        gap_time = np.random.randint(5,last_time,1).item()
        start_time.append(gap_time+end_time[-1])
        duration_time = duration_time - temp_time
        temp_time = np.random.randint(0,duration_time,1).item()
        end_time.append((start_time[-1]+temp_time))
        last_time = last_time-gap_time


    end_time[-1] += temp_time
    if end_time[-1]>all_time:
        end_time[-1]=all_time-1

    index = list(np.where((np.array(end_time)-np.array(start_time)) == 0)[0])

    for i in range(len(index)):
        start_time = np.delete(list(start_time), index[i]-i)
        end_time = np.delete(list(end_time),index[i]-i)

    if not len(start_time):
        start_time=np.array([15,35])
        end_time = np.array([25,45])
    return start_time/times,end_time/times

if __name__=='__main__':
    start_time,end_time =generate_time(6.8)
    print(type(start_time))
    print(start_time)
