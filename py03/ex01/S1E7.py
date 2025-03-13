from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, first_name, is_alive=True,
                 family_name='Baratheon', eyes='brown', hairs='dark'):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        """Return a string representation of the object"""
        return self.__str__()


class Lannister(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, first_name, is_alive=True,
                 family_name='Lannister', eyes='blue', hairs='light'):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        """Return a string representation of the object"""
        return self.__str__()

    def create_lannister(first_name: str, is_alive: bool):
        """create lanister constuctor"""
        return Lannister(first_name, is_alive)
