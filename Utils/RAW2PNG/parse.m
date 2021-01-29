clear; close all; clc;

Path = 'raw/';                   % 设置数据存放的文件夹路径
File = dir(fullfile(Path,'*.txt'));  % 显示文件夹下所有符合后缀名为.txt文件的完整信息
FileNames = {File.name}';    
window = 1024; %fft长度
duration = 1024; %
sample_rate = 40e6;%USRP接收机采样率
frame_num = 256;   %根据采样率进行修改，采样率为20M时为128，采样率为40M时为256
trans_num = 0;   %记录处理完成的数量
for filenum=1:length(FileNames)
    tic
    file = FileNames{filenum};
    disp(file);
    filename = [Path,file];%
    fip=fopen(filename,'rb'); %���ֽ���ʽ���ļ�
    [SIN,num]=fread(fip, Inf,'float');%��ȡȫ������
    fclose(fip);

    
    data = zeros(frame_num, 2, window, duration);
    SIN = SIN(1:frame_num*2*window*duration);%�ض����
    SIN = reshape(SIN, 2, window*duration, frame_num);%��ݰ�֡����
    rawdata = SIN(1,:,:) + 1i*SIN(2,:,:);%�ϳ�IQ���
    times = window/frame_num;
    out_pic = zeros(2,1024,1024);

    for i=1:frame_num%
        frame = rawdata(:,:,i);%��ȡһ֡�
        %[S,F,T,P]=spectrogram(x,window,noverlap,nfft,fs)�
        %x---输入信号的向量
        %window---窗函数，默认为nfft长度的海明窗Hamming
        %noverlap---每一段的重叠样本数，默认值是在各段之间产生50%的重叠
        %nfft---做FFT变换的长度，默认为256和大于每段长度的最小2次幂之间的最大值
        %fs---采样频率，默认值归一化频率
        [S,F,T,P] = spectrogram(frame, window, 0, window,  sample_rate, 'centered');%������ͼ
%         surf(T,F,10*log10(P),'edgecolor','none')
%         view(0,90)
        for j=1:times
            out_pic(1,:,j+(i-1)*times)  = real(S(:,frame_num*j));
            out_pic(2,:,j+(i-1)*times) = imag(S(:,frame_num*j));
        end
    end
    
    out_pic = single(out_pic);%转换为单精度数组�
    final_pic = zeros(2,1024,1024);
    for i=1:1024
        final_pic(1,:,i)=out_pic(1,:,1024-i+1);
        final_pic(2,:,i)=out_pic(2,:,1024-i+1);
    end    
    
    angel_pic = final_pic(1,:,:)+1i*final_pic(2,:,:);
    
    root = pwd;
    P = average_pooling(final_pic, 2);%2*1024*1024---->256*256--4/512*512--2
    P2 = average_pooling_angle(angel_pic,2);
    S=mat2gray(10*log10(P));
    S2=mat2gray(10*log10(P2));
    S=rot90(S);
    S2=rot90(S2);
    name = file(1:17);
    imwrite(S,sprintf('%s/amplitude/%s.png',root,name));
    imwrite(S2,sprintf('%s/phase/%s.png',root,name));
    trans_num = trans_num+1;
    fprintf('finished number:%d',trans_num);
    toc
end
disp('matlab finished!!!!')
