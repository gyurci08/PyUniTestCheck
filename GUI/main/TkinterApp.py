import tkinter
import customtkinter
import PIL

from PIL import ImageTk, Image
from tkinter import messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self, exams):
        super().__init__()

        # configure window
        self.title("PythonHomework")
        self.geometry(f"{850}x{550}")


        self.la_padx = 10
        self.la_pady = 10


        self.curr_exam = 0
        self.exams = exams.list


        # configure grid layout
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)




        # create id frame with widgets
        self.fr_id = customtkinter.CTkFrame(self, corner_radius=0,)
        self.fr_id.grid(row=0, column=0, columnspan=1)

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
        self.fr_id_img.grid(row=0, column=1, columnspan=2)

        self.la_id_img = customtkinter.CTkLabel(self.fr_id_img, image=None)
        self.la_id_img.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)

        # create results frame with widgets
        self.la_results = customtkinter.CTkLabel(self.fr_id, text="Results: ")
        self.la_results.grid(column=0, row=2, padx=self.la_padx, pady=self.la_pady)

        self.la_results_value = customtkinter.CTkLabel(self.fr_id, text="TODO")
        self.la_results_value.grid(column=1, row=2, padx=self.la_padx, pady=self.la_pady)
        self.la_conf_results_id = customtkinter.CTkLabel(self.fr_id, text="Confirmed Results: ")
        self.la_conf_results_id.grid(column=0, row=3, padx=self.la_padx, pady=self.la_pady)
        self.tb_conf_results_id_value = customtkinter.CTkEntry(self.fr_id)
        self.tb_conf_results_id_value.grid(column=1, row=3, padx=self.la_padx, pady=self.la_pady)


        # create id image frame with widgets
        self.fr_results_img = customtkinter.CTkFrame(self, corner_radius=0, width=500, height=300)
        self.fr_results_img.grid(column=0, row=1,  columnspan=3)

        self.la_results_img = customtkinter.CTkLabel(self.fr_results_img, image=None)
        self.la_results_img.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)


        #
        self.fr_search = customtkinter.CTkFrame(self, corner_radius=0)
        self.fr_search.grid(column=0, row=2,  columnspan=3)

        self.la_search = customtkinter.CTkLabel(self.fr_search, text="Search (ID): ")
        self.la_search.grid(column=0, row=0, padx=self.la_padx, pady=self.la_pady)
        self.tb_search = customtkinter.CTkEntry(self.fr_search)
        self.tb_search.grid(column=1, row=0, padx=self.la_padx, pady=self.la_pady)
        #
        self.fr_nav = customtkinter.CTkFrame(self, corner_radius=0)
        self.fr_nav.grid(row=3, column=0, columnspan=3)

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
            self.exams[self.curr_exam].identifier.confirmed_identifier = self.tb_conf_id_value.get().upper()
        if not len(self.tb_conf_results_id_value.get()) < 1:
            try:
                self.exams[self.curr_exam].result.confirmed =[int (result) for result in self.tb_conf_results_id_value.get().split(",")]
            except ValueError:
                dialog =  tkinter.messagebox.showerror(title="Error", message=r"You are using invalid separator! Try: , (comma)")
        self.refresh()

    def search_exam(self):
        if not len(self.tb_search.get()) < 1:
            isFound = False
            for i in range(len(self.exams)):
                id = self.compareConfirmed(self.exams[i].identifier.original,
                                           self.exams[i].identifier.confirmed_identifier)

                if id == self.tb_search.get().upper():
                    self.curr_exam = i
                    self.refresh()
                    isFound = True
            if isFound == False:
                dialog =  tkinter.messagebox.showinfo(title="Search ID", message="ID not found!")
        else:
            dialog = tkinter.messagebox.showerror(title="Error", message="Prompt in an ID!")
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

        results_str = ""
        for result in results:
            results_str += str(result)+","
        results_str = results_str[:-1]

        self.la_id_value.configure(text=id)
        self.la_results_value.configure(text=results)

        self.tb_conf_id_value.delete(0,100)
        self.tb_conf_id_value.configure(placeholder_text=id)

        self.tb_conf_results_id_value.delete(0, 100)
        self.tb_conf_results_id_value.configure(placeholder_text=results_str)

        img_id_width = 350
        img_id_height = 150
        img_res_width = 750
        img_res_height = 150


        try:
            img_id = customtkinter.CTkImage(light_image=Image.open(f"Data/{self.exams[self.curr_exam].identifier.image}"), size=(img_id_width, img_id_height))
            img_res = customtkinter.CTkImage(light_image=Image.open(f"Data/{self.exams[self.curr_exam].result.image}"), size=(img_res_width, img_res_height))

            self.la_id_img.configure(text="", image=img_id, height=img_id_height, width=img_id_width)
            self.la_results_img.configure(text="", image=img_res, height=img_res_height, width=img_res_width)
        except FileNotFoundError:
                self.la_id_img.configure(text="Image not found!", image="")         # Setting image to None cause error in tkinter :(
                self.la_results_img.configure(text="Image not found!", image="")
