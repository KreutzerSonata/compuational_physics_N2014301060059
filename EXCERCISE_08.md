#Routes to Chaos: Period Doubling  

Homework 3.20  

##Abstract  

In this task we seek a method to describe how chaos takes place in a pendulum system, bifurcation diagram is introduced to show the
transition from periodic to chaotic behaviour. And from bifurcation diagram we can get a feature parameter δ to estimate 
the shrinkage rate of the transition.  

##Background  

Bifurcation diagram takes θ as a function of drive amplitude, for each drive amplitude θ is plotted at times that are in phase with 
the driving force, this process was then reapted for the range of values of drive amplitude concerned.  


##Mainbody  

![](https://camo.githubusercontent.com/7bfbcc3e2494c8b5036741ecece5da147795e145/68747470733a2f2f7777772e657665726e6f74652e636f6d2f73686172642f733134302f73682f30373234383135622d373961392d343335372d396538352d3431366333336362316236392f65326230363637343436653666376437343138313936396564306337633335372f7265732f37636164646638352d663436302d343932652d396630362d6565616464666335613634392f386137656337363631636266613531652e706e67)  
When driving force increases beyound a specific value, the period for pendulum doubles, this process keeps until period no longer 
makes sense, that is where chaos takes place. We describe this process by bifurcation diagram starting with drive amplitude F=1.35, 
some constants are as follows  
  q = 0.5  
  l = 9.8  
  g = 9.8  
  f = 2/3    
  theta0 = 0.2  
  omega0 = 0  
    
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/bifurcation.py)    
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/bifurcation.png)  
    
We note that the spacing between period-doubling transitions becomes rapidly smaller as the order of the transition increases. Let 
us define Fn to be the value of the driving force at which the transition takes place, then the shrinkage of the size of the period
windows can be described by a parameter δn, where  
![](https://camo.githubusercontent.com/f9645cfc988ae6970d3a53296d6eec6defb025e1/68747470733a2f2f7777772e657665726e6f74652e636f6d2f73686172642f733134302f73682f30373234383135622d373961392d343335372d396538352d3431366333336362316236392f65326230363637343436653666376437343138313936396564306337633335372f7265732f37643831623533322d366261622d346235612d393539302d6635386461343135613136392f5f5f5356475f5f6264613336353434363537636133373631343738633233636231383366353831)    
This is known as Feigenbaum δ. To estimate the value, we magnify the diagram in the vicinty of transition.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/bifurcation1.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/bifurcation2.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/bifurcation3.png)  
Keep magnifying the points where transition takes place, and we get accurate pictures about the transition, like this  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/bifurcation4.png)  
Now it's convenient to tell the corresponding Fd as 1.419693, 1.454545, 1.471212, and the δ is around 2.091.  

##Conclusion  

Obviously δ>1, that means the windows becomes smaller as n increases. And it has been found that sa n become large enough, δ
approaches a constant known as Feigenbaum δ, which is around 4.669... and this is one of the universal parameters associated 
wih the transition to chaos no matter what system it is concerned.  

##Acknowledgment and Reference  

程序参考吴雨桥学长，第一幅插图来自教材~

