import json
import tkinter

from tkinter import messagebox
from GUI.main import TkinterApp
from Repository.ExamRepository import ExamRepository


def loadExams():
    try:
        with open("Data/exam_data.json", "r") as file:
            json_data = json.load(file)
            file.close()
        exams = ExamRepository(json_data)
        return exams
    except FileNotFoundError as e:
        tkinter.messagebox.showerror(title="Error", message=f"File not found: {e}")


def exportExams(exams):
    try:
        with open("Data/exam_data.json", "w") as file:
            json.dump(exams.serialize(), file)
            file.close()
        print("File saved.")
    except Exception as e:
        tkinter.messagebox.showerror(title="Error", message=f"Error during save: {e}")


def start():
    exams = loadExams()

    if not exams == None:
        gui = TkinterApp.App(exams)
        gui.mainloop()
        exportExams(exams)





if __name__ == '__main__':
    start()


