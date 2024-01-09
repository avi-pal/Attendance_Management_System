from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
       
        #first image
        img=Image.open("./college_images/face-recognition.png")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open("./college_images/facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=500,height=130)

        #third image
        img2=Image.open("./college_images/iStock-182059956_18390_t12.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1040,y=0,width=500,height=130)

        #background image
        img3=Image.open("./college_images/bg1.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1500,height=600)
        #main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame 
         
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)
        #Left_frame.place(x=10,y=10,width=760,height=580)
        

        img_left=Image.open("./college_images/AdobeStock_303989091.jpeg")
        img_left=img_left.resize((640,130),Image.LANCZOS)
        #img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=35,y=220,width=620,height=130)
      
        #current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course  information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=15,y=130,width=620,height=130)
        #Current_course_frame.place(x=10,y=10,width=760,height=580)

        #DEPARTMENT
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        #COURSE
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label_label.grid(row=0,column=2,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","EE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)


        #Right label frame 
         
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=10,width=660,height=580)
        #Right_frame.place(x=78,y=10,width=660,height=580)





if __name__ == "__main__":
 root=Tk()
 obj = Student(root)
 root.mainloop()

