import numpy as np

#%% Global variables
N_A = 6.022e23 # Avagadro's number
l_OD = 1e7 # OD to cell #
V_sample = 5 # mL

#%% Calculating uptake metal
# parameters
OD = 1
d = 4e-6 # m
uptake = 100e-6 # M

# volume
def volume(d):
	"""
	@args:
		- d = diameter (um) 
	@returns:
		- V = volume (L)
	"""
	return 4/3 * np.pi * np.power(d/2, 3) # um^3

# number of uptaken per yeast
N_m = uptake * N_A # molecules/L
N_yeast = OD * l_OD * V_sample # number of yeast
N_uptake = N_m / N_yeast * V_sample * 1e-3
print(N_uptake)