

import numpy as np

# f(x,y,z,orientation(pitch),yaw, ) for each particle
# number rows- 1 is number of particles

nProts = 2
nVars = 5

prot = np.arange(nVars*(nProts+1)).reshape(1+nProts,nVars)
print(prot)

# mouth is origin
# array for spring consts between each particle. 
# 2 arms, 2 legs are springs and torso is stiff. 
# g(arm1, arm2, leg1, leg2) == spring consts

nSprings = nProts*4
nSpringCats = 4 # four spring categories for the four types of geoms that have spring constants. 

stretchn = np.arange(nSprings+nSpringCats).reshape(1+nProts,nSpringCats)
print(stretchn)

#tau code

# approaching a monte carlo method. If the spring constant is used between two prots, and they
# are sampled for a new randomly chosen position, if the new position is of lower energy, then
# the particle is moved to the new position with lower energy. 



