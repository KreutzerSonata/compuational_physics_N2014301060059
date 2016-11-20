#Cannon Shell Trajectory  

##Abstract  

In this task, Euler method is applied to solve a second-order ODE involving two variables which represents motion in two spatial dimensions.
A simple example is the projectile motion problem, namely the trajectory of a cannon shell. For a realistic approximation, air resistance and
altitude effect are engaged, both adiabatic and isothermal models for altitude effect are applied, and with schema it's convenient to
see the difference.  

##Background  

For a two-spatial-dimension projetile problem, Newton's equation is written in form of second-order ODE with two variables.  
![f=ma](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/f%3Dma.jpg)  
Now apply it in various situations:  

1.With no air drag, it degenerated to a free falling body problem.  
![no air drag](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/no%20air%20drag.jpg)  

2.Supppose the air drag comes from the impulse when object pushes the air in front of it out of the way, the drag force is propotional
to the velocity's square.  
![f=kv^2](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/f%3Dkv%5E2.jpg)  
in which B is related to the density of air.  

3.Consider the altitude effect, air density vary as a function of the altitude, use isothermal ideal gas to make an approximation.  
![isothermal](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/isothermal.jpg)  

4.Alter the model for adiabatic ideal gas.  
![adiabatic](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/adiabatic.jpg)  

We will soon see the different effects between the two models.  

##Mainbody  

In order to reduce higher-order ODE to finite difference equations conveniently, write each second-order equations as two first-order
differential equations. First consider no air drag effect.  

![first order](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/first%20order.jpg)  

Now use the Euler method to derive finite difference form.  

![d](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/f%3Dma2.jpg)  

Similarily we can add air resistance to the difference form.  
![air drag](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/f%3Dkv%5E22.jpg)  

In this way it's convenient to run a program to plot the result. Set the initial values as follows and we can see the effect of air resistance.  

Initial veloctiy -> 700  
Initial angle of velocity -> π/4 = 0.785  
Initial location of cannon shell -> (0, 0)  
time step -> 0.01  
B over m =0.00001 /m  

[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/air%20drag%20effect.py)  
![air drag](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/air%20drag%20effect.png)  
Though the B factor is quite small, it makes a substantial effect in both range and height.  

Next we take the altitude effect into consideration, rewrite the previous equations in finite difference form.  
![iso](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/iso.jpg)  
This is for isothermal model  

![adia](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/adia.jpg)  
And this is for adiabatic model  

Set the initial values as follows and we can compare the results.  

Initial veloctiy -> 700  
Initial angle of velocity -> π/4 = 0.785  
Initial location of cannon shell -> (0, 0)  
time step -> 0.01  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/altitude%20effect.py)  
![alt](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/altitude%20effect.png)  

Furthermore we take varying temperature into consideration, which shift B by a factor ![f](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/factor.jpg) , in this case we take α = 2.5, with the same initual values we have result as follows  

[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/varying%20temperature.py)  
![vary](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/varying%20temperature.png)  

##Conclusion  

Air resistance makes a substantial effect for a cannon shell's trajectory. The result of the two models for altitude differ from each other a bit, and the isothermal model gives a better value in both range and height. However, the adiabatic model may be closer to realistic situation for we know temperature varies as altitude changes. Also it varies with seasons, it seems that in winter a cannon shell should have a better flight.  

##Acknowledgement and Reference  

参考了贺一珺同学和上官俊怡学长的程序。我再想想怎么能把公式的字体缩小一点，现在这样太不美观了╮(╯ _ ╰)╭



