from copy import deepcopy
from json import load as json_load
from os import path as os_path

here = os_path.abspath(os_path.dirname(__file__))

class RotTable:
    """Represents the rotation table"""

    # 3 first values: 3 angle values
    # 3 last values: SD values
    __ORIGINAL_ROT_TABLE = json_load(
        open(os_path.join(here, 'table.json'))
    )

    def __init__(self):
        self.__Rot_Table = deepcopy(RotTable.__ORIGINAL_ROT_TABLE)


    ###################
    # WRITING METHODS #
    ###################


    ###################
    # READING METHODS #
    ###################

    def getTwist(self, dinucleotide):
        return self.__Rot_Table[dinucleotide][0]

    def getWedge(self, dinucleotide):
        return self.__Rot_Table[dinucleotide][1]

    def getDirection(self, dinucleotide):
        return self.__Rot_Table[dinucleotide][2]

    ###################
