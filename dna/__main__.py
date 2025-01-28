from dna.RotTable import RotTable
from dna.Traj3D import Traj3D

from os import (
    path as os_path,
    getcwd as os_getcwd
)

here = os_path.abspath(os_path.dirname(__file__))

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input filename of DNA sequence")
parser.add_argument("--save-traj", help="Save the DNA 3D trajectory", action="store_true")
parser.add_argument("--save-fig", help="Save the figure of the DNA 3D trajectory", action="store_true")
parser.add_argument("--draw", help="Draw the DNA 3D trajectory", action="store_true")
parser.add_argument("--rot-table", help="Input filename of rotation table", default=os_path.join(here, "table.json"))
parser.parse_args()
args = parser.parse_args()

def main():

    rot_table = RotTable(args.rot_table)
    traj = Traj3D()

    # Read file
    lineList = [line.rstrip('\n') for line in open(args.filename)]
    # Formatting
    seq = ''.join(lineList[1:])
    traj.compute(seq, rot_table)

    working_dir = os_getcwd()
    basename = os_path.basename(args.filename).split('.')[0]

    # Save the trajectory
    if args.save_traj:
        traj.save_coords(
            os_path.join(working_dir, basename + ".csv")
        )
    else:
        print(traj.getTraj())

    # Draw the trajectory
    if args.draw:
        traj.draw()
    
    # Save the figure
    if args.save_fig:
        traj.save_fig(
            os_path.join(working_dir, basename + ".png")
        )


if __name__ == "__main__" :
    main()
