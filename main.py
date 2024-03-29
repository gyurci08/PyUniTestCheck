import json

from GUI.main import TkinterApp
from Repository.ExamRepository import ExamRepository


def loadExams():
    with open("Data/exam_data.json", "r") as file:
        json_data = json.load(file)
        file.close()
    exams = ExamRepository(json_data)

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

    gui = TkinterApp.App(exams)
    gui.mainloop()

    exportExams(exams)




if __name__ == '__main__':
    start()


