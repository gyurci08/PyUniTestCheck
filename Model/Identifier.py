from dataclasses import dataclass
from typing import List


@dataclass
class Identifier:
    original: List[int]
    image: str
    confirmed_identifier: str

    def __init__(self, **identifier):
        self.original = identifier['original']
        self.image = identifier['image']
        try:
            self.confirmed_identifier = identifier['confirmed_identifier']

        except KeyError:
            self.confirmed_identifier = None

    def serialize(self):
        return (self.__dict__)