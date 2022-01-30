from encrypt_decrypt import encrypt_message,decrypt_message

from properties import *
from tkinter import *
class User2:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Cipher-Chat")
        self.root.resizable(0,0)
        self.root.geometry("410x490+750+250")
        self.root.config(bg="#039dfc")
        self.header = Label(self.root, text= "User 2",font=HEADER, bg= BACKGROUND_COLOR).place(x= 180, y = 10)
        self.send_message = Label(self.root,text="Send Message",font=HEADER,bg=BACKGROUND_COLOR)
        self.send_message.place(x=20,y=70)
        self.send_message_input = Entry(self.root,font=LABEL_FONT,relief=FLAT,borderwidth=5,width=32)
        self.send_message_input.place(x=20,y=120)

        self.send_button = Button(self.root,text="Send",font=BUTTON_FONT,bg=BUTTON_COLOR,fg="WHITE",relief=FLAT, padx=12,command=self.encryption).place(x=70,y=170)
        self.send_message_value = StringVar()
        self.recieved_message = Label(self.root,text="Recieved Message",font=HEADER,bg=BACKGROUND_COLOR)
        self.recieved_message.place(x=20,y=210)
        self.recieved_message_box = Text(self.root,width=45,height=8, relief=FLAT)
        self.recieved_message_box.place(x=20, y = 260)

        self.recieve_button = Button(self.root,text="Recieve",font=BUTTON_FONT,bg=BUTTON_COLOR,fg="WHITE",relief=FLAT, padx=12,command=self.decrypt).place(x=70,y=415)


    def encryption(self):
        msg = self.send_message_input.get().strip()

        with open('message_from_user2.txt','wb') as file:
            encodede_message = encrypt_message(msg)
            file.write(encodede_message)

        print("Encrypted Message Sent")

    def decrypt(self):
        self.file = decrypt_message((open('message_from_user1.txt').read()).encode())
        self.recieved_message_box.delete("1.0",END)
        self.recieved_message_box.insert("1.0",self.file)



    def start(self):
        self.root.mainloop()



        