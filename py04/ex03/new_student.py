import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
     GENERATE RANDOM ID
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
     class student
    """
    name: str
    surname: str
    is_active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        Post-initialization method to set the login name to the nickname.
        """
        self.is_active = True
        if len(self.name) > 0:
            self.login = self.name[0] + self.surname
        self.id: str = generate_id()

# student = Student(name = "Edward", surname=  "agle")
# print(student)
