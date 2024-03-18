"""Uses PYQT6 module to create a GUI to select and view all spherical harmonics. Currently incomplete"""

import pickle
import matplotlib.pyplot as plt

with open("HarmonicsData.pickle", "rb") as test:
    a = pickle.load(test)
    

    for i in range(14):

        x = a[i]["x"]
        y = a[i]["y"]
        z = a[i]["z"]
        cmap = a[i]["harmonic_colourmap"]

        fig = plt.figure(figsize=plt.figaspect(1.))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors = cmap)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        ax.set_zlim(-1,1)
        plt.axis("equal")
        plt.show()