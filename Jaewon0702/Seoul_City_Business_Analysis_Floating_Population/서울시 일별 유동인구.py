import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('data/Floating_Population.csv')

del df['연령대'], df['시간'], df['성별'], df['시']  # 필요없는 열은 삭제

df.index=df['군구']       #지역(군구) 열을index로 지정
del df['군구']

print("원하는 지역을 고르고 창을 닫으십시오.")
from tkinter import*                       #서울 지도 출력
window=Tk()
window.title("서울 지도")

photo=PhotoImage(file='data/seoul_map.GIF')
label1=Label(window,image=photo)
label1.pack()
window.mainloop()

local=input("유동인구 분석을 원하는 지역을 입력하세요.('구'포함해서 입력, 예 : 강남구) : ") # 원하는 지역의 시간대별 유동인구 데이터만 추출
a=df.index.str.contains(local)
df2=df[a]
df2.index=df2['일자']

del df2['일자']

df2=df2.sort_values(by=['일자'])

df3=df2.T

date_ran=20200431    #4월 1일~4월 30일까지 분석
month=4    #4월 데이터를 분석
year=2020   #2020년의 데이터를 분석

for i in range(20200401,date_ran,1) :       # 일별 유동인구의 합
    df3['%d월 %d일'%(month,i-20200400)]=np.sum((df3[i]),axis=1)
    del df3[i]

df3['mean']=np.mean(df3,axis=1)                 #입력받은 지역 유동인구의 평균과 표준편차
df3['std']=np.std(df3,axis=1)
print("%s 유동인구의 평균은 %.2f명 입니다."%(local,float(df3['mean'])))
print("%s 유동인구의 표준편차는 %.2f 입니다."%(local,float(df3['std'])))

del df3['mean'], df3['std']

df4=df3.T

df4['유동인구수']=df4['유동인구수'].apply(pd.to_numeric)

plt.rc('font',family='Malgun Gothic')
df4.plot()
plt.title("%d년 %s의 일별  유동인구"%(2020,local,))
plt.show()



