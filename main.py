import os
from tkinter import Tk, Menu, Label, Button
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror

from remove_bg import remove_bg

from threading import Thread

IMGPATH = ''


class GUI(object):

    def __init__(self, window):
        self.window = window
        self.window.title('Remove image BG')
        self.window.geometry('300x200')
        menubar = Menu(self.window)

        # define empty menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Help', command=self.helpme)
        filemenu.add_separator()

        # display
        self.l = Label(window, text='')
        self.l.pack(padx=5, pady=10)

        # select pic
        btn1 = Button(window, text='Select photo', width=15,
                      height=2, command=self.get_img)
        btn1.pack()

        # generate pic
        self.send_btn = Button(window, text='Remove BG',
                               width=15, height=2, command=self.gen_img)
        self.send_btn.pack()

    def helpme(self):
        showerror('Help', 'Please contact xin')

    def get_img(self):
        global IMGPATH
        # select file
        filenames = askopenfilenames(filetypes=(
            ("jpep img", "*.jpep"), ("jgp img", "*.jpg"), ("png img", "*.png")))
        if len(filenames) > 0:
            fnlist = [fn for fn in filenames]
            fnstr = '\n'.join(fnlist)
            self.l.config(text=fnstr)
            IMGPATH = fnlist
        else:
            self.l.config(text="you have not selected any pics")

    def gen_img(self):
        global IMGPATH
        respathlist = []
        for imgpath in IMGPATH:
            filepath, tempfilename = os.path.split(imgpath)
            filename, extension = os.path.splitext(tempfilename)
            print(f'filename is {filename}')
            print(f'extension is {extension}')
            thread1 = Thread(target=remove_bg(imgpath),
                             name='remove_bg_thread')
            thread1.start()
            respathlist.append(imgpath)
        respath = ' '.join(respathlist)
        showinfo('finish processing',
                 f'The photos are processed, path is: {respath}')


if __name__ == '__main__':
    # create window
    window = Tk()
    GUI(window)
    # display window
    window.mainloop()
