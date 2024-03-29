import json
from dataclasses import dataclass
from typing import List

from GUI.main import TkinterApp


def compareConfirmed(orig, confirmed):
    if confirmed is not None:
        return confirmed
    else:
        return orig




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


@dataclass
class Result:
    original: str
    image: str
    confirmed: str

    def __init__(self, **result):
        self.original = result['original']
        self.image = result['image']
        try:
            self.confirmed = result['confirmed']
        except KeyError:
            self.confirmed = None

@dataclass
class Exam:
    identifier: Identifier
    result: Result

    def __init__(self, **exam ):
        self.identifier = Identifier (**exam['identifier'])
        self.result = Result (**exam['result'])


@dataclass
class ExamList:
    list: List[Exam]

    def __init__(self,  **exams):
        self.list = [Exam (**exams[key]) for key in exams]


def loadExams():
    test2_json = dict
    with open("exam_data.json", "r") as file:
        json_data = json.load(file)
        file.close()
    exams = ExamList(**json_data)

    return exams

def exportExams(exams):
    with open("exam_export.json", "w") as file:
        json.dump(exams, file)
        file.close()

def start():
    exams = loadExams()

    gui = TkinterApp.App(exams)
    gui.mainloop()

    #exportExams(exams)

if __name__ == '__main__':
    start()


