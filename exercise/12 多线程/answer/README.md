# 练习一 多线程文件名称查找
1. 对某一文件夹启动10个线程查找文件包含abc三个字符的文件名，并显示该文件所在的路径
2. 尽量使用面向对象编程方式实现



# 练习二 扩展练习：使用多线程编写一个简单的聊天室
1. 接收用户的网络连接可以使用socketserver库
2. 用户首次登陆输入自己的名字和当前在线的用户，支持多人同时登陆
3. 用户默认发的消息全部人可以收到，用户使用@某一用户可以进行私聊

提示： 服务端执行后会监听指定的端口， 客户端可以通过 nc <服务器ip地址>  <服务器端口> 方式连接， 如：
服务端执行 python server.py 后进行监听8000端口， 客户端执行 nc -v 127.0.0.1 8000 后可以连接到服务端
客户端A 发送消息给全体人员可以直接输入消息内容， 回车后，其他客户端可见，  客户端A发给客户端B私信可以使用
@客户端B的名字  聊天内容，只有客户端B能够看到聊天内容

```python
# coding=utf-8
#!/usr/bin/python

import socketserver
import threading
import socket
import time
import re

srvip = ('', 8000)

userg = {}

timefmt = "%H:%M:%S"

reg = re.compile(r'^@')

##
"""
override socketserver.TcpServer.__init__()
"""


class MyTCPServer(socketserver.TCPServer):
    socket_lev = socket.SOL_SOCKET
    socket_opt = socket.SO_REUSEADDR

    def __init__(
            self,
            server_address,
            RequestHandlerClass,
            bind_and_activate=True):
        socketserver.BaseServer.__init__(
            self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        self.socket.setsockopt(self.socket_lev, self.socket_opt, 1)
        if bind_and_activate:
            self.server_bind()
            self.server_activate()


##

class MyThreadingTCPServer(socketserver.ThreadingMixIn, MyTCPServer):
    pass


class MyTcpHandler(socketserver.StreamRequestHandler):

    def sendtimes(self):
        msgsendtime = time.strftime(timefmt, time.localtime())
        return msgsendtime

    def whoonline(self, name):
        self.usernames = ""
        for key in userg.keys():
            self.usernames = self.usernames + key.strip('\n') + " "
        self.sendmsg = "online: %s\n" % self.usernames
        self.name = name
        userg[self.name].send(self.sendmsg.encode(encoding="utf-8"))

    def newuserlogin(self, name):
        self.sendtime = self.sendtimes()
        self.name = name
        self.sendmsg = "[ %s %s login]\n" % (
            self.sendtime, self.name.strip('\n'))
        for key in userg.keys():
            if key == self.name:
                continue
            else:
                userg[key].send(self.sendmsg.encode(encoding="utf-8"))

    def userlogout(self, name):
        self.sendtime = self.sendtimes()
        self.name = name.strip('\n')
        self.sendmsg = "[%s %s logout]\n" % (self.sendtime, self.name)
        for key in userg.keys():
            userg[key].send(self.sendmsg.encode(encoding="utf-8"))

    def sendmsgs(self, msg, name):
        self.sendtime = self.sendtimes()
        self.sendmsg = "<public>[%s %s]: %s" % (
            name.strip('\n'), self.sendtime, msg)
        self.name = name

        for key in userg.keys():
            if key == self.name:
                continue
            else:
                userg[key].send(self.sendmsg.encode(encoding="utf-8"))

    def sendmsgtoone(self, msg, name):
        self.sendtime = self.sendtimes()
        self.toname = msg.split()[0][1:]
        msglen = len(msg.split()[0]) + 1
        self.tomsg = msg[msglen:]
        self.keyname = self.toname + "\n"
        if self.keyname not in userg:
            self.sendmsg = "ERROE [%s] user not online or not exist\n" % self.toname
            userg[name].send(self.sendmsg.encode(encoding="utf-8"))
        else:
            self.sendmsg = "<priv msg>[%s %s]: %s" % (
                self.name.strip('\n'), self.sendtime, self.tomsg)
            userg[self.keyname].send(self.sendmsg.encode(encoding="utf-8"))

    def handle(self):
        self.usernames = ""
        self.cur_thread = threading.current_thread()
        #        print "%s Staring..." % self.cur_thread.name
        #        print threading.active_count()
        print('-' * 10, 'Get new connection', '-' * 10)
        #        print self.request
        self.sendmsg = """
                ======================================
                |        Welcome to My Server        |
                |       Please Enter You Name:       |
                |                                    |
                ======================================\n"""
        self.wfile.write(self.sendmsg.encode(encoding="utf-8"))
        self.name = self.rfile.readline().decode()
        while not self.name.strip('\n').strip():
            self.wfile.write('Please Enter You Name\n')
            self.name = self.rfile.readline().decode()
        while True:
            if self.name not in userg:
                userg[self.name] = self.request
                self.sendmsg = "Hello %s" % self.name
                self.wfile.write(self.sendmsg.encode(encoding="utf-8"))
                self.newuserlogin(self.name)
                self.whoonline(self.name)
                break
            else:
                self.wfile.write('Please Enter A New Name:\n')
                self.name = self.rfile.readline().decode()
        while True:
            self.resvmsg = self.rfile.readline().decode()
            #            print "*" * 30
            #            print self.resvmsg
            if self.resvmsg.strip(
                    '\n') is None or self.resvmsg.strip('\n') == "":
                continue
            elif self.resvmsg.strip('\n') == "quit":
                del (userg[self.name])
                self.userlogout(self.name)
                break
            elif reg.search(self.resvmsg):
                self.sendmsgtoone(self.resvmsg, self.name)
            elif self.resvmsg.strip('\n') == "w" or self.resvmsg.strip('\n') == "W":
                self.whoonline(self.name)
            else:
                self.sendmsgs(self.resvmsg, self.name)

    def finish(self):
        if not self.wfile.closed:
            self.wfile.flush()
        self.wfile.close()
        self.rfile.close()


server = MyThreadingTCPServer(srvip, MyTcpHandler)
server.serve_forever()
```