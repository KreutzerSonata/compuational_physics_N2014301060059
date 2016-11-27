#Planetary Orbits  

Homework 4.9  

##Abstract  

This task provides with a simulation of planetary orbits under the effort of gravity. As a conclusion, the inverse-square law is the
only form of gravitational force which maintains a planet in a stable orbit, otherwise the orbit rotates with elapsing, and the period
it remains stable is dependent on the ellipticity of the orbit with the same gravitational force form.  

##Background  

Since planetary motion is a typical oscillatory problem, we use Euler-Cromer method instead of Euler method to do the simulation just
as we did with pendulum. The rule for planetary motion is described through Newton's second law with two second-order ODEs which treat
the motion as a two-dimension problem. As usual the equations should be reduced to four first-order ones, thus converted into difference
form as follows  
![](https://camo.githubusercontent.com/6360ae0cac0fcbf444e703ccff428d7ef9d136bf/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f765f253742782532436926706c75733b31253744253344765f25374278253243692537442d2535436672616325374234253230253543706925354532253230785f25374269253744253744253742725f253742692537442535453325374425354344656c746125323074)  
![](https://camo.githubusercontent.com/dac3d82d16ff87987208b467a1e6b469ff851508/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f785f2537426926706c75733b31253744253344785f2537426925374426706c75733b765f253742782532436926706c75733b3125374425354344656c746125323074)  
![](https://camo.githubusercontent.com/7e76f28ed493a30f7dca85e122cf261e7f6bef26/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f765f253742792532436926706c75733b31253744253344765f25374279253243692537442d2535436672616325374234253230253543706925354532253230795f25374269253744253744253742725f253742692537442535453325374425354344656c746125323074)  
![](https://camo.githubusercontent.com/7d4009a6c03ead8447142456ab9549d41cd6e540/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f795f2537426926706c75733b31253744253344795f2537426925374426706c75733b765f253742792532436926706c75733b3125374425354344656c746125323074)  

Numbers invovling astronomy is very large, for the sake of simplicity, *astronomical units* are used, in which 1 AU equals the average distance between the Sun and Earth, and time is measured in years. In this unit the velocity of earth is 2π.  

##Mainbody  

The simplest orbit we can imagine is a circle, which indeed agrees with the real motion of earth around the sun quite well. However this is a very special case requiring the planet's initial velocity strictly perpendicular to its link to the sun, and having the magnitude of 2π. Any deviation from this initial value will leads to a elliptical orbit.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/speed.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/angle.png)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/initial%20velocity.py)  
This alludes that we can change the orbit's eccentricity by reseting the planet's initial velocity.  
In real world, the universal gravition meets the inverse-square dependence. To make a general extend, suppose the force is of this form  
![](https://camo.githubusercontent.com/b2009fbe9e15795aae881f247b449e141bfbb5d1/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f465f2537424725374425334425354366726163253742474d5f253742732537444d5f253742452537442537442537427225354525354362657461253744)   
If β=2, it's an inverse-sqaure law gravity and electromagnetic force both meet. But we consider the motion for values of β that are different from 2, and investigate how the planet behaves with different values of ellipticity of orbit.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/2.011.png)  
Set β=2.1, but the initial velocity is still perpendicular to the link to the sun, and taking the magnitude of 2π, then the orbit is a circle. Actually planet with this special initial velocity is destinated to draw a circular orbit no matter what the rule the interactive force obeys.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/2.3%20pi.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/2.5%20pi.png)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/orbit.py)  
Reseting the veloctiy to 2.3π and 2.5π actually changes the ellipticity of the orbit, with inverse-square force it should produces an ellipse, but in this case the orbit rotates, and the more elliptical the faster it rotates.  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/2.01%20beta.png)  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/2.001%20beta.png)  
A smaller value of β produces a familiar conclusion, in the last case the orbit rotates so slowly that it looks like a regular ellipse.  

##Conclusion  

![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/Precessing_Kepler_orbit_280frames_e0.6_smaller.gif)  
Any deviation from the inverse-square law will leads to a unstable orbit, though the difference may be very slight, since astronomy is a subject of great precision, it matters. Actually it is through astronomical observation of Mercury's precession that people prove the existence of the effort of general relativity, which correct the force law as  
![](https://camo.githubusercontent.com/1d927634df570151beebfd3dd54915386fb7c126/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f465f25374247253744253543617070726f7825323025354366726163253742474d5f253742532537444d5f2537424d25374425374425374272253545322537442532383126706c75733b25354366726163253742253543616c7068612537442537427225354532253744253239)  
where α is a coefficient. This deviation from inverse-square law contributes to Mercury's precession.  

##Acknowledgment and Reference  

参考了吴雨桥学长的程序，以及教材上的很多内容~

