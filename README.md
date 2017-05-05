# findMyService
实验室服务器的ip不知道是多少了，接显示屏也无法显示了。写了一个python代码去查找自己的服务器的ip

由于需要import Paramiko。通过以下命令即可安装
pip install paramiko

## 你需要修改的
threading.Thread(target=ssh2,args=('210.45.249.'+str(i),22,'username','password',))
需要填上你对应的ip和用户名密码。
## 结果
python findMyService.py
结果就会在同一级的目录下生成以你的有权访问的ip地址生成的txt的文件名。
