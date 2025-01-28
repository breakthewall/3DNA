from json import load as json_load
from json import dump as json_dump


class RotTable:
    """Represents a rotation table"""

    # 3 first values: 3 angle values
    # 3 last values: SD values

    def __init__(self, filename: str):
        self.rot_table = json_load(open(filename))

    ###################
    # WRITING METHODS #
    ###################
    def setTwist(self, dinucleotide: str, value: float):
        self.rot_table[dinucleotide][0] = value

    def setWedge(self, dinucleotide: str, value: float):
        self.rot_table[dinucleotide][1] = value

    def setDirection(self, dinucleotide: str, value: float):
        self.rot_table[dinucleotide][2] = value

    ###################
    # READING METHODS #
    ###################
    def getTwist(self, dinucleotide: str) -> float:
        return self.getTable()[dinucleotide][0]

    def getWedge(self, dinucleotide: str) -> float:
        return self.getTable()[dinucleotide][1]

    def getDirection(self, dinucleotide: str) -> float:
        return self.getTable()[dinucleotide][2]
    
    def getTable(self) -> dict:
        return self.rot_table

    ###################
    def save(self, filename: str):
        """Saves the current rotation table to a file."""
        with open(filename, 'w') as file:
            json_dump(self.rot_table, file)
