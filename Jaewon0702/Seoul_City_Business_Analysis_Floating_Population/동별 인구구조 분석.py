import csv
f=open('data/age.csv')
data=csv.reader(f)

maxage=0
minage=0
result=[]
max1=0
min1=101

local=str(input("인구분석을 원하는 동네를 입력하세요('동' 단위, 예 청담동) : "))

for row in data :               #동별 인구
    if local in row[0] :
        for i in row[3:] :
            result.append(int(i))

print(result)



for i in range(len(result)) :     #인구가 가장 많은 나이
    if max1<result[i]:
        max1=result[i]
        maxage=i
    if min1>result[i] :  #인구가 가장 적은 나이
        min1=result[i]
        minage=i
         
print("%s은(는) %d세가 %d명으로 가장 많습니다."%(local,maxage,max1))
print("%s은(는) %d세가 %d명으로 가장 적습니다."%(local,minage,min1))  


import matplotlib.pyplot as plt

plt.rc('font',family='Malgun Gothic')
plt.title('%s 인구구조'%(local))
plt.style.use('ggplot')  #격자구조
plt.plot(result)
plt.show()
