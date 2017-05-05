import paramiko
import pprint #pretty print result, not necessary
import threading 

flag=1

def ssh2(ip,port,username,passwd,timeout=10):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,username,passwd)
    stdin, stdout, stderr = ssh.exec_command("ls") 
    #print(stdout.readlines()) 
    if len(stdout.readlines())>=0:
       flag=0
       file = open(ip+".txt","w") 
       file.close()
       print ip+'-------------------------------------------------------------------'
    ssh.close()

#ssh2('210.45.249.238',22,'chenlei','123')


for i in range(1,254):
	print('210.45.249.'+str(i))
	#ssh2('210.45.249.'+str(i),22,'chenlei','lei')
	#ssh.close()
	if flag==1:
	    t1 = threading.Thread(target=ssh2,args=('210.45.249.'+str(i),22,'username','password',))
	    t1.start()
 
