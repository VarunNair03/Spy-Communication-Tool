import time
from user2 import User2
from encrypt_decrypt import encrypt_message,decrypt_message
from properties import *
from tkinter import *
class User1:
    def __init__(self):
        self.root = Tk()
        self.root.title("User 1")
        self.root.resizable(0,0)
        self.root.geometry("410x420+250+250")
        self.root.config(bg="#039dfc")
        self.send_message = Label(self.root,text="Send Message",font=HEADER,bg=BACKGROUND_COLOR)
        self.send_message.place(x=20,y=30)
        self.send_message_input = Entry(self.root,font=LABEL_FONT,relief=FLAT,borderwidth=5,width=32)
        self.send_message_input.place(x=20,y=80)
        self.send_button = Button(self.root,text="Send",font=BUTTON_FONT,bg=BUTTON_COLOR,fg="WHITE",relief=FLAT, padx=12,command=self.encryption_Delay).place(x=70,y=130)

        self.recieved_message = Label(self.root,text="Recieved Message",font=HEADER,bg=BACKGROUND_COLOR)
        self.recieved_message.place(x=20,y=170)
        self.recieved_message_box = Text(self.root,width=45,height=8,padx=5,pady=5,relief=FLAT)
        self.recieved_message_box.place(x=20,y = 220)

        self.recieve_button = Button(self.root,text="Recieve",font=BUTTON_FONT,bg=BUTTON_COLOR,fg="WHITE",relief=FLAT, padx=12,command= self.decrypt).place(x=70,y=370)
        User2().start()

    def encryption_Delay(self):
        self.span.config(text="Encrypting Data: ")
        time.sleep(2)            


        self.span.config(text= "")
        self.encryption()



    def encryption(self):
        msg = self.send_message_input.get().strip()

        with open('message_from_user1.txt','wb') as file:
            encodede_message = encrypt_message(msg)
            file.write(encodede_message)

        print("Encrypted Message Sent")


    def decrypt(self):
        self.file = decrypt_message((open('message_from_user2.txt').read()).encode())
        self.recieved_message_box.delete("1.0",END)
        self.recieved_message_box.insert("1.0",self.file)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    User1().start()
        