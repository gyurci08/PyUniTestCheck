import json
from dataclasses import dataclass
from typing import List

from GUI.main import TkinterApp


def compareConfirmed(orig, confirmed):
    if confirmed is not None:
        return confirmed
    else:
        return orig



def convert(lst):
   res_dict = {}
   for i in range(0, len(lst), 2):
       res_dict[lst[i]] = lst[i + 1]
   return res_dict


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

    def serialize(self):
        return {"original": self.original, "image": self.image, "confirmed":self.confirmed}

@dataclass
class Exam:
    identifier: Identifier
    result: Result

    def __init__(self, **exam ):
        self.identifier = Identifier (**exam['identifier'])
        self.result = Result (**exam['result'])

    def serialize(self):
        return {"identifier": self.identifier.serialize(), "result": self.result.serialize()}

@dataclass
class ExamList:
    list: List[Exam]

    def __init__(self,  exams):
        self.list = [Exam(**exam) for exam in exams]

    def serialize(self):
        return [dict (**item.serialize()) for item in self.list]




def loadExams():
    test2_json = dict
    with open("Data/exam_data.json", "r") as file:
        json_data = json.load(file)
        file.close()
    exams = ExamList(json_data)

    return exams

def exportExams(exams):
    try:
        with open("Data/exam_data.json", "w") as file:
            json.dump(exams.serialize(), file)
            file.close()
        print("File saved.")
    except Exception as e:
        print(f"Error durring save: {e}")


def start():
    exams = loadExams()
    print(exams)

    gui = TkinterApp.App(exams)
    gui.mainloop()

    exportExams(exams)




if __name__ == '__main__':
    start()


