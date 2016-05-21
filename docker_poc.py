#coding:utf-8
from Queue import Queue
from netaddr import  IPNetwork
import threading
import requests
import sys
global queue
def docker_poc(ip):
    try:
        url="http://"+str(ip)+":2375"
        httpget=requests.get(url+"/version",timeout=2)
        if httpget.status_code!=200:
            pass
        else:
            if 'ApiVersion' in httpget.content:
                print url + '\n'
    except:
        pass
class MultiThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while not queue.empty():
            ip = queue.get()
            docker_poc(ip)
def ips(str1):
    print "[*]Start run Docker_poc..."
    for ip in IPNetwork(str1):
        queue.put(ip)
        for i in range(100):
            c = MultiThread()
            c.start()
if __name__ == "__main__":
    queue=Queue()
    ip=sys.argv[1:]
    args="".join(ip)
    ips(args)
