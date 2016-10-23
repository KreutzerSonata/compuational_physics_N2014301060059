#Auxiliary Attacking System  
Homework 2.10, L1  

##Abstract  

This task involves a more realistic model dealing with a movable target, namely a target at a differet altitude than the cannon.
The goal is to determine the minimum firing velocity and its corresponding firing angle to hit the target, to solve this, a correct velocity
is calculated at each fixed angle, after scanning over a 90° range we can find the best shooting parameter. Besides, An adiabatic model is
applied to determine the altitude effect, and headwind is put into consideration.  

##Background  

[In last excercise](https://github.com/KreutzerSonata/compuational_physics_N2014301060059/blob/master/EXCERCISE_05.md) we have implemented Euler method to make a numerical calculation for a set of second-order ODE describing cannon
shell's flying trajectory, the key step is to derive finite difference form of the equations.  
![](https://camo.githubusercontent.com/8a1ab28bc76db3b262d7b37fcbc60d6333d3ef97/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f253543253543253230785f2537426926706c75733b31253744253344785f6926706c75733b765f253742782532436925374425354344656c746125323074253230253543253543253230253543253543253230765f253742782532436926706c75733b31253744253344765f25374278253243692537442d2535436672616325374225354372686f25323025374425374225354372686f2532305f3025374425354366726163253742425f3276765f25374278253243692537442537442537426d25374425354344656c746125323074253230253543253543253230253543253543253230795f2537426926706c75733b31253744253344795f6926706c75733b765f253742792532436925374425354344656c746125323074253230253543253543253230253543253543253230765f253742792532436926706c75733b31253744253344765f25374279253243692537442d6725354344656c7461253230742d2535436672616325374225354372686f25323025374425374225354372686f2532305f3025374425354366726163253742425f3276765f25374279253243692537442537442537426d25374425354344656c746125323074)  
We have already used the the adiabatic model ![](https://camo.githubusercontent.com/967d25dfed65f2f45de0647dda8aa52a773c6849/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f25354372686f25323025334425354372686f2532305f30253238312d253543667261632537426179253744253742545f30253744253239253545253742253543616c706861253230253744)
to predict the change of air density along altitudes. This time we add the effect of headwind so the drag force changes to  
![](https://camo.githubusercontent.com/2b41a53fef7614bc02086478a3f225eb2fb80f8e/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f465f25374264726167253243782537442533442d425f253742322537442535437371727425374276253545322d765f25374277696e6425374425354532253744253238765f253742782537442d765f25374277696e64253744253239)
 , ![](https://camo.githubusercontent.com/9d326e13b1e20294ba1d2996db49c556c70497d8/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f465f25374264726167253243792537442533442d425f253742322537442535437371727425374276253545322d765f25374277696e6425374425354532253744765f25374279253744)  
Substitute these specific expression for the previous forces and it's ready to run a simulation.  

##Mainbody  

In reality a target is not always fixed at floor level, to hit targets at various positions, an auxiliary attacking system is required
, it takes in the relative distance and height and feedback with possible shooting parameters. Usually there's more than one trajectory
reach a specific target, for sake of saving gunpowder, the best choice is the one with minimum firing velocity.  

A simulation method is to calculate the correct firing velocity at each fixed angle, after scanning over a 90° range we can find the best 
shooting parameter. There is a tricky to make the program more efficient, we don't need to handle with all angles among the 90° range degree
by degree, a dichotomic method help lot, the syntax is as follows  
![]()
        
A futher simplification is to reduce the scanning range to 25°~60° since we expect the maximum shooting range would appear within.  
[here is the code]()


