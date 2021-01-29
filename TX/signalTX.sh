#use usrp generate signal
name="json"
rm -rf $name
mkdir $name

#-r represent signal_sample_frequence:40e6,20e6,10e6
#-c represent the job ciuculate numbers:(int)>0
#-s represent whether use skip_fre:(bool)default=False
#-d represent usrp send delay time ,+ after - before,usually 20M:0,40M:0.2
#-uc represent usrp_center_fre:1.982e9,2.012e9
#-ur represent usrp_sample_rate:40e6,20e6
#10.18 10.17 10.16 10.13
sleep 10s
#python usrp_tx_1.py -r 20e6 -c 200 -s True -d 0 -uc 1.982e9 -ur 40e6
python usrp_tx_1.py -r 40e6 -c 400 -s True -d 0.2 -uc 1.982e9 -ur 40e6

#python usrp_tx_2.py -r 40e6 40e6 -c 100 -s True -d 0.2 0.2 -uc 1.982e9 -ur 40e6
#python usrp_tx_2.py -r 20e6 20e6 -c 100 -s True -d 0 0 -uc 1.982e9 -ur 40e6
#python usrp_tx_2.py -r 20e6 40e6 -c 100 -s True -d 0 0.2 -uc 1.982e9 -ur 40e6
#python usrp_tx_2.py -r 40e6 20e6 -c 100 -s True -d 0.2 0 -uc 1.982e9 -ur 40e6

#python usrp_tx_3.py -r 20e6 20e6 20e6 -c 400 -s True -d 0 0 0 -uc 1.982e9 -ur 40e6

#python usrp_tx_4.py -r 20e6 20e6 20e6 20e6 -c 400 -d 0 0 0 0 -uc 1.982e9 -ur 40e6

echo '+===============================+'
echo "Finshed MY JOB!"
#关闭USRP平台
matlab -nodesktop -nosplash -r 'shutdown;quit'

echo '================================+'
echo 'SHUTDOWN THE SYSTEM'

datetime=$(date +%Y-%m-%d-%H%M%S)
filename=$name$datetime
#将文件名改为json+当前时间
mv $name $filename
