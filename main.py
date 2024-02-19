from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfMerger

pdf = PdfMerger()
window = Tk()
text = Text(window, height=250, width=250)
files = []


def open_file():
    name = filedialog.askopenfilename()
    if name != '' and name not in files:
        text.insert(END, name)
        files.append(name)


def merge_files():
    for f in files:
        pdf.append(f)
    with open("result.pdf", "wb") as new_file:  # write binary
        pdf.write(new_file)


if __name__ == '__main__':
    window.wm_minsize(300, 300)
    window.wm_maxsize(300, 300)
    window.wm_title("PDF Merger")

    button = Button(text="Select PDF", command=open_file)
    button.pack()

    button_merge = Button(text="Merge PDF", command=merge_files)
    button_merge.pack()

    text.pack()
    window.mainloop()