import csv
import numpy as np
f=open('data/subwaytime.csv')
data=csv.reader(f)
next(data)
next(data)

timeran=21           #시간범위 : 24시 이후로는 지하철이 다니지 않으므로 허수로 취급

sub_in=[0]*timeran    
sub_out=[0]*timeran
maxtime_in=0
smaxtime=0
mintime_in=0
smintime=0
maxtime_out=0
mintime_out=0
sort_in=[0]*timeran
sort_out=[0]*timeran
sub=[0]*timeran
sub_sort=[0]*timeran

print("원하는 역을 고르고 창을 닫으십시오.")

from tkinter import*                       #서울 지하철 노선도 이미지
window=Tk()
window.title("서울 지하철 노선도")

photo=PhotoImage(file='data/img_subway.GIF')
label1=Label(window,image=photo)

label1.pack()

window.mainloop()


station=str(input("입지분석을 원하는 지하철역 이름을 검색하세요.('역'빼고 입력)"))

for row in data :                  #시간대별 승하차 인원
    row[4:]=map(int,row[4:])
    if station in row[3]:
        for i in range(len(sub_in)):
            sub_in[i]+=row[4+i*2]
            sub_out[i]+=row[5+i*2]
            sort_in[i]+=row[4+i*2]
            sort_out[i]+=row[5+i*2]

            
for i in range(len(sub_in)) :                # 시간대별 총 유동인구
    sub[i]=sub_in[i]+sub_out[i]
    sub_sort[i]=sort_in[i]+sort_out[i]



aver_in=np.mean(sub_in)
aver_out=np.mean(sub_out)
aver_sub=np.mean(sub)
std_in=np.std(sub_in)
std_out=np.std(sub_out)
std_sub=np.std(sub)

print("")
print("평균 승차 인원은 %.2f명입니다."%(aver_in))   #승하차인원의 평균
print("평균 하차 인원은 %.2f명입니다."%(aver_out))
print("평균 유동인구는 %.2f명입니다, "%(aver_sub))
print("승차, 하차, 유동인구의 표준편차는 %.2f, %.2f, %.2f입니다."%(std_in,std_out,std_sub))
print("(표준편차가 클수록 데이터의 퍼짐경향이 강합니다.)")
print("")
sort_in.sort()
sort_out.sort()
sub_sort.sort()


print("%s의 승하차인원 및 유동인구의 상위 5개 값은 다음과 같습니다."%(station))
print("승차인원 상위 5개 값 :",sort_in[len(sort_in):len(sort_in)-5:-1])
print("하차인원 상위 5개 값 :",sort_out[len(sort_out):len(sort_out)-5:-1])
print("유동인구 상위 5개 값 :",sub_sort[len(sub_sort):len(sub_sort)-5:-1])
print("")

min_in=sort_in[len(sort_in)-1]
min_out=sort_out[len(sort_out)-1]
max_in=sort_in[0]
max_out=sort_out[0]
max_sub=sub_sort[0]
min_sub=sub_sort[len(sub_sort)-1]



for i in range(len(sub_in)) :   #승차인원 최대 최소 시간대
    if max_in<sub_in[i] :
        max_in=sub_in[i]
        maxtime_in=i+4


    if min_in>sub_in[i] :
        min_in=sub_in[i]
        mintime_in=i+4


for i in range(len(sub_out)) :   #하차인원 최대 최소 시간대
    if max_out<sub_out[i] :
        max_out=sub_out[i]
        maxtime_out=i+4


    if min_out>sub_out[i] :
        min_out=sub_out[i]
        mintime_out=i+4


for i in range(len(sub)) :   #유동인구 최대 최소 시간대
    if max_sub<sub[i] :
        max_sub=sub[i]
        smaxtime=i+4

    if min_sub>sub[i] :
        min_sub=sub[i]
        smintime=i+4


print("%s에서 승차인원이 가장 많을 때는 %d시 %d명이고, 가장 적을 때는 %d시  %d명입니다,"%(station,maxtime_in,max_in,mintime_in,min_in))
print("%s에서 하차인원이 가장 많을 때는 %d시 %d명이고, 가장 적을 때는 %d시  %d명입니다,"%(station,maxtime_out,max_out,mintime_out,min_in))
print("%s에서 유동인구가 가장 많을 때는 %d시 %d명이고, 가장 적을 때는 %d시  %d명입니다,"%(station,smaxtime,max_sub,smintime,min_sub))


x=[0]*timeran
for i in range(len(sub)) :     #그래프의 x축 범위는 4시~24시
    x[i]=i+4


import matplotlib.pyplot as plt

plt.rc('font',family='Malgun Gothic')                 #승차/하차/유동인구 그래프
plt.style.use('ggplot')
plt.title("2020년 4월 %s 시간대별 승하차 인원 추이"%(station))
plt.plot(sub_in[0:],label='승차')
plt.plot(sub_out[0:],label='하차')
plt.plot(sub[0:],label='유동인구')
plt.xticks(range(len(x)),x)
plt.legend()
plt.show()











