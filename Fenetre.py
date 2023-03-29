import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import Controle as test


def showGraphMaro(anaranas):
    # w1 = test.Controle()
    # moyenne = w1.moyenneTemp(*anarana)
    # print(moyenne)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Initialize empty arrays for x, y, and z data
    x_data = np.array([])
    y_data = np.array([])
    z_data = np.array([])

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    # Loop over all "anaranas"
    for anarana in anaranas:
        x11 = test.Controle()
        aa = x11.getZ(anarana)
        Caa = []
        y11 = test.Controle()
        bb = y11.getY(anarana)
        Cbb = []
        z11 = test.Controle()
        cc = z11.getX(anarana)
        Ccc = []

        for _ in aa:
            Caa.append(float(_[0]))
        for _ in bb:
            Cbb.append(float(_[0]))
        for _ in cc:
            Ccc.append(int(_[0]))

        # Append x, y, and z data to the existing arrays
        x_data = np.append(x_data, Caa)
        y_data = np.append(y_data, Cbb)
        z_data = np.append(z_data, Ccc)

    # Plot the data
    ax.scatter(x_data, y_data, z_data, c=colors[5%len(colors)])
    ax.plot(x_data, y_data, z_data, linestyle='-', c=colors[5%len(colors)])

    ax.set_xlabel('X Jour  ')
    ax.set_ylabel('Y Temperature (en °C)')
    ax.set_zlabel('Z Oxygene (en %)')
    ax.set_title('Details des patients')

    plt.show()


def showGraphMaro1(anarana):
    x1 = test.Controle()
    a = x1.getZ(anarana)
    Ca = []
    y1 = test.Controle()
    b = y1.getY(anarana)
    Cb = []
    z1 = test.Controle()
    c = z1.getX(anarana)
    Cc = []
    for ac in a:
        Ca.append(float(ac[0]))
    for bc in b:
        Cb.append(float(bc[0]))
    for ck in c:
        Cc.append(int(ck[0]))

    x = np.array([])
    y = np.array([])
    z = np.array([])

    x = np.append(x, Ca)
    y = np.append(y, Cb)
    z = np.append(z, Cc)

    colors = ['k' if value < 50 else '#0000FF' for value in z]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c=colors)
    ax.plot(x, y, z, linestyle='-')

    ax.set_xlabel('X Jour  ')
    ax.set_ylabel('Y Temperature (en °C)')
    ax.set_zlabel('Z Oxygene (en %)')
    ax.set_title('Details du patient: ' + anarana)

    plt.show()
