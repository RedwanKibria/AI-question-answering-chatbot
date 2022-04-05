from distutils.fancy_getopt import wrap_text
from tkinter import *
from chatbot import get_response, bot_name

BG = "#1E90FF"
TEXT_CLR = "#EAECEE"

FONT = "Calibri 14"
FONT_BOLD = "Calibri 13 bold"


class ui:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("EverKnock")
        self.window.resizable(width=FALSE, height=FALSE)
        self.window.configure(width=510, height=525, bg=BG)

        # head label
        head_lbl = Label(self.window, bg=BG, fg=TEXT_CLR,
                         text="Welcome", font=FONT_BOLD, pady=10)
        head_lbl.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2,
                                bg="#F0FFFF", fg="#000000", font=FONT_BOLD, wrap=WORD, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrlbar = Scrollbar(self.text_widget)
        scrlbar.place(relheight=1, relx=0.974)
        scrlbar.configure(command=self.text_widget.yview)

        # bottom label
        btm_label = Label(self.window, bg=BG, height=60)
        btm_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(btm_label, bg="#F0FFFF",
                               fg="#000000", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_bttn = Button(btm_label, text="Send", font=FONT_BOLD,
                           width=20, bg=BG, command=lambda: self._on_enter_pressed(None))
        send_bttn.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_msg(msg, "You")

    def _insert_msg(self, msg, sndr):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sndr}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ui()
    app.run()
