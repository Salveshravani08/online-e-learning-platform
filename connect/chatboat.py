import re
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Help ChatBot")
        self.root.geometry("730x620+0+0")

        # Main frame
        main_frame = Frame(self.root, bd=4, bg='violet', width='610')
        main_frame.pack()

        # Chatbot image
        #img_chat = Image.open('chatbot.png')
        img_chat = Image.open(r"C:\Users\Admin\Desktop\online education project\connect\chatbot.png")
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        # Title label
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=700, compound=LEFT, image=self.photoimg, text='Programming Help Bot', font=('arial', 30, 'bold'), fg='blue', bg='white')
        Title_label.pack(side=TOP)

        # Text area
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # Button frame
        btn_frame = Frame(self.root, bd=4, bg='white', width='730')
        btn_frame.pack()

        label = Label(btn_frame, text="Ask a Question", font=('arial', 14, 'bold'), fg='black', bg='violet')
        label.grid(row=0, column=0, padx=8, sticky=W)

        # Entry box
        self.entry = ttk.Entry(btn_frame, width=40, font=('times new roman', 16, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 16, 'bold'), width=8, bg='violet')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Chat", font=('arial', 17, 'bold'), width=8, bg='violet', fg='black', command=self.clear_chat)
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_1 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='black', bg='white')
        self.label_1.grid(row=1, column=1, padx=8, sticky=W)

    # Function to send user input and bot response
    def send(self):
        user_input = self.entry.get()
        send_message = '\t\t\t\t\t\t\t\t' + ' You: ' + user_input
        self.text.insert(END, '\n' + send_message)

        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_1.config(text=self.msg, fg='black')
        else:
            self.msg = ''
            self.label_1.config(text=self.msg, fg='black')  

        bot_response = self.get_bot_response(user_input)
        self.text.insert(END, '\n\n' + 'Bot: ' + bot_response)
        self.text.yview(END)  # Scroll to the bottom of the chat

        # Clear entry field after sending
        self.entry.delete(0, END)

    # Function to generate bot responses based on predefined questions and answers
    def get_bot_response(self, user_input):
        predefined_answers = {
            "hey": "Hey, how can I help you!",
        
        # HTML Related
        "html": "HTML stands for Hypertext Markup Language. It is the standard language for creating webpages.",
        "what is html?": "HTML is the standard markup language for creating web pages and web applications.",
        "html tags": "HTML tags are the building blocks of HTML. Examples include <div>, <p>, <h1>, etc.",
        "html5": "HTML5 is the latest version of HTML. It includes new elements like <section>, <article>, <nav>, etc.",

        # CSS Related
        "css": "CSS stands for Cascading Style Sheets. It is used to style HTML elements.",
        "what is css?": "CSS is a style sheet language used for describing the presentation of a document written in HTML or XML.",
        "css flexbox": "Flexbox is a layout model in CSS that allows items to be aligned and distributed in a container even when their size is unknown.",
        "css grid": "CSS Grid Layout is a two-dimensional layout system for the web. It allows you to create complex layouts with rows and columns.",

        # JavaScript Related
        "javascript": "JavaScript is a programming language used to make webpages interactive.",
        "what is javascript?": "JavaScript is a high-level, interpreted programming language that is used for creating dynamic and interactive web pages.",
        "javascript functions": "A function in JavaScript is a block of code designed to perform a particular task when called.",
        "javascript events": "JavaScript events are actions that occur in the system, such as clicks, mouse movements, key presses, etc., which can trigger specific functions.",
        "javascript promises": "A Promise is an object in JavaScript that represents the eventual completion (or failure) of an asynchronous operation.",

        # C Related
        "c": "C is a general-purpose programming language that is widely used for system software and embedded systems.",
        "what is c?": "C is a powerful general-purpose programming language. It was originally developed for system software and applications requiring high performance.",
        "c pointers": "A pointer in C is a variable that stores the memory address of another variable.",
        "c structures": "In C, a structure is a user-defined data type that allows grouping of variables of different data types.",

        # C++ Related
        "c++": "C++ is an extension of the C programming language. It is used for object-oriented programming.",
        "what is c++?": "C++ is a high-level, compiled programming language that includes object-oriented, imperative, and generic programming features.",
        "c++ inheritance": "Inheritance is an OOP concept where one class can inherit the properties and methods of another class in C++.",
        "c++ classes": "A class in C++ is a user-defined data type that contains variables and functions that operate on them.",

        # Python Related
        "python": "Python is a high-level programming language known for its readability and ease of use. It is used for web development, data analysis, and more.",
        "what is python?": "Python is an interpreted, high-level, and general-purpose programming language. It's known for its simplicity and versatility.",
        "python functions": "Functions in Python are blocks of reusable code that perform a specific task when called.",
        "python classes": "A class in Python is a blueprint for creating objects that contain attributes and methods.",
        "python libraries": "Python libraries are collections of pre-written code that make it easier to perform various tasks, like NumPy for data analysis, or Django for web development.",
        }
        # Clean the user input for better matching
        user_input = user_input.strip().lower()

        # Search for matching keywords in the user input
        for keyword, answer in predefined_answers.items():
            # Use regular expression for a case-insensitive match of keywords in the user input
            if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
                return answer

        return "Sorry, I don't have an answer for that. Try asking another question!"

    # Function to clear the chat
    def clear_chat(self):
        self.text.delete(1.0, END)
        self.entry.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()