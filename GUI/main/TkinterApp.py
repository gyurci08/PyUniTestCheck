import tkinter
import customtkinter

from tkinter import messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self, list):
        super().__init__()

        # configure window
        self.title("PythonHomework")
        self.geometry(f"{860}x{600}")

        self.la_padx = 10
        self.la_pady = 10


        self.curr_exam = 0
        self.exams = list.list


        # configure grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create id frame with widgets
        self.fr_id = customtkinter.CTkFrame(self, corner_radius=0,)
        self.fr_id.grid(row=0, column=0, columnspan=2)
        self.la_id = customtkinter.CTkLabel(self.fr_id, text="ID: ", width=10, justify="left")
        self.la_id.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)
        self.la_id_value = customtkinter.CTkLabel(self.fr_id, text="TODO", justify="left")
        self.la_id_value.grid(column=1, row=0, padx=self.la_padx, pady=self.la_pady)
        self.la_conf_id = customtkinter.CTkLabel(self.fr_id, text="Confirmed ID: ")
        self.la_conf_id.grid(column=0, row=1, padx=self.la_padx, pady=self.la_pady)
        self.tb_conf_id_value = customtkinter.CTkEntry(self.fr_id)
        self.tb_conf_id_value.grid(column=1, row=1, padx=self.la_padx, pady=self.la_pady)

        # create id image frame with widgets
        self.fr_id_img = customtkinter.CTkFrame(self, corner_radius=0, width=300, height=300)
        self.fr_id_img.grid(row=0, column=1, columnspan=4)
        self.la_id_img = customtkinter.CTkLabel(self.fr_id_img, text="IMG")
        self.la_id_img.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)

        # create results frame with widgets
        self.fr_results = customtkinter.CTkFrame(self, corner_radius=0)
        self.fr_results.grid(row=1, column=0, columnspan=2)
        self.la_results = customtkinter.CTkLabel(self.fr_results, text="Results: ")
        self.la_results.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)
        self.la_results_value = customtkinter.CTkLabel(self.fr_results, text="TODO")
        self.la_results_value.grid(column=1, row=0, padx=self.la_padx, pady=self.la_pady)
        self.la_conf_results_id = customtkinter.CTkLabel(self.fr_results, text="Confirmed Results: ")
        self.la_conf_results_id.grid(column=0, row=1, padx=self.la_padx, pady=self.la_pady)
        self.tb_conf_results_id_value = customtkinter.CTkEntry(self.fr_results)
        self.tb_conf_results_id_value.grid(column=1, row=1, padx=self.la_padx, pady=self.la_pady)

        # create id image frame with widgets
        self.fr_results_img = customtkinter.CTkFrame(self, corner_radius=0, width=300, height=300)
        self.fr_results_img.grid(row=2, column=0, columnspan=4)
        self.la_results_img = customtkinter.CTkLabel(self.fr_results_img, text="IMG")
        self.la_results_img.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)


        #
        self.fr_search = customtkinter.CTkFrame(self, corner_radius=0)
        self.fr_search.grid(row=3, column=0, columnspan=4)
        self.la_search = customtkinter.CTkLabel(self.fr_search, text="Search (ID): ")
        self.la_search.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)
        self.tb_search = customtkinter.CTkEntry(self.fr_search)
        self.tb_search.grid(column=1, row=0, padx=self.la_padx, pady=self.la_pady)
        #
        self.fr_nav = customtkinter.CTkFrame(self, corner_radius=0)
        self.fr_nav.grid(row=4, column=0, columnspan=4)
        self.bt_prev = customtkinter.CTkButton(self.fr_nav, text="Prev", command=self.prev_exam)
        self.bt_prev.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)
        self.bt_search = customtkinter.CTkButton(self.fr_nav, text="Search", command=self.search_exam)
        self.bt_search.grid(column=1, row=0, padx=self.la_padx, pady=self.la_pady)
        self.bt_confirm = customtkinter.CTkButton(self.fr_nav, text="Confirm", command=self.confirm_exam)
        self.bt_confirm.grid(column=2, row=0, padx=self.la_padx, pady=self.la_pady)
        self.bt_next = customtkinter.CTkButton(self.fr_nav, text="Next", command=self.next_exam)
        self.bt_next.grid(column=3, row=0, padx=self.la_padx, pady=self.la_pady)

        self.refresh()

    def compareConfirmed(self, orig, confirmed):
        if confirmed is not None:
            return confirmed
        else:
            return orig

    def confirm_exam(self):
        if not len(self.tb_conf_id_value.get()) < 1:
            self.exams[self.curr_exam].identifier.confirmed_identifier = self.tb_conf_id_value.get()
        if not len(self.tb_conf_results_id_value.get()) < 1:
            try:
                self.exams[self.curr_exam].result.confirmed =[int (result) for result in self.tb_conf_results_id_value.get().split(",")]
            except ValueError:
                dialog =  tkinter.messagebox.showerror(title="Error", message=r"You are using invalid separator! Try: , (comma)")
        self.refresh()

    def search_exam(self):
        isFound = False
        for i in range(len(self.exams)):
            id = self.compareConfirmed(self.exams[i].identifier.original,
                                       self.exams[i].identifier.confirmed_identifier)

            if id == self.tb_search.get():
                self.curr_exam = i
                self.refresh()
                isFound = True
        if isFound == False:
            dialog =  tkinter.messagebox.showinfo(title="Search ID", message="ID not found!")

    def prev_exam(self):
        if not self.curr_exam == 0:
            self.curr_exam -= 1
            self.refresh()


    def next_exam(self):
        if not self.curr_exam == len(self.exams)-1:
            self.curr_exam += 1
            self.refresh()

    def refresh(self):
        id = self.compareConfirmed(self.exams[self.curr_exam].identifier.original,
                              self.exams[self.curr_exam].identifier.confirmed_identifier)
        results = self.compareConfirmed(self.exams[self.curr_exam].result.original,
                                        self.exams[self.curr_exam].result.confirmed)
        self.la_id_value.configure(text=id)
        self.la_results_value.configure(text=results)




