from .RotTable import RotTable
from .Traj3D import Traj3D

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input filename of DNA sequence")
parser.parse_args()
args = parser.parse_args()

def main():

    rot_table = RotTable()
    traj = Traj3D()

    # Read file
    lineList = [line.rstrip('\n') for line in open(args.filename)]
    # Formatting
    seq = ''.join(lineList[1:])
    traj.compute(seq, rot_table)

    # print(traj.getTraj())

    traj.draw()
    traj.write(args.filename+".png")


if __name__ == "__main__" :
    main()
