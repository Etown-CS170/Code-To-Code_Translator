import tkinter as tk
from tkinter import ttk
from tkinter import Text
import AI_Response

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        self.title('Code-To-Code Translator')
        self.iconbitmap("./assets/CodeToCodeTranslate.ico")

        # initialize data
        self.languages = ("Select a Language","Python","Java","Javascript","C","C++","C#","PHP","HTML","CSS")

        # set up variable
        self.current_language = tk.StringVar(self)

        # place widgets
        self.place_wigets()

    def place_wigets(self):
        
        # user label
        user_label = ttk.Label(self,  text='User:', font=("Times New Roman", 15))
        user_label.place(x=0, y=0)

        # translation label
        translation_label = ttk.Label(self,  text='Translation:', font=("Times New Roman", 15))
        translation_label.place(x=500,y=0)

        # user text entry
        user_entry = Text(self, height=10, width=60)
        user_entry.place(x=5, y=25)

        # translation text entry
        translation_entry = Text(self, height=10, width=60)
        translation_entry.place(x=500, y=25)
        translation_entry['state'] = 'disabled'

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.current_language,
            self.languages[0],
            *self.languages)
        option_menu.config(width=17)
        option_menu.place(x=0, y=200)

        # clear button
        translate_button = ttk.Button(self, text="Clear")
        translate_button.place(x=10, y=230, width=225, height=30)

        # translate button
        translate_button = ttk.Button(self, text="Translate", command=lambda: self.translate(user_entry, translation_entry))
        translate_button.place(x=250, y=230, width=225, height=30)

        # exit button
        translate_button = ttk.Button(self, text="Exit Program", command=lambda: self.quit())
        translate_button.place(x=10, y=265)
    
    # translate function
    def translate(self, user_text, translation_text):

        # clear output
        translation_text['state'] = 'normal'
        translation_text.delete("1.0", "end")
        translation_text.insert("1.0", "Translation Loading...")
        translation_text['state'] = 'disabled'

        # get response
        if self.current_language.get() != "Select a Language":
            user = str(user_text.get("1.0","end"))
            language = self.current_language.get()
            response = AI_Response.get_response(user, language)
        else:
            response = "Select a Language"
        translation_text['state'] = 'normal'
        translation_text.delete("1.0", "end")
        translation_text.insert("1.0", response)
        translation_text['state'] = 'disabled'

if __name__ == "__main__":
    app = App()
    app.mainloop()