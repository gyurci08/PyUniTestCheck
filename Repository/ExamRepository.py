from dataclasses import dataclass
from typing import List

from Model.Exam import Exam


@dataclass
class ExamRepository:
    list: List[Exam]

    def __init__(self,  exams):
        self.list = [Exam(**exam) for exam in exams]

    def serialize(self):
        return [dict (**item.serialize()) for item in self.list]

