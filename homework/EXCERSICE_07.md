#Chaos in the Driven Nonlinear Pendulum  
Homework 3.13

##Abstract  

In this task we discuss about chaotic phenomena through an example of pendulum. Pendulum oscillation is treated as simple harmonic
motion under the condition that the initial drift angle is small enough to allow the approximation sinx≈x, otherwise the nonlinear
term sinx would cause a much different result, namely chaos. For a more realistic simulation, dissipation and a external driving force
are also put into cosidereation, such model is called the physical pendulum. To make a simulation of this, Euler-Cromer method
is applied, and the reslts reveal the significant feature of chao —— sensitivity to initial value.  

##Background  

 - **Euler-Cromer method**  
 
An oscillation involving damping and driving force is described as follow  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7D%5Ctheta%20%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta%20-q%5Cfrac%7Bd%5Ctheta%20%7D%7Bdt%7D&plus;F_%7BD%7Dsin%28%5COmega_%7BD%7Dt%29)  
In which q represents the damping factor and F the amplitude of driving force and Ω the angular frequency. Euler method fails to
predict its behavior so it's substitued by Euler-Cromer method, which inherits the idea of deriving finite difference form from the differential
equations but leaves a small change. Rewrite this second-order equatin in form of two first-order ones using dθ/dt= ω , then apply
Euler-Cromer method  
  ![](http://latex.codecogs.com/gif.latex?%5Comega%20_%7Bi&plus;1%7D%3D%5Comega%20_%7Bi%7D-%5B%28g/l%29sin%5Ctheta%20_%7Bi%7D-q%5Comega%20_%7Bi%7D&plus;F_%7BD%7Dsin%28%5COmega_%7BD%7Dt%29%5D%5CDelta%20t)  
  ![](http://latex.codecogs.com/gif.latex?%5Ctheta%20_%7Bi&plus;1%7D%3D%5Ctheta%20_%7Bi%7D&plus;%5Comega%20_%7Bi&plus;1%7D%5CDelta%20t)  
Notice that the previous values of ω and θ are used to calculate the new value of ω, but the new value of ω is used to calculate the 
new value of θ.   

For a physical pendulum, just replace -(g/l)θ term by -(g/l)sinθ ,and Euler-Cromer method performs as well as previous.  


- **Poincare section** 

In the phase-space graph, plot ω versus v only at times that are in phase with the driving force. That is, only the points with Ωt=2nπ are displayed where n is an integer.
Ihis is known as Poincare section. And it is a very useful way to plot and analyze the behavior of a dynamical system.  

#Mainbody  

Now consider a physical pendulum's behaviors under different driving force, with the following constants and initial values, 
results are displayed.  
q = 0.5  
l = 9.8  
Ω = 2/3  
g = 9.8  
theta0 = 0.2  
omega0 = 0    
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/pendulum.png)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/commit/aca90706f5b189b99c51cee0b95f579b0c17be52)  
When no driving force is applied, the pendulum comes to rest after a few oscillations. With a small driving force F=0.5
the pendulum yields to the external frequency after an initial transient, which also happens in a simple harmonic motion. However, once the force is increased to 1.2, the pendulum starts to lose control, period vanished, the motion seems to be irregular and unpredictable, this is a chaotic phenomenon.  

To gain a deeper understanding of this strange feature, give two identical pendulums the same initial values but a slightly
difference between initial angles, namely 0.001rad, for a non-chaotic situation (F=0.5), we have the result  
![d](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/c6f45ea7be45329af8b17593eaae0326a42eea27/pendulum2.png)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/pendulums.py)  
The difference between angles vanished as time goes, which agrees with our inituition that small error would be erased by time and result converges to a determined value. However for chaotic situation(F=1.2) the result reverse  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/d620f9ef2dfcb2a8b84da67f1501325333e3130b/pendulum2%20(1).png)    
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/pendulums2.py)  
The error increases as time goes, the two pendulums can't cath each other any longer. So slight difference leads to tremendous divergence, this is the sensibility of chaotic system.  

Notice that the vertical axis has a logarithmic scale, though the trendecy of the curve seems to be linear with time, actually it changes exponentially, ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta%20%5Capprox%20e%5E%7B%5Clambda%20t%7D) this is called Lyapnov exponent. From the first schema we can estimate λ≈-0.158, it's a negative constant for non-chaotic system. As for the second schema, the value of λ is not so easy to tell, but it's clearly a positive constant.  

##Conclusion  

![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/4b631e83ta46b5278f2b3%26690.jpg)  
The chaotic phenomena means more than astonihing, it remedies our cognition to the world. Physicists In past expressed their cognition to the world by a allegory of a supernatural creature *The Demon of Laplace* , who measures the position and velocity of every single object at a very moment, then he can calculate how everything runs in the past and in the future through classic mechanic method, so the world is determined. This sound reasonabele but a bit odd, now we know the reason. Practicall The demon has to record the information of every object in a finite form, it can't be infinite precise. And once there is a slight inaccuracy in the initial values, chaos plays a significant role, and the demon's calculation deviates more and more from the actual motion as time goes. In this way we say the world is *determined* but *unpredictable*.  

##Acknowledgment and Reference  

程序参考了吴雨桥学长，部分内容参考教材和Wiki词条[Laplace's demon](https://en.wikipedia.org/wiki/Laplace%27s_demon)



