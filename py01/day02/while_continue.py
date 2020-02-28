#!/usr/local/bin/python3
#计算100以内偶数之和
result=0
i=0

while i<100:
   i+=1
   if i%2: #i%2结果只能是1或0，1为真，0为假
       continue
   else:
       result+=i

print(result)