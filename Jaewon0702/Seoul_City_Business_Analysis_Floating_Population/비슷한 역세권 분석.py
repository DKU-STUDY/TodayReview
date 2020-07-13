import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font',family='Malgun Gothic')

df=pd.read_csv('data/subwaytime.csv',encoding='cp949')

df2=df['역이름']                                        

del df['A'],df['B']        #원활한 계산을 위해 문자 제거
del df['C'],df['역이름']

df['Floating Population']=np.sum(df,axis=1)          #유동인구 총합 열 추가
df=df[df['Floating Population']>0]

df=df.div(df['Floating Population'],axis=0)          #각 행을 유동인구로 나눈다.

del df['Floating Population']

df.index=df2                                    #역 이름을 index로 지정

print("원하는 지하철역을 고르고 창을 닫으십시오.")
from tkinter import*                       #서울 지하철 노선도 이미지
window=Tk()
window.title("서울 지하철 노선도")

photo=PhotoImage(file='data/img_subway.GIF')
label1=Label(window,image=photo)
label1.pack()
window.mainloop()

station=input("원하는 지하철역을 입력하세요('역' 빼고 입력):")
a=df.index.str.contains(station)
df3=df[a]                                    # 다른 지하철역의 인구와 원하는 지하철 역의 인구를 빼고 제곱

x=df.sub(df3.iloc[0],axis=1)

timeran=48
xran=['']*timeran


y=np.power(x,2)
z=y.sum(axis=1)

i=z.sort_values().index[:5]                        #유사한 유동인구를 가진 역 5개 추출
df.loc[i].T.plot()
plt.xticks(range(len(xran)),xran)
plt.title("%s역과 유사한 유동인구를 가진 지하철역 5개"%(station))
plt.show()
