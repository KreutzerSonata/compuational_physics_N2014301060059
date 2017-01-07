#Random Walks and Diffusion  
姓名：白德凡  
学号：2014301060059  
班级：物理学基地一班  

##Abstract  

In this final task, we investigate the properties of a random system by firstly introducing the random walk model, then compare it
with the diffusive equation(in two dimension), finally check the statistical interpretation of entropy.  

##Background  

Generally we take the evolution of *any* system as determinitstic, which means in principle we can find some mathematical rules(such
as Newton's laws) to describe the their motions. However, in previous chapters, we have seen that a good many of such systems are *unpredicable* because
of the arising of chaos. In this task, we investigate another kind of systems ivolving randomness, they are actually both determinitstic
and predicable, but the tremendous number of *degree of freedom* makes it infeasible and useless to calculate the results by solving
each motion equation. Instead, statistics gives us a more concise and comprehensible understanding of the system's behaviour.  

The motion of a particle or molecule is analogous to a random walk,  where the walker's steps correspond to the motion of the particle between collisions, each collision changes the direction of the velocity of paricle, and this is modeled by letting the direction of each step in the walk be random. Consider one-dimmensional walks, writing the position after n steps as a sum of n separate steps gives  
![](http://latex.codecogs.com/gif.latex?x_%7Bn%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Ds_%7Bi%7D)  
where ![](http://latex.codecogs.com/gif.latex?s_%7Bi%7D%3D%5Cpm%201) with equal probabilities for simplicity. Then statistics suggests the average of the square of the displacement after n steps is given as  
![](http://latex.codecogs.com/gif.latex?%5Cleft%20%5Clangle%20x_%7Bn%7D%5E%7B2%7D%20%5Cright%20%5Crangle%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Ds_%7Bi%7D%5E%7B2%7D%3Dn)  
If one step is taken in one time unit, this result implies the displacement of the walker grows as ![](http://latex.codecogs.com/gif.latex?%5Csqrt%7B%5Cleft%20%5Clangle%20x%5E%7B2%7D%20%5Cright%20%5Crangle%7D%5Csim%20t%5E%7B1/2%7D) , and this should be verified in the following simulation.  

On the other hand, the diffusion equation has a similar form as waves equation  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20%5Crho%20%7D%7B%5Cpartial%20t%7D%3DD%5Cbigtriangledown%20%5E%7B2%7D%5Crho)  
with ρ representing the density of particles. A typical solution of this equation has a Gaussian form  
![](http://latex.codecogs.com/gif.latex?%5Crho%20%28x%2Ct%29%3D%5Cfrac%7B1%7D%7B%5Csigma%20%7Dexp%5Cleft%20%5B%20-%5Cfrac%7Bx%5E%7B2%7D%7D%7B2%5Csigma%20%5E%7B2%7D%7D%20%5Cright%20%5D)  
for one dimension, with ![](http://latex.codecogs.com/gif.latex?%5Csigma%20%3D%5Csqrt%7B2Dt%7D), which implies the width increases as ![](http://latex.codecogs.com/gif.latex?%5Csigma%5Csim%20t%5E%7B1/2%7D), the same with random walk. From this we can see the close connection between diffusion and random walk, and it will be clearer by simulative illustration.  

The definition of entropy ![](https://camo.githubusercontent.com/50db2c9d90480aea76403a5cf24bf2109dd01806/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f533d2d25354373756d2532305f25374269253744505f253742692537446c6e505f25374269253744) will be used in the last section, where pi is the probability of finding the system in state i, and the sum is over all possible states of the system.  

##Mainbody  

###Random Walk  
To perform the random walk in one dimension, we generate a random number in the range between 0 and 1 and compare its value to 1/2, if it's less than 1/2, our walker moves right, otherwise it moves left. Repeat this process n times. The following figure shows the results for two individual walkers, as we expect, their trajecototies are much different. Actually each line of this kind is unique .
![](http://i1.piimg.com/567571/433637dff8137497.png)  
However, a large number of such walkers, say 5000 as a whole obeys a certain statistical rule. We add up the displacement of every walker and take the average, as expected, it should be fluctuating around zero.  
![](http://i1.piimg.com/567571/50ad2863078ee80c.png)  
Then we consider the average of the square of the displacement after n steps.  
![](http://i1.piimg.com/567571/5edcc121c6831f63.png)  
It grows linearly with time, we write this as ![](http://latex.codecogs.com/gif.latex?%5Cleft%20%5Clangle%20x%5E%7B2%7D%20%5Cright%20%5Crangle%3D2Dt), and the value of D is around 1/2 from the slope of the line, this result is in agreement with our previous statistical one. If we take the root-mean-square value, ![](http://latex.codecogs.com/gif.latex?%5Csqrt%7B%5Cleft%20%5Clangle%20x%5E%7B2%7D%20%5Cright%20%5Crangle%7D%5Csim%20t%5E%7B1/2%7D),  Compared with a free walker whose displacement is described as x=vt, a random walker escapes from the origin more slowly.  

To generalize the model and make it more realistic, one way is to allow the steps to be of random length. To do this, each time we take a random number from -1~+1 as the length of step, then add them up and take the average. We'll find the walking pattern and the behaviour of the mean displacement is much like the previous one, yet the relation of mean square of the displencement versus time is different.  
![](http://i1.piimg.com/567571/979d9ea04fda6986.png)  
Obviously the slope is smaller than fixed step length case, though it also obeys the statistical rules.  
[code for walking pattern](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/two%20random%20walkers.py)  
[code for mean dispalcement](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/x%20average%20for%205000%20walkers.py)  
[code for mean square of the displencement](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/x%20square%20average.py)  

###Diffusion  
Next we explore the properties of diffusion. With a similar treatment as we do in wave's case, chose the initial condition as a Gaussian profile, and the revolution for one dimension is  
![](http://p1.bqimg.com/567571/ba00575484960c2c.png)  
The peak value decreases rapidly, while the width grows, and the total area remains fixed.  

Then we use the random walk model to simulate a two-dimensional diffusion, such as cream spreading in coffee. The initial condition is a cup of coffee containing a drop of cream in the centre. We assume each of the cream molecule executes a rondom walk on a two-dimensional square lattice, at each time step we choose a particle at random and let it take one step in its random walk. The distributions after t=0, 50, 200, 800 are showed as follows, as expected, the cream spreads with time in a manner that appears by eye to be diffusive. This result is equivalent to the solution of the two-dimensional diffusion equation.   
![](http://p1.bqimg.com/567571/ccda79286f2bcf1f.png)  

[code for one-dim diffusion](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/diffusion%20in%20one%20dimension.py)  
[code for two-dim diffusion](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/diffusion%20in%20two%20dimension.py)  

###Entropy  

The cream-in-coffee problem is a nice example to introduce the concept of entropy. We divide the two-dimensional coffee cup into grid cells, each representing a distinct state in which a particle might be found. The previous simulation involves a large number of particles, we can use all of them, say 5000, in the computation of entropy.   
![](http://i1.piimg.com/567571/de9d5d36f636c59f.png)  

The entropy increases and eventually levels off, it approaches a constant. This result is in agreement with the second thermodynamic law, saying that the entropy of a isolated system never decreases, and should increase for irreversible process like diffusion, until it eventually converges to a constant, which implies the system reaches equilibrium. 

[code for entropy](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/entropy.py)  

##Conclusion  

From the previous simulations we see, the average displacement of large number of random walkers is zero, while the mean square of displacement is linearly dependented on time, and the latter leads to diffusive phenomennon. Random walk model is a good approximation of diffusive phenomennon, it's all based on simple statistical rules regardless of the dynamic rules the particles involves, thus reveals the profound mathematical nature of the physical problems. However, this also deviates the model from many real problems, for appreciable interactions do exist between particles in many cases, and the behaviour is much different. Such a system is a *complex system* rather than a random one, this field contains many interesting topics such as Earth's global climate, organisms, the human brain, social organization and so on, and it's still under spiritoso exploration.  

##Reference  

1.Computational Physics, Nicholas J. Giordano & Hisao Nakanishi  
2.[Python图表绘制：matplotlib绘图库入门](http://blog.csdn.net/ywjun0919/article/details/8692018)  
3.Wiki entry [Complex System](https://en.wikipedia.org/wiki/Complex_system)  



