#!/usr/local/bin/python3
#计算1加到100的结果
#bash实现
# echo 'seq 100 |tr '\n' '+' |sed 's/\+$/\n/' |bc
#5050

#创建变量用于保存最终结果
result=0
#创建计数器
i=1

# result+=i #result=result+i -> result=0+1 -> result=1
# i+=1      #i=1+1 -> i=2
#
# result+=i #result=result+i -> result=1+2 -> result=3
# i+=1      #i=2+1 -> i=3
#......

#循环累加
while i<=100:
    result+=i
    i+=1
print(result)