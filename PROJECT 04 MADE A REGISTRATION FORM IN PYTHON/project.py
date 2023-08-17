            #   TKINTER FONT

            #  IT IS USED FOR STYLING AND DISPLAYING TEXT OR SIZE.


from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals(): 
    print("You have just submitted the form thanks!")
        #   HEADING
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row = 0,column = 3)
        #   FIELD NAME
name = Label(root,   text="Name")
phone = Label(root,  text="Phone")
gender = Label(root, text="Gender")
email = Label(root,  text="Email")
age = Label(root,    text="Age")
        #   PACKING FIELDS
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)
age.grid(row=5,column=2)
        #   VARIABLE FOR STORING DATA
namevalue   = StringVar
phonevalue  = StringVar    
gendervalue = StringVar
emailvalue  = StringVar
agevalue    = StringVar
checkvalue  =  IntVar
        #   CREATING ENTRY FIELD 
nameentry =Entry(root,  textvariable=namevalue) 
phoneentry =Entry(root, textvariable=phonevalue) 
genderentry =Entry(root, textvariable=phonevalue) 
emailentry =Entry(root, textvariable=emailvalue) 
ageentry =Entry(root,   textvariable=agevalue) 
       #   PACKING ENTRY FIELDS 
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emailentry.grid(row=4,column=3)
ageentry.grid(row=5,  column=3)    
      #   CREATING CHECKBOX
checkbtn = Checkbutton(text="remeber me?", variable=checkvalue)
checkbtn.grid(row=6,column=3)      
      #  SUBMIT BUTTON
Button(text="Submit", command=getvals).grid(row=7,column=3)      


root.mainloop()