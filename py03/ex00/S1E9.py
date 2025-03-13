from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract die class"""
        pass


@abstractmethod
class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive=True):
        """Your docstrinyg for constructor"""
        Character.__init__(self, first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
