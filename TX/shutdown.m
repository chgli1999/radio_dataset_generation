com =serial('/dev/ttyS0');    %创建串口对象
com.baudrate=57600;  %设置波特率,缺省9600bit/s
com.parity='none';  %设置校验位无奇偶校验
com.stopbits=1;     %设置停止位
try
    fopen(com);
    cmd=[72 26 0 5 7 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)
    cmd=[72 26 0 5 6 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)

    cmd=[72 26 0 5 5 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)
    cmd=[72 26 0 5 4 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)
    
    cmd=[72 26 0 5 3 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)
    cmd=[72 26 0 5 2 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)

    cmd=[72 26 0 5 1 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)
    cmd=[72 26 0 5 0 0 0 77];
    cmd=dec2hex(cmd)
    fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    recdta=fread(com,1,'uint8')
    if recdta==0
        fwrite(com,hex2dec(cmd),'int8');%写入数字数据
    end
    pause(0.1)
    fclose(com);
    delete(com);
    msgbox('系统已关闭','提示');
catch
    msgbox('串口打开失败','提示','error');
    
end