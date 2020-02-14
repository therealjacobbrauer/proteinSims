# proteinSims
protein simulation for tau interactions in a simplified MD spring based simulation

This is using a monte carlo method to find the most protein relaxed energies based off of spring constants for tau. 
Estimated spring constants are used currently, we are working toward getting measured spring constants from publically
available published works. 

Monte carlo samples a new position to determine if this new position is lower in potential energy than the previous position
effectively moving down the potential energy slope. 

The Lennard Jones potential is a popular Monte carlo method, but is not the molecular dynamics pure spring constant method 
being currently used in this code. We hope to work towards a lennard jones potential in the future. 
