import tkinter as tkint
class Application(tkint.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.test_button = tkint.Button(self)
        self.test_button["text"] = "Test a basic button"
        self.test_button["command"] = self.print_test
        self.test_button.pack(side="top")

        self.quit = tkint.Button(self, text="Exit", fg="blue", command=root.destroy)
        self.quit.pack(side="bottom")

    def print_test(self):
        print("Testing the button")

root = tkint.Tk()
application = Application(master=root)
application.mainloop()