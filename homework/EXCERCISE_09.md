#The Billiard Problem  

Homework 3.31  

##Abstract  

In this task another process to chaos is discussed, say a billiard moving without friction on a horizontal table, reflected only at the
boundary. If the table's shape is of high symmetry, like a square or a circle, then the billiard's trajectory is regular and the
corresponding phase space plot is simple. Once the symmetry is broken, the billiard's motion tends to be chaotic. Tables of different shapes of
are considered in this task.  


##Background  

Without firction the billiard's motion is quite simple, its velocity is a constant  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/equation.jpg)  
where vx and vy changes only through collision with the walls. For simplicity we take the collision as perfectly elastic, so the reflected trajactory
will be mirrorlike. Define the unit normal vector of the wall as n, the components of vi can be divided as  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/incident.jpg)  
To get the reflected velocity, reverse the perpendicular component and remain the parallel component  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/reflect.jpg)  

This can be realized in program by statement like, for example *ball.velocity.x = -ball.velocity.x* , where *ball.velocity.x* 
represents the x component of billard's velocity, in the meanwhile we correct its x position by *ball.pos.x = 2 * table_right.x - ball.pos.x* 
Then we can handle with various boundaries.  

##Mainbody  

First we choose a circle table, the trajectory looks like this  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/circle%20table1.png)  
With time goes, the ball reaches nearly every part of the table except a small circle near the core  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/circle%20table2.png)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/circle%20table.py)  

To capture the regularity in another way, we investigate a phase space of vx vs. x by plotting the points when the billiard crosses the y=0 axis. For a circle table, it looks like this  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/phase%20space1.png)  
From which we see the same conclusion that the billiard doesn't enter a small zone near the core.  

Next we change the the shape to an ellipse, the boundary is ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bx%5E%7B2%7D%7D%7B4%7D&plus;y%5E%7B2%7D%3D1) the trajectory becomes different  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/ellipse.png)  
[code is here](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/ellipse%20table.py)  
The corresponding phase space plot is  
![](https://raw.githubusercontent.com/KreutzerSonata/compuational_physics_N2014301060059/master/diagrams/phaes%20space2.png)  
Looks not so neat. Here rises the chaotic phenomenon. Keep changing the shape, for example cut a circle table along an axis and
and put the two halves a small distance apart, then fill these sections with straight segments, on such a stadium-like table, chaos also takes place.  

##Conclusion  

In the billiard problem, chaos rises form the broken symmetry of table, only tables of very high symmetry are nonchaotic. This allude that the chaos is everywhere in our daily life, for realistic tables or containers can't be perfectly symmetry, thus the gas molecules within behave just like the billiard on a odd-shaped table.  

##Acknowledgment and Reference  

参考了罗佳佳同学的程序，并进行一定的debug，然而还是没有达到预期效果╮(╯ _ ╰)╭




