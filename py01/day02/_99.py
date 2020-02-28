#!/user/local/bin/pythons
#输出:
#1*1=1
#1*2=2 2*2=4
#1*3=3 2*3=6 3*3=9
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(j,i,i*j),end='\t')
    print()