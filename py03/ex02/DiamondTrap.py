from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    '''A King that inherit from a Baratheon and a Lannister in the form of Diamond'''
    def __init__(self, first_name: str, is_alive=True):
        """Init a King"""
        super().__init__(first_name, is_alive)
    
    def set_eyes(self,var):
        self.eyes = var
    
    def get_eyes(self):
        """Get the eyes of the King"""
        return self.eyes

    def set_hairs(self, value):
        """Set the hairs of the King"""
        self.hairs = value

    def get_hairs(self):
        """Get the hairs of the King"""
        return self.hairs

    
    