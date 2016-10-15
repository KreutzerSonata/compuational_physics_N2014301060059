#Decay Simulation

##Abstract

In this task, Euler method is used for solving the equaions set of a decay problem with two types of nuclei. Python gives the schema 
from which we can see the deviation from the accurate result. 

##Background

Ordinary differential equations are used for depicting decay processes. A numerical approach to solving these equations is known as 
*Euler method*, which takes the Taylor expansion of the variable and drops the higher order terms to do the approximation. To simulate 
it, four steps are required in programming: 1)Declare necessary variables and arrays. 2)Initialize variables. 3)Do the actual calculation.
4)Store(or show)the results.

##Mainbody

>Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while
nuclei of type B decay into ones of type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to 
turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states 
A and B which have equal energies. The corresponding rate equations are
![eq1](https://camo.githubusercontent.com/0289cbd721c15bc0a9e8a413b749fcbf4cfc9692/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f5c667261637b644e5f417d7b64747d3d5c667261637b4e5f427d7b5c7461755f427d2d5c667261637b4e5f417d7b5c7461755f417d)  
![eq2](https://camo.githubusercontent.com/f18ae9efd10a980fa9b0c19059007cdb0206401c/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f5c667261637b644e5f427d7b64747d3d5c667261637b4e5f417d7b5c7461755f417d2d5c667261637b4e5f427d7b5c7461755f427d
)  
where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equation for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc, and take tau=1s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.

Firstly create a class representing nuclei A and B, then set the initial values as follows:

Initial number of nucleiA -> 100  
Initial number of nucleiB -> 0  
Time constant -> 1  
Time step -> 0.05  
Total time -> 5  

Then define a function to do the calculation using Euler method, and a function to show the result in pylab.  

[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/decay%20code1.py)

Run this program and we get a schema.
![result1](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/decay_1.png)  

Change the initial values to 60 for nucleiA and 40 for nucleiB and we get a similar result.  

![result2](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/decay_2.png)  


Analyticaly solving the given equations set is quite easy, the solution is  

![result3](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/result3.jpg)  

Suppose NA(0)=100, NB(0)=0, then we can plot this analytical result with the numerical result in the same schema, wthin an acceptable
inaccurracy they agree with each other quite well.
![result4](https://raw.githubusercontent.com/JiajiaLuo/computational_physics_N2014301510065/master/ex4%208.PNG)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/decay%20code2.py)  

##Conclusion

The system of two types of nuclei reaches a steady state in which NA=NB=constant. The approximation of Euler method is acceptable, 
a more accuracy result could be attained by reducing the time step constant.

##Acknowledge and Reference

参考了课本第一章和蔡老师的讲义，程序部分以吴帆帆同学的为蓝本，并参照江俊、罗佳佳同学进行修正。





