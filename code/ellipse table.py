import matplotlib.pyplot as plt
import numpy as np
import math
class tabel:
    
    def __init__(self,x_0=0.2,y_0=0,vx_0=-0.2,vy_0=-0.5,dt_1=0.001,total_time=1000):
        self.x=[x_0]
        self.y=[y_0]
        self.vx=[vx_0]
        self.vy=[vy_0]
        self.dt=dt_1
        self.time=total_time
        self.t=[0]
    def calculate(self):
        for i in range(int(self.time/self.dt)):
            self.x.append(self.x[i]+self.vx[i]*self.dt)
            self.y.append(self.y[i]+self.vy[i]*self.dt)
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i])
            
            if ((self.x[i+1]**2/4+self.y[i+1]**2)>1):
                X=(self.x[i]+self.x[i+1])/2
                Y=(self.y[i]+self.y[i+1])/2
                x1=(X/2)/(X**2/4+Y**2)**0.5
                x2=Y/(X**2/4+Y**2)**0.5
                self.vx[i+1]=(1-2*x1**2)*self.vx[i]-2*x1*y1*self.vy[i]
                self.vy[i+1]=(1-2*y1**2)*self.vy[i]-2*x1*y1*self.vx[i]
                continue
            
            else:
                self.x[i]=X
                self.y[i]=Y
                continue
       
    def bound(self):
        x_1=[-1]
        y_1=[0]
        x_2=[-1]
        y_2=[0]
        dx=0.0001
        for k in range(20000):
            x_1.append(x_1[k]+dx)
            y_1.append((1-x_1[k+1]**2)**0.5)
            x_2.append(x_2[k]+dx)
            y_2.append(-(1-x_2[k+1]**2)**0.5)
    def show_results(self):
        plt.plot(self.x,self.y,'--',label='trajectory')
        plt.xlabel(u'x')
        plt.ylabel(u'y')
        
a=tabel()
a.calculate()
a.show_results()
