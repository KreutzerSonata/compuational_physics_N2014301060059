#Chaos in the Driven Nonlinear Pendulum  
Homework 3.12, 3.13, 3.14  

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