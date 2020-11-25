#%%
#三阶段

allred=2 #全红时间 
n=3  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

#北东南西 流量
Q1=250
Q2=140
Q3=190



print(f" zjb 平峰流量：\n北南：{Q1} \n南北左转：{Q2}\n东西：{Q3}\n\n")

#Lost time
L=n *( l + allred)
#流量比
Y1=Q1/S
Y2=Q2/S
Y3=Q3/S



Y=Y1+Y2+Y3

C0=(1.5*L+5)/(1-Y)

#有效绿灯时间
Ge=C0-L
ge1=Ge *Y1 /Y
ge2=Ge *Y2 /Y
ge3=Ge *Y3 /Y


#显示时间
amber=4   #黄灯
G1=round(ge1 -amber+l)
G2=round(ge2 -amber+l)
G3=round(ge3 -amber+l)


print(f"zjb 平峰时间：\n北南：{G1}\n南北左转：{G2}\n东西：{G3}\n")

# %%
#%%
#四阶段

allred=2 #全红时间 
n=3  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

Q1=300  #北进口道流量
Q2=340  #东进口道流量
Q3=250  #南进口道流量
Q4=210  #西进口道流量

#损失时间
L=n *( l + allred)

#流量比
Y1=Q1/S
Y2=Q2/S
Y3=Q3/S
Y4=Q4/S
Y=Y1+Y2+Y3+Y4

#周期时长
C0=(1.5*L+5)/(1-Y)

#有效绿灯时间
Ge=C0-L
ge1=Ge *Y1 /Y
ge2=Ge *Y2 /Y
ge3=Ge *Y3 /Y
ge4=Ge *Y4 /Y


#显示时间
amber=4   #黄灯
G1=round(ge1 -amber+l)
G2=round(ge2 -amber+l)
G3=round(ge3 -amber+l)
G4=round(ge4 -amber+l)



#%%
#二阶段

allred=2 #全红时间 
n=2  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

#北东南西 流量
Q1=250
Q2=140

print(f" 第一个路口 流量：\n北南：{Q1} \n东西：{Q2}\n\n")

#Lost time
L=n *( l + allred)
#流量比
Y1=Q1/S
Y2=Q2/S

Y=Y1+Y2

C0=(1.5*L+5)/(1-Y)

#有效绿灯时间
Ge=C0-L
ge1=Ge *Y1 /Y
ge2=Ge *Y2 /Y



#显示时间
amber=4   #黄灯
G1=round(ge1 -amber+l)
G2=round(ge2 -amber+l)



print(f"第一个路口  绿灯显示时间：\n北南：{G1}\n东西：{G2}\n")
# %%
