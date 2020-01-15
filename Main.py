from Rot_Table import *
from Traj3D import *


def main():

	rot_table = Rot_Table()
	traj = Traj3D()

	traj.compute("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAAGGTTAAGTCAG", rot_table)

	print(traj.getTraj())

	traj.draw("test.png")


if __name__ == "__main__" :
    main()
