#!/usr/bin/env python3 

import paramiko
import time  

IP = '10.42.0.70'
USERNAME = 'rock'
PASSWORD = 'rock'


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=IP, username=USERNAME, password=PASSWORD)
stdin, stdout, stderr = ssh_client.exec_command("sudo su")
print(stdout.readlines())
stdin.write("rock\n")
print("connected!")
print('exec on')
ssh_client.exec_command("nmcli r wifi on")
time.sleep(5)

print('exec list')
s1,s2,s3 = ssh_client.exec_command("nmcli d wifi list")
time.sleep(5)
print(s2.readlines())

print('exec connection')
s1,s2,s3 = ssh_client.exec_command("nmcli d wifi connect VodafoneA66208560 password bbzmecflaht7y2f5")
time.sleep(15)
print(s2.readlines())

print('exec close')
ssh_client.close()
