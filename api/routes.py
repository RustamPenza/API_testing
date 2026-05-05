from enum import Enum

class Routes(str, Enum):
    OBJECTS = '/objects'
    OBJECTS_ITEMS = '/objects/{}'

    def __str__(self) -> str:
        return self.value
    