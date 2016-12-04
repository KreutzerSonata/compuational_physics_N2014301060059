#Effect of Jupiter  

Homework 4.16 ＆ 4.17  

##Abstract  

Jupiter is the biggest planet in solar system, its great mass exerts effect on eatrth's orbit and the distribution of asteroids, the 
former one involves a three-body motion of Jupiter, Earth and the Sun, the latter one accounts for so-called Kirkwood Gap. And these 
are simulated in this task.  

##Background  

In a three-body problem, each object interacts with the other two through the inverse-square law, for Earth, its motion under the force 
of Jupiter and the Sun is ruled by   
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/force.jpg)  
Equations for Jupiter and the Sun is likewise. Decompose these vector equations to first-order ones with x and y components, then we
can use Euler-Cromer method to do the simulation.  

A Kirkwood gap is a gap or dip in the distribution of the semi-major axes (or equivalently of the orbital periods) of the orbits of main-belt asteroids. They correspond to the locations of orbital resonances with Jupiter.
 The weaker resonances lead only to a depletion of asteroids, while spikes in the histogram are often due to the presence of a prominent asteroid family.  
![](https://upload.wikimedia.org/wikipedia/commons/d/d3/Kirkwood_Gaps.svg)  

##Mainbody  

Before we do the task, we have a hunch that the Jupiter's effect on Earth is quite small, since both of their orbits is in stable existence
for billions of years. To make the result more appreciable, we virtually magnify the mass of Jupiter step by step, and observe the
effect.  

If the Sun's position is fixed at the origin, 1000 times of Jupiter's mass would produce a result like  
![](https://raw.githubusercontent.com/JunyiShangguan/computationalphysics_N2013301020076/master/ex12/figure_5.png)  
Earth is ejected out of the system while Jupiter's orbit is stable. Yet we would like to simulate a more realistic motion, move the 
constrain of the Sun and choose the system's mass center as origin so the three objects perform a real three-body motion.  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/three-body.py)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/三体1.png)  
Even so the effect of Jupiter on Earth and the Sun is too small to notice. Then increase Jupiter's mass ten times  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/三体2.1.png)  
The Sun starts to roll around the mass center, it seems more clear using a 3D plot.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/三体2.2.png)  
Next is 100 times of Jupiter's mass, the effect is more visible.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/三体3.1.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/三体3.2.png)  
1000 times of Jupiter's mass is very close to the Sun's, they tends to form a binary system while Earth is trying to rotate around the
Sun but actaully its motion is chaotic.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/three-body%20trajectory.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/three-body%20trajectory%203D.png)   

Next we check the effect of Jupiter on the asteroids in the 2/1 gap, which means the asteroids there would complete two orbits every
time Jupiter completes one, this is called the resonance of the planets.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/t%3D40.png)  
As we can see, the upper and lower part of the asteroids' orbit is thicker than other part, these are the two positions where the
asteroids find its closet approach to Jupiter, so after every period the perturbations due to Jupiter accumulat, this will be clear
if we observe for a longer time  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/t%3D120.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/t%3D120%203D.png)  
From the latter schema we see the asteroids' orbit leans at an angle with the time axis, which implies it's moving as time goes, finally
the asteroids will no more stay in the Gap. Similiar phenonmenon happens at other places where the asteroids' periods are 1/3, 2/5, 
3/7 of Jupiter's.  

##Conclusion  

Three-body problem is a good example to real the power of numerical simulation, for there are actually very few exact analytic results
in this case. As for the resonance of planets, this reminds me of the ancient Greek tradition treating celestial mechanics as a
kind of knowledge related close to music, or harmonics of the stars.  

##ACknowledgment and Reference  
第一张轨迹图是直接从上官俊怡学长那儿移过来的，程序参考郭潇学长，并进行一小点debug。部分内容摘自[wiki词条](https://en.wikipedia.org/wiki/Kirkwood_gap)
