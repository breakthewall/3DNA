import math

#For drawing
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .RotTable import RotTable


class Traj3D:
    """Represents a 3D trajectory"""

    # Vertical translation (elevation) between two di-nucleotides
    __MATRIX_T = np.array(
        [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -3.38/2],
        [0, 0, 0, 1]]
    )

    def __init__(self):
        self.__Traj3D = {}
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')

    def getTraj(self) -> dict:
        return self.__Traj3D

    def compute(self, dna_seq: str, rot_table: RotTable):

        # Matrice cumulant l'ensemble des transformations géométriques engendrées par la séquence d'ADN
        total_matrix = np.eye(4)  # Identity matrix

        # On enregistre la position du premier nucléotide
        self.__Traj3D = [np.array([0.0, 0.0, 0.0, 1.0])]

        matrices_Rz = {}
        matrices_Q = {}
        # On parcourt la sequence, nucléotide par nucléotide
        for i in range(1, len(dna_seq)):
            # On lit le dinucleotide courant
            dinucleotide = dna_seq[i-1]+dna_seq[i]
            # On remplit au fur et à mesure les matrices de rotation
            if dinucleotide not in matrices_Rz:
                matrices_Rz[dinucleotide], matrices_Q[dinucleotide] = \
                    self.__compute_matrices(rot_table, dinucleotide)

            # On calcule les transformations géométriques
            # selon le dinucleotide courant,
            # et on les ajoute à la matrice totale
            total_matrix = \
                total_matrix \
                @ self.__MATRIX_T \
                @ matrices_Rz[dinucleotide] \
                @ matrices_Q[dinucleotide] \
                @ matrices_Rz[dinucleotide] \
                @ self.__MATRIX_T

            # On calcule la position du nucléotide courant
            # en appliquant toutes les transformations géométriques
            # à la position du premier nucléotide
            self.__Traj3D.append(total_matrix @ self.__Traj3D[0])

    def __compute_matrices(self, rot_table: RotTable, dinucleotide: str):

        Omega = math.radians(rot_table.getTwist(dinucleotide))
        # Create rotation matrix of theta on Z axis
        matrices_Rz = \
            np.array([[math.cos(Omega/2), math.sin(Omega/2), 0, 0],
                        [-math.sin(Omega/2), math.cos(Omega/2), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

        sigma = rot_table.getWedge(dinucleotide)
        delta = rot_table.getDirection(dinucleotide)
        alpha = math.radians(sigma)
        beta = math.radians(delta - 90)
        # Rotate of -beta on Z axis
        # Rotate of -alpha on X axis
        # Rotate of beta on Z axis
        matrices_Q = \
            np.array([[math.cos(-beta), math.sin(-beta), 0, 0],
                        [-math.sin(-beta), math.cos(-beta), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]) \
            @ np.array([[1, 0, 0, 0],
                            [0, math.cos(-alpha), math.sin(-alpha), 0],
                            [0, -math.sin(-alpha), math.cos(-alpha), 0],
                            [0, 0, 0, 1]]) \
            @ np.array([[math.cos(beta), math.sin(beta), 0, 0],
                        [-math.sin(beta), math.cos(beta), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
        
        return matrices_Rz, matrices_Q

    def draw(self):
        xyz = np.array(self.__Traj3D)
        x, y, z = xyz[:,0], xyz[:,1], xyz[:,2]
        self.ax.plot(x,y,z)
        plt.show()

    def write(self, filename: str):
        self.fig.savefig(filename)