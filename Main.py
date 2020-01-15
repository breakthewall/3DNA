from RotTable import *
from Traj3D import *


def main():

	rot_table = RotTable()
	traj = Traj3D()

	traj.compute("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAAGGTTAAGTCAG", rot_table)

	print(traj.getTraj())

	traj.draw("test.png")


if __name__ == "__main__" :
    main()
