#!/usr/local/bin/python3
import time

def timejia():

    result=0
    start=time.time()
    for i in range(1,10000001):
        result+=i
    end=time.time()
    print(end-start)
    print(result)

if __name__ == '__main__':
    timejia()
