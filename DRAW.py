# -*- coding=utf-8 -*-

import random
import matplotlib.pyplot as plt
from pylab import mpl



def Draw_SIG():

    plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
    #设置图信息
    fig=plt.figure()
    fig.suptitle('信号灯配时图', fontsize=10)
    ax=plt.Axes(fig,[0.05, 0.03,0.9,0.9])

    dict_locate_phase={'phase_4':0.25,'phase_3':0.5,'phase_2':0.75,'phase_1':1}
    ax.set_yticks([dict_locate_phase['phase_4'],dict_locate_phase['phase_3'],dict_locate_phase['phase_2'],dict_locate_phase['phase_1']])#修正后

    ax.set_yticklabels(['第4相位','第3相位','第2相位','第1相位'])



    phase_1={'red':5,'amber':3,'green':5,'allred':2}
    phase_2={'red':5,'amber':3,'green':5,'allred':2}
    phase_3={'red':5,'amber':3,'green':5,'allred':2}
    phase_4={'red':5,'amber':3,'green':5,'allred':2}
    
    cycle_time=0
    list_phase=[phase_1,phase_2,phase_3,phase_4]
    phase_1=list_phase[0]
    phase_2=list_phase[1]
    phase_3=list_phase[2]
    phase_4=list_phase[3]

    for phase in list_phase:
        
       cycle_time += phase['red']+phase['amber']+phase['green']+phase['allred']
       
    for phase in list_phase:
        phase['red']    /= cycle_time 
        phase['amber']  /= cycle_time 
        phase['green']  /= cycle_time 
        phase['allred'] /= cycle_time 
        #phase['red']   = round( phase['red'] ,2)
        #phase['amber'] = round( phase['amber'] ,2)
        #phase['green'] = round( phase['green'] ,2)
        #phase['allred']=round( phase['allred'] ,2)
    print(list_phase)
   
    phase_start_1={'red':phase_1['green']+phase_1['amber']+phase_1['allred'],'amber':phase_1['green'],'green':0,'allred':phase_1['green']+phase_1['amber']}
    phase_start_2={'red':phase_start_1['red']+phase_2['green']+phase_2['amber']+phase_2['allred'],'amber':phase_start_1['red']+phase_2['green'],'green':phase_start_1['red'],'allred':phase_start_1['red']+phase_2['green']+phase_2['amber']}
    phase_start_3={'red':phase_start_2['red']+phase_3['green']+phase_3['amber']+phase_3['allred'],'amber':phase_start_2['red']+phase_2['green'],'green':phase_start_2['red'],'allred':phase_start_2['red']+phase_3['green']+phase_3['amber']}
    phase_start_4={'red':phase_start_3['red']+phase_4['green']+phase_4['amber']+phase_4['allred'],'amber':phase_start_3['red']+phase_4['green'],'green':phase_start_3['red'],'allred':phase_start_3['red']+phase_4['green']+phase_4['amber']}


    phase_1_x_green=[phase_start_1['green'], phase_start_1['green']+phase_1['green'] ]
    phase_1_x_amber=[phase_start_1['amber'],phase_start_1['amber']+ phase_1['amber'] ]
    phase_1_x_allred=[phase_start_1['allred'],phase_start_1['allred']+ phase_1['allred'] ]
    phase_1_x_red=[phase_start_1['red'] , phase_start_1['red']+ phase_1['red'] ]
    phase_1_y=[dict_locate_phase['phase_1'],dict_locate_phase['phase_1']]

    phase_2_x_green=[phase_start_2['green'],phase_start_2['green']+ phase_2['green'] ]
    phase_2_x_amber=[phase_start_2['amber'],phase_start_2['amber']+ phase_2['amber'] ]
    phase_2_x_allred=[phase_start_2['allred'], phase_start_2['allred']+ phase_2['allred'] ]
    phase_2_x_red=[phase_start_2['red'] , phase_start_2['red'] + phase_2['red'] ]
    phase_2_y=[dict_locate_phase['phase_2'],dict_locate_phase['phase_2']]

    phase_3_x_green=[phase_start_3['green'], phase_start_3['green']+phase_3['green'] ]
    phase_3_x_amber=[phase_start_3['amber'], phase_start_3['amber']+phase_3['amber'] ]
    phase_3_x_allred=[phase_start_3['allred'],phase_start_3['allred']+phase_3['allred'] ]
    phase_3_x_red=[phase_start_3['red'] ,phase_start_3['red'] +phase_3['red'] ]
    phase_3_y=[dict_locate_phase['phase_3'],dict_locate_phase['phase_3']]

    phase_4_x_green=[phase_start_4['green'],phase_start_4['green']+ phase_4['green'] ]
    phase_4_x_amber=[phase_start_4['amber'],phase_start_4['amber']+ phase_4['amber'] ]
    phase_4_x_allred=[phase_start_4['allred'], phase_start_4['allred']+phase_4['allred'] ]
    phase_4_x_red=[phase_start_4['red'] ,phase_start_4['red']+phase_4['red'] ]
    phase_4_y=[dict_locate_phase['phase_4'],dict_locate_phase['phase_4']]


  
    ax.plot(phase_1_x_green,phase_1_y,linewidth=9,linestyle='-',color='green')
    ax.plot(phase_1_x_amber,phase_1_y,linewidth=9,linestyle='-',color='yellow')
    ax.plot(phase_1_x_allred,phase_1_y,linewidth=9,linestyle='-',color='red')
    ax.plot(phase_1_x_red,phase_1_y,linewidth=9,linestyle='-',color='red')
      
    ax.plot(phase_2_x_green,phase_2_y,linewidth=9,linestyle='-',color='green')
    ax.plot(phase_2_x_amber,phase_2_y,linewidth=9,linestyle='-',color='yellow')
    ax.plot(phase_2_x_allred,phase_2_y,linewidth=9,linestyle='-',color='red')
    ax.plot(phase_2_x_red,phase_2_y,linewidth=9,linestyle='-',color='red')
      
    ax.plot(phase_3_x_green,phase_3_y,linewidth=9,linestyle='-',color='green')
    ax.plot(phase_3_x_amber,phase_3_y,linewidth=9,linestyle='-',color='yellow')
    ax.plot(phase_3_x_allred,phase_3_y,linewidth=9,linestyle='-',color='red')
    ax.plot(phase_3_x_red,phase_3_y,linewidth=9,linestyle='-',color='red')
      
    ax.plot(phase_4_x_green,phase_4_y,linewidth=9,linestyle='-',color='green')
    ax.plot(phase_4_x_amber,phase_4_y,linewidth=9,linestyle='-',color='yellow')
    ax.plot(phase_4_x_allred,phase_4_y,linewidth=9,linestyle='-',color='red')
    ax.plot(phase_4_x_red,phase_4_y,linewidth=9,linestyle='-',color='red')

    fig.add_axes(ax)
    plt.show()

if __name__=="__main__":
    Draw_SIG()




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
