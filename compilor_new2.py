
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Java Loader")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbar2 = Scrollbar(root, orient='horizontal')
scrollbar2.pack(side=BOTTOM, fill=X)

brackets_list = []
outcasts_list = []

brackets_dict = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

apps = []

textarea = Text(root, width=60, height=30, wrap=NONE, yscrollcommand=scrollbar.set,
                xscrollcommand=scrollbar2.set)
scrollbar.config(command=textarea.yview)
scrollbar2.config(command=textarea.xview)


def checker():
    # an infinite loop
    i = 1
    while True:
        code = str(textarea)
        # looping individual characters for brackets
        for char in code:

            if '{' == char or '(' == char or '[' == char or '<' == char:

                if len(brackets_list) > 0:
                    if brackets_list[-1] == '<' and char != '>':
                        outcasts_list.append(char)

                brackets_list.append(char)

            elif '}' == char or ')' == char or ']' == char or '>' == char:
                if len(brackets_list) > 0:
                    if brackets_dict[brackets_list[-1]] == char:
                        brackets_list.pop()
                    else:
                        outcasts_list.append(char)
                else:
                    outcasts_list.append(char)

        # exit
        if code == '.':
            break

        i += 1
    aspi = "Sorry, brackets not nested correctly..."

    asp = "Brackets are nested correctly, now running the program..."

    if len(brackets_list) == 0 and len(outcasts_list) == 0:
        label2 = Label(root, text=asp, bg="red")
        label2.pack()

    elif len(brackets_list) > 0 or len(outcasts_list) > 0:
        label3 = Label(root, text=aspi, bg="red")
        label3.pack()


def addapp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.java"), ("All Files", "*.*")))
    f = open(filename)
    sa = f.read()
    for line in sa:
        textarea.insert(END, str(line))
    return sa


textarea.pack()


openFile = Button(root, text="Open File", padx=10, pady=5, fg="white", bg="pink", command=addapp)
openFile.pack()

ranApp = Button(root, text="Ran App", padx=10, pady=5, fg="white", bg="pink")
ranApp.pack()

ten = "To Exit, Press ."

label = Label(root, text=ten, bg="red")
label.pack()

label5 = Label(root, text=ten, bg="red")
label5.pack()

ok = Button(root, text="OK", padx=10, pady=1, fg="white", bg="pink", command=checker)
ok.pack()

label4 = Label(root, text="", bg="red")
label4.pack()


root.mainloop()
