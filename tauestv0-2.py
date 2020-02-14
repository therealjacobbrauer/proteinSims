
#tau code

import numpy as np
from numpy.random import seed
from numpy.random import rand

# f(x,y,z,orientation(pitch),yaw, ) for each particle
# number rows- 1 is number of particles

nProts = 2
nVars = 5
nSpatialDims = 3

prot = np.arange(nVars*(nProts+1)).reshape(1+nProts,nVars)
print(prot)

# mouth is origin
# array for spring consts between each particle. 
# 2 arms, 2 legs are springs and torso is stiff. 
# g(arm1, arm2, leg1, leg2) == spring consts in units [N/m]

nSprings = nProts*4
nSpringCats = 4 # four spring categories for the four types of geoms that have spring constants. 

stretchn = np.arange(nSprings+nSpringCats).reshape(1+nProts,nSpringCats)
print(stretchn)

Distances = np.arange(1+nProts) # a 1d array of the distances
print(Distances)

np.place(Distances, Distances>0, [((((((prot[2,0])-prot[1,0])**2) + ((prot[2,1] - prot[1,1]) ** 2) + ((prot[2,2]) - prot[1,2]) ** 2)) **(1/2)), (((((prot[1,0])-prot[2,0])**2) + ((prot[1,1] - prot[2,1]) ** 2) + ((prot[1,2]) - prot[2,2]) ** 2)) **(1/2)  ])
print(Distances)

print('Please input a value below for the lumped spring constant.')
LumpedSpringConst = input()

LumpedSpringConst = float(LumpedSpringConst)
Energies = (0.5)*LumpedSpringConst*(Distances**2)

print("Energy between ith particle is: ")
print(Energies)

seed(10000)

rand(1)

#need to get this random number generator to put random values for x,y,z into the prot array to test
#new values of x,y,z to see if they have less energy than the inital guess. 
randomnums = np.random.rand(1,10)
print(prot)
for i in range (2, 10):

	np.place(prot, (nVars-1)<prot, [randomnums[1]])
	print(prot)



# approaching a monte carlo method. If the spring constant is used between two prots, and they
# are sampled for a new randomly chosen position, if the new position is of lower energy, then
# the particle is moved to the new position with lower energy. 

#joules are in N*m
