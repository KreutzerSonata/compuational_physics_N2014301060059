#Waves on a String  

Homework 6.12  

##Abstract  

In this task we consider wave motion on a string, specifically the propagation of Gaussian wavepacket and realistic excitation profile.
Observation from a fixed point on the string produce a time-dependent signal which could be reduced to a simpler frequency spectrum form with the tool
of Fourier analysis, in this way we can easily tell the difference between the waves with different initial conditions.  

##Background  

The central equation of wave motion is  
![](https://camo.githubusercontent.com/609e94ed4c8841a6260ed3f756047e79337e3fd4/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f253543667261632537422535437061727469616c25354532253230792537442537422535437061727469616c25323074253545322537442533446325354532253543667261632537422535437061727469616c25354532253230792537442537422535437061727469616c2532307825354532253744)  
In the same way we delt with Laplace's equation, this equation can also be reduced to finite-difference form  
![](https://camo.githubusercontent.com/9f8d0f11cecc5c1d3ff21d25041552f27b0b59c3/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f2535436672616325374279253238692532436e26706c75733b3125323926706c75733b79253238692532436e2d312532392d3279253238692532436e25323925374425374225323825354344656c74612532307425323925354532253744253543617070726f78253230632535453225354225354366726163253742792532386926706c75733b312532436e25323926706c75733b79253238692d312532436e2532392d3279253238692532436e25323925374425374225323825354344656c74612532307825323925354532253744253544)  
With some arragement we have  
![](https://camo.githubusercontent.com/baa11eb0b0ba9cd3275b6dbfa1f075eeaf144f48/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f79253238692532436e26706c75733b3125323925334432253238312d722535453225323979253238692532436e2532392d79253238692532436e2d3125323926706c75733b7225354532253542792532386926706c75733b312532436e25323926706c75733b79253238692d312532436e253239253544)  
where ![](https://camo.githubusercontent.com/1e67aefd82f4dbf68997fcac1d5602f8c3d5cfdc/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f7225354365717569762532306325354344656c7461253230742f25354344656c746125323078) .
For simplicity we consider a string with fixed ends, so the interior part obeys the equation above, while the ends follows y(0,n)=
y(M,n)=0. Once we define the initial profile, the equation above determines how it evolve in the following time.  

To analyse the observation on a fixed point on a string, it's convenient to apply Fourier transform and get the frequency spectrum, 
if we are just concerned with the relative amplitudes of the Fourier components regardless their phases, power spectrum is a useful 
way to display the results of an FFT, which is given by  
![](https://camo.githubusercontent.com/0c01d1b9443dd7ceb9053c7e31dd09e21eb82e68/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f50532535427925354425323866253239253344253543696e745f2537422d253543696e667479253744253545253742253543696e6674792537447925323874253239253545253543617374253230792532387426706c75733b253543746175253239652535452537423225354370692532306966253543746175253744642535437461752533442535436c6566742532302537432532305925323866253239253230253543726967687425323025374325354532)  


##Mainbody  

A Gaussian wavepacket at the center of a string as initial condition would decompose into two travelling wave   
![](http://p1.bpimg.com/567571/72d9758dd4fcd37f.gif)  
From which we can see the the wave inverts at the ends. Observe from a point on the string, say 5% from one end of the string, and
we get a signal diagram  
![](http://p1.bpimg.com/567571/df54e443fc7e6f16.png)  
The corresponding power spectrum looks like  
![](http://p1.bpimg.com/567571/094e1ac1eab8162d.png)  
Notice that only odd times fundemental frequency (150Hz in this caes) produces a peak because our initial condition
suppresses standing waves with a node at the center of the string. If the initial wavepacket deviates a little from the center,
these suppressed peak will come about.   

Next we consider a more realistic excitation form. When a guitar string is being plucked, the initial profile is triangular, with
two straight lines that start at the ends of the string and end at the excitation point, namely the central point, then the propagation
of the wave looks like  
![](http://p1.bpimg.com/567571/1f433230e1037ac2.gif)  
With a time-dependent signal  
![](http://p1.bpimg.com/567571/08d2f1b2dc97b83c.png)  
Which could be transformed as  
![](http://p1.bpimg.com/567571/7758e8fb5f374a8d.png)  
[code for propagation](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/code/plucking.py)  
[code for power spectrum]()
From the comparison we see that, the main sound when plucking a guitar string comes with the fundemental frequency, this agrees with our daily experience,
people are tending to regard the fundemental frequency of a string as its tone in music.  

##Conclusion  

The conclusion gained from the power spectrum can be generalized, If the string with length l is excited at l/n from one end, 
the peaks at knf0 in its power spectra vanishes, where k is an arbitrary positive integer, and f0 is fundamental frequency of 
this string.  

##Acknowledgment and Reference  
参考吴雨桥的程序~
