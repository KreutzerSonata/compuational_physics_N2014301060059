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



