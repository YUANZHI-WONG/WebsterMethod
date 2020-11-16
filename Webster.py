#%%
#四阶段

allred=2 #全红时间
n=4  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

#北东南西 流量
Q1=230
Q2=99
Q3=150
Q4=210


print(f" zjb平峰流量：\n北：{Q1} \n东：{Q2}\n南：{Q3}\n西：{Q4}\n")

#Lost time
L=n *( l + allred)
#流量比
Y1=Q1/S
Y2=Q2/S
Y3=Q3/S
Y4=Q4/S

Y=Y1+Y2+Y3+Y4

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

print(f"zjb平峰时间：\n北：{G1}\n东：{G2}\n南：{G3}\n西：{G4}")

#%%
allred=2 #全红时间
n=2  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

#北东南西 流量
Q1=600
Q2=400

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


print(f"高峰：\n北南：{G1}\n东西：{G2} ")

#%%


allred=2 #全红时间
n=2  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

#北东南西 流量
Q1=900
Q2=600
print(f" 找物件早高峰流量：\n北南：{Q1} \n东西：{Q2}  \n")
#print(f" 刘程平峰流量：\n北南：{Q1} \n东西：{Q2}  \n")
#print(f" 刘程夜间流量：\n北南：{Q1} \n东西：{Q2}  \n")
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


print(f" 找物件早高峰时间：\n北南：{G1} \n东西：{G2}  ")
#print(f" 刘程平峰时间：\n北南：{G1} \n东西：{G2}  ")
#print(f" 刘程夜间时间：\n北南：{G1} \n东西：{G2}  ")

# %%
