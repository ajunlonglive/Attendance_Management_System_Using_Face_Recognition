from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x700+0+0")
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\VKU\STEM\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
        img=img.resize((1250,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1250,height=120)

        # backgorund image 
        bg1=Image.open(r"D:\VKU\STEM\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1250,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1250,height=768)

        #title section
        title_lb1 = Label(bg_img,text="Developer",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\VKU\STEM\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\phong.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=550,y=180,width=180,height=200)

        att_b1_1 = Button(bg_img,text="Nguyễn Thanh Phong",cursor="hand2",font=("tahoma",10,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=550,y=360,width=180,height=45)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()