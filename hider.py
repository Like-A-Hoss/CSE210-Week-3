from random import randint as rand
class hider():
    def __init__(self) -> None:
        self.location = rand(1,100)
    
    def report_location(self):
        """Returns the location for compairison"""
        return self.location
    def change_location(self):
        """Changes the location of the hider"""
        self.location = rand(1,100)