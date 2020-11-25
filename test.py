#二阶段

allred=2 #全红时间 
n=2  #相位数
l=5.2 #相位损失时间
S=1800  #单车道饱和流量

#北东南西 流量
Q1=750
Q2=450

print(f" 第三个路口 流量：\n北南：{Q1} \n东西：{Q2}\n\n")

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

C0=round(C0)

#显示时间
amber=4   #黄灯
G1=round(ge1 -amber+l)
G2=round(ge2 -amber+l)



print(f"第三个路口  绿灯显示时间：\n北南：{G1}\n东西：{G2}\n周期：{C0}\n")