"""Here I will calculate all spherical harmonics up to l = 3 and store their values and associated colourmaps into a file. This is to save on processing time when graphing said harmonics and allows for fast swapping between graphs. Helpful for less powerful computers."""

import numpy as np
import pickle


#Generate values for polar and azimuthal angles
theta = np.linspace(0, np.pi, 50)
phi = np.linspace(0, 2*np.pi, 50)
theta, phi = np.meshgrid(theta, phi)

#Stored values for ease of writing equations
a = np.sin(theta)*np.cos(phi)
b = np.sin(theta)*np.sin(phi)
c = np.cos(theta)

#All formulas for the real spherical harmonics for graphing purposes
#Source: https://en.wikipedia.org/wiki/Table_of_spherical_harmonics

#Y(0, 0)
Y_0_0 = 1/2 * np.sqrt(1/np.pi)

#Y(1, m)
Y_1_neg1 = np.sqrt(3/(4*np.pi))*b
Y_1_0 = np.sqrt(3/(4*np.pi))*c
Y_1_1 = np.sqrt(3/(4*np.pi))*a

#Y(2, m)
Y_2_neg2 = 1/2 * np.sqrt(15/np.pi) * a * b
Y_2_neg1 = 1/2 * np.sqrt(15/np.pi) * b * c
Y_2_0 = 1/4 * np.sqrt(5/np.pi) * (3 * c**2 - 1)
Y_2_1 = 1/2 * np.sqrt(15/np.pi) * a * c
Y_2_2 = 1/4 * np.sqrt(15/np.pi) * (a**2 - b**2)

#Y(3, m)
Y_3_neg3 = 1/4 * np.sqrt(35/(2*np.pi)) * b * (3 * a**2 - b**2)
Y_3_neg2 = 1/2 * np.sqrt(105/np.pi) * a * b * c
Y_3_neg1 = 1/4 * np.sqrt(21/(2*np.pi)) * b * (5 * c**2 - 1)
Y_3_0 = 1/4 * np.sqrt(7/np.pi) * (5 * c**3 - 3 * c)
Y_3_1 = 1/4 * np.sqrt(21/(2*np.pi)) * a * (5 * c**2 - 1)
Y_3_2 = 1/4 * np.sqrt(105/np.pi) * (a**2 - b**2) * c
Y_3_3 = 1/4 * np.sqrt(35/(2*np.pi)) * a * (a**2 - 3 * b**2)

#Array to store all spherical harmonics exluding Y_0_0
all_Y = [Y_1_neg1, Y_1_0, Y_1_1, Y_2_neg2, Y_2_neg1, Y_2_0, Y_2_1, Y_2_2, Y_3_neg3, Y_3_neg2, Y_3_neg1, Y_3_0, Y_3_1, Y_3_2, Y_3_3]

#Contains all info for coordinates and colour of plot
#Colour is in RGBA format
harmonics_dict = {}

#Y_0_0 is single valued and must be added to the dictionary seperately 
r = np.full(Y_0_0.shape, 0.5)
x = r * a
y = r * b
z = r * c
harmonic_colourmap = np.full((50, 50), (243/255, 223/255, 9/255, 0.8))

harmonics_dict[0] = {
        "x": x,
        "y": y,
        "z": z,
        "harmonic_colourmap": harmonic_colourmap
    }
#Store all info about each harmonic into a dictionary
for k in range(len(all_Y)):

    Y = all_Y[k]

    harmonic_colourmap = np.empty(Y.shape, dtype=tuple)
    r = np.abs(Y)

    #Cartesian coordinates
    x = r * a
    y = r * b
    z = r * c

    #Generates colour map for our harmonics. yellow indicates positive values and blue indicates negative
    for i in range(50):
        for j in range(50):
            if(Y[i, j]>0):
                harmonic_colourmap[i,j] = (243/255, 223/255, 9/255, 0.8)
            else: harmonic_colourmap[i, j] = (52/255, 149/255, 235/255, 0.8)
    
    harmonics_dict[k+1] = {
        "x": x,
        "y": y,
        "z": z,
        "harmonic_colourmap": harmonic_colourmap
    }
    

#Stores dictionary in a file to be used later
with open("HarmonicsData.pickle", "wb") as hd:
    pickle.dump(harmonics_dict, hd)    