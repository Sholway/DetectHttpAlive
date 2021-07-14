import requests
import sys
import threading
import queue
import urllib3
#import os

# 使用方法  DetectHttpAlive.py url.txt 100
listName = sys.argv[1]
num = int(sys.argv[2])

quit = queue.Queue()
threadingNum = num

urlList = open(listName,'r')
lines = urlList.readlines()
urlList.close()

for line in lines:
    line = line.rstrip()
    quit.put(line)

def crawler():
    while not quit.empty():
        url = quit.get()
        try:
            urllib3.disable_warnings()#屏蔽一些https错误
            content = requests.get (url,verify =False,allow_redirects = True ,timeout =8)
            if content.status_code == 200:
                with open('aliveHttp.txt','a') as f:
                    f.write(url + '\n')
                    print(url)
        except requests.RequestException as e:
            pass

if __name__ == '__main__':
    for i in range(threadingNum):
        t = threading.Thread(target=crawler())
        t.start()

    print ("All tasks done !")