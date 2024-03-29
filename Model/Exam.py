from dataclasses import dataclass

from Model.Identifier import Identifier
from Model.Result import Result


@dataclass
class Exam:
    identifier: Identifier
    result: Result

    def __init__(self, **exam ):
        self.identifier = Identifier (**exam['identifier'])
        self.result = Result (**exam['result'])

    def serialize(self):
        return {"identifier": self.identifier.serialize(), "result": self.result.serialize()}
