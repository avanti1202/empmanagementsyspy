#Importing packages, modules
from tkinter import Tk , ttk
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter.messagebox import askokcancel
from sqlite3 import *
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import requests
import csv
import re

def addback():
   mw.deiconify()
   aw.withdraw()

def viewback():
   mw.deiconify()
   vw.withdraw()

def updateback():
   mw.deiconify()
   uw.withdraw()

def deleteback():
   mw.deiconify()
   dw.withdraw()

def addpage():
   aw.deiconify()
   mw.withdraw()

def updatepage():
   uw.deiconify()
   mw.withdraw()

def deletepage():
   dw.deiconify()
   mw.withdraw()

def mainback():
   root.deiconify()
   mw.withdraw()
      
#Root Window
   
#Login Window for Manager
root = Tk()
root.geometry("750x650+400+100")
root.title("Employee Management System By Avanti")
root.configure(bg = "#FFF0DB")
f = ("Arial",20, "bold")
root.resizable(height = FALSE, width =FALSE)

#Top frame
top = Frame(root, width=750, height=85, bg= "#FF7F50")
top.grid(row=0, column=0)

icon = Image.open('C:/internship/mira/Python/task4/p4_empms/images/download.png')
icon = icon.resize((90, 90))
icon= ImageTk.PhotoImage(icon)

app_name = Label(top, image= icon, compound=LEFT, text=" Employee Management System",  height = 4, padx =30,pady =35, anchor = CENTER, font = f , bg = "#FF7F50", fg = "black" )
app_name.place(x=70, y=8)

#Main frame
root1 = Frame(root, width=700, height=565, bg= "#FFF0DB")
root1.grid(row=1, column=0)
f1 =("Helvetica", 25, "bold")
f3 =("Helvetica", 22, "bold")

lab_adm = Label(root1, text=" Manager Login",font = f1, bg = "black", fg  = "white")
lab_adm.place(x=240, y =10)

lab_email = Label(root1, text = "Enter email", font = f1, bg = "#FFF0DB")
ent_email = Entry(root1, font = f3,  width = 22, relief="solid")
lab_password = Label(root1, text = "Enter password", font = f1,  bg = "#FFF0DB")
ent_password = Entry(root1, font = f3, show="*",  width = 22, relief="solid")

#Login Function
def login():
      passwd = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]+$'
      pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
      email = ent_email.get()
      password = ent_password.get()
      if (email == "") and (password == ""):
         messagebox.showerror("Login Failed", "Please enter all the fields")
      elif (email == ""):
         messagebox.showerror("Login Failed", "Email is empty")
      elif (email.isspace()):
         messagebox.showerror("Login Failed", "Email should not contain only blank spaces")
         ent_email.delete(0, tk.END)
         ent_email.focus()
      elif re.match(r"^\d+$", email):
         messagebox.showerror("Login Failed", "Email should not contain only digits")
         ent_email.delete(0, tk.END)
         ent_email.focus()
         return
      elif re.search(r'~`@_!#$%^&*()<>?/|}{~:;.]"', email):
         messagebox.showerror("Login Failed", "Email should not contain only special characters")
         ent_email.delete(0, tk.END)
         ent_email.focus()
         return
      elif not re.match(pattern, email):
         messagebox.showerror("Login Failed", "Incorrect email format")
         ent_email.delete(0, tk.END)
         ent_email.focus()
         return
      elif (len(email) < 5):
         messagebox.showerror("Login Failed", "Length of email should be atleast 8 characters")
         ent_email.delete(0, tk.END)
         ent_email.focus()
         return
      elif (password == ""):
         messagebox.showerror("Login Failed", "Password is empty")
         ent_password.delete(0, tk.END)
         ent_password.focus()
      elif (password.strip() == ""):
         messagebox.showerror("Login Failed", "Password cannot be blank spaces")
         ent_password.delete(0, tk.END)
         ent_password.focus()
         return
      elif not re.search(passwd, password):
         messagebox.showerror("Login Failed", "Password must contain atleast one alphabet, digit and special character")
         ent_password.delete(0, tk.END)
         ent_password.focus()
         return
      elif (len(password)< 8):
         messagebox.showerror("Login Failed", "Length of password should be atleast 8 characters")
         ent_password.delete(0, tk.END)
         ent_password.focus()
         return
      elif (email == "admin1@gmail.com") and (password == "admin@123"):
         messagebox.showinfo("Success!!", "Login Successful")
         mw.deiconify()
         root.withdraw()
         ent_email.delete(0, tk.END)
         ent_password.delete(0, tk.END)
         ent_email.focus()
         return
      else:
           messagebox.showerror("Login Failed", "Invalid Login credentials")
           ent_email.delete(0, tk.END)
           ent_password.delete(0, tk.END)
           ent_email.focus()
           return
btn_login = Button(root1, text = "Login", font = f1, width = 8,bg= "#9B59B6", relief = "solid", command=login)

#Location
url = "https://ipinfo.io/"
res = requests.get(url)
data = res.json()
city_name = data["city"]
lab_loc = Label(root1, text="Location: " + city_name , font = f, bg = "#FFF0DB")

#Temperature
def temp():
   api_key = '3b002e26c02666c071c70fc80c6f9cf0' 
   turl = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
   response = requests.get(turl)      
   data1 = response.json()
   temp = data1["main"]["temp"]
   msg = "Temperature: " + " " + str(temp) + "\u2103"
   lab_temp.config(text = msg)

lab_temp = Label(root1, text="", font = f,bg = "#FFF0DB")
temp()

lab_email.place(x = 250, y = 100)
ent_email.place(x = 200, y = 150)
lab_password.place(x = 250, y = 220)
ent_password.place(x = 200, y = 280)
btn_login.place(x =280, y = 350)
lab_loc.place(x = 20, y =480)
lab_temp.place(x = 380, y =480)

#Main Window for all Buttons
mw = tk.Toplevel(root)
mw.geometry("700x650+400+100")
mw.title("Employee Data Management")
mw.configure(bg = "#82CAFF")
f = ("Arial",25, "bold")
f1 = ("Arial",20, "bold")
mw.resizable(height = FALSE, width =FALSE)

lab_emp =Label(mw,text = "Employee Data Management", font = f1,bg = "black" ,fg = "white")
lab_emp.place(x = 170, y = 20)

# Load images with global scope
global image1, image2, image3
# Load your images using the PhotoImage class
image1 = PhotoImage(file="C:/internship/mira/Python/task4/p4_empms/images/add.png")
image2 = PhotoImage(file="C:/internship/mira/Python/task4/p4_empms/images/view1.png")
image3 = PhotoImage(file="C:/internship/mira/Python/task4/p4_empms/images/update1.png")
image4 = PhotoImage(file="C:/internship/mira/Python/task4/p4_empms/images/delete.png")
image5 = PhotoImage(file="C:/internship/mira/Python/task4/p4_empms/images/charts1.png")

image_width = image1.width()
image_height = image1.height()

#Buttons for data management
btn_add = Button(mw, image=image1, compound="left", relief = "solid",text = "Add Employee ", font = f1, width = 250, height = 60, command = addpage)
btn_add.place(x = 220, y = 70)

#View Details of Employee
def view():
	vw.deiconify()
	mw.withdraw()
	vw_emp_data.delete(1.0, END)
		
	con = None
	try:
				con = connect("ems.db")
				cursor = con.cursor()
				sql = "select * from employees"
				cursor.execute(sql)
				data = cursor.fetchall()
				info = ""
				for d in data:
						info += "Id = " + str(d[0])  + "\n"
						info += "Name = " + str(d[1])  + "\n"
						info += "Salary = " + str(d[2]) + "\n"
						info +=  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" + "\n"
				vw_emp_data.insert(INSERT, info)
	except Exception as e:
			con.rollback()
			messagebox.showerror("Issue", e)
	finally:
			if con is not None:
				con.close()
                
btn_view = Button(mw, image = image2, compound="left", relief = "solid",text = "View Employee", font = f1, width = 270, height = 60 ,command = view)
btn_view.place(x = 210, y = 160)
btn_update = Button(mw, image = image3, compound="left", relief = "solid", text = "Update Employee", font = f1, width = 285, height = 60 , command = updatepage)
btn_update.place(x = 210, y = 250)
btn_delete = Button(mw, image = image4, compound="left",relief = "solid", text = "Delete Employee", font = f1, width = 295, height = 60, command = deletepage)
btn_delete.place(x = 210, y = 340)

#Chart to display top 5 highest salaried employees
def bar_plot():
   conn = sqlite3.connect('ems.db')
   cursor = conn.cursor()

# Retrieve data from the database
   cursor.execute("SELECT name, salary FROM employees")
   data = cursor.fetchall()

# Sort data based on salary
   data.sort(key=lambda x: x[1], reverse=True)
   top_5 = data[:5]

   with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])  # Header
    writer.writerows(top_5)

# Plotting
   names = [emp[0] for emp in top_5]
   salaries = [emp[1] for emp in top_5]
   colors = ['yellow', 'orange', 'green','purple', 'brown']
   plt.subplots(figsize=(8, 6)) 
   plt.bar(names, salaries, color=colors)
   plt.xlabel('Employee Name',  fontsize=15, fontweight='bold', color = "red")
   plt.ylabel('Salary', fontsize=15, fontweight='bold', color = "red")
   plt.title('Top 5 Employees with Highest Salary', fontsize=18, fontweight='bold', color = "purple")
   plt.xticks(rotation=0)
   plt.tight_layout()
   plt.show()
   conn.close()

btn_charts = Button(mw, image = image5,compound="left", relief = "solid",text = "Chart", font = f1,width = 270, height = 75 , command = bar_plot)
btn_charts.place(x = 210, y = 430)
btn_back = Button(mw, text = "Back", font = f1,relief = "solid",bg ="#2B60DE",fg = "white", width = 8 ,height = 1, command = mainback)
btn_back.place(x =280, y = 550)
mw.withdraw()

# Add Employee Window
aw= Tk()
aw.geometry("700x650+400+100")
aw.title("Add Employee Details")
aw.configure(bg = "#A0D6B4")
f = ("Arial",25, "bold")
aw.resizable(height = FALSE, width =FALSE)

lab_add = Label(aw, text = "Add Employee Details", bg = "black", fg = "white", font = f)
lab_add.place(x = 210, y = 20)
lab_empid = Label(aw, text = "Enter id", font = f, bg = "#A0D6B4")
lab_empid.place(x = 300, y = 80)
ent_empid = Entry(aw, font = f)
ent_empid.place(x = 180, y = 140)
lab_empname = Label(aw, text = "Enter name", font = f, bg = "#A0D6B4")
lab_empname.place(x = 280, y = 220)
ent_empname = Entry(aw, font = f)
ent_empname.place(x = 180, y = 280)
lab_empsalary = Label(aw, text = "Enter salary", font = f, bg = "#A0D6B4")
lab_empsalary.place(x = 280, y = 360)
ent_empsalary = Entry(aw, font = f)
ent_empsalary.place(x = 180, y = 420)

#Save Enquiries
def save():
     con = None
     try:
      id = ent_empid.get()
      name = ent_empname.get()
      salary = ent_empsalary.get()

      if ((id == "") and (name == "") and (salary == "")):
         messagebox.showerror("Error", "Please enter all details") 
         return
      if(id == ""):
         messagebox.showerror("Error" , "Enter Employee ID")
         return
      if(id.isspace()):
         messagebox.showerror("Error" , "Id should not contain blank spaces")
         ent_empid.delete(0, tk.END)
         ent_empid.focus()
         return
      if id.isalpha():
         messagebox.showerror("Error" , "Id should not contain alphabets")
         ent_empid.delete(0, tk.END)
         ent_empid.focus()
         return
      if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", id):
         messagebox.showerror("Error" , "Id should not contain special characters")
         ent_empid.delete(0, tk.END)
         ent_empid.focus()
         return
      id = int(ent_empid.get())
      if (id < 1):
         messagebox.showerror("Error" , "Id cannot be zero or negative")
         ent_empid.delete(0, tk.END)
         ent_empid.focus()
         return
      if (id < 101 or id > 500):
         messagebox.showerror("Error" , "Emp Id should be between 101 to 500")
         ent_empid.delete(0, tk.END)
         ent_empid.focus()
         return
      if(name == ""):
         messagebox.showerror("Error" , "Name is empty")
         return
      if(name.isspace()):
         messagebox.showerror("Error" , "Name should not contain spaces")
         ent_empname.delete(0, tk.END)
         ent_empname.focus()
         return
      if (len(name) < 2):
         messagebox.showerror("Error" , "Name should contain atleast 2 letters")
         ent_empname.delete(0, tk.END)
         ent_empname.focus()
         return
      if name.isdigit():
         messagebox.showerror("Error" , "Name should not contain numbers")
         ent_empname.delete(0, tk.END)
         ent_empname.focus()
         return
      if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", name):
         messagebox.showerror("Error" , "Name should not contain special characters")
         ent_empname.delete(0, tk.END)
         ent_empname.focus()
         return
      if (salary == ""):
         messagebox.showerror("Error", "Salary is empty")
         ent_empsalary.delete(0, tk.END)
         ent_empsalary.focus()
         return
      if (salary.isspace()):
         messagebox.showerror("Error" , "Salary should not contain only blank spaces")
         ent_empsalary.delete(0, tk.END)
         ent_empsalary.focus()
         return
      if salary.isalpha():
         messagebox.showerror("Error" , "Salary should not contain alphabets")
         ent_empsalary.delete(0, tk.END)
         ent_empsalary.focus()
         return
      if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", salary):
         messagebox.showerror("Error" , "Salary should not contain special characters")
         ent_empsalary.delete(0, tk.END)
         ent_empsalary.focus()
         return
      salary = int(ent_empsalary.get())
      if (salary <= 0):
         messagebox.showerror("Error" , "Salary cannot be negative")
         ent_empsalary.delete(0, tk.END)
         ent_empsalary.focus()
         return
      if (salary < 10000 or salary > 300000):
         messagebox.showerror("Error" , "Salary should be between 10,000 and 3,00,000")
         ent_empsalary.delete(0, tk.END)
         ent_empsalary.focus()
         return
      
      else:
           con = connect("ems.db")
           cursor = con.cursor()
           cursor.execute('select * from employees where id = ?', (id, ))
           existing_user = cursor.fetchone()

           if existing_user:
            messagebox.showerror("Error", "Employee of this ID already exists. Please enter a different ID.")
            ent_empid.delete(0, END)
            ent_empid.focus()
           else:
            sql = "insert into employees values('%s', '%s', '%s')"
            cursor.execute(sql % (id, name, salary) )
            con.commit()
            with open('data.csv', mode='a', newline='') as file:
                 writer = csv.writer(file)
                 writer.writerow([name, salary])
            messagebox.showinfo("Success", "Employee details saved")
            ent_empid.delete(0, END)
            ent_empname.delete(0, END)
            ent_empsalary.delete(0, END)
            ent_empid.focus()
          
     except Exception as e:
          messagebox.showerror("Issue", e)
          con.rollback()
         
     finally:
         if con is not None:
             con.close()

btn_save = Button(aw, text = "Save", width = 6,font = f,bg = "#006A4E", fg = "white",relief="solid", command = save)
btn_save.place(x = 200, y = 530)
aw_btn_back = Button(aw, text = "Back", width = 6, bg = "#6AA121",fg = "white",font = f, relief="solid",command = addback)
aw_btn_back.place(x = 400, y = 530)
aw.withdraw()

#View Employee Window              
vw= Tk()
vw.geometry("700x650+400+100")
vw.title("View Employee Details")
vw.configure(bg = "#EDE275")
f2 = ("Arial",22, "bold")
vw.resizable(height = FALSE, width =FALSE)
lab_view= Label(vw, font = f2, text = "View Employee Details", bg = "black", fg = "white")
lab_view.place(x = 220, y = 20)
vw_emp_data =  ScrolledText(vw,relief = "solid", width=38, height=13, font =f2, padx = 10 )
vw_emp_data.place(x=30, y =70)
vw_btn_back = Button(vw, text = "Back", font = f2,bg ="#FBB117", relief="solid",command = viewback)
vw_btn_back.place(x = 300, y = 550)
vw.withdraw()

#Update Window
uw= Tk()
uw.geometry("750x650+400+100")
uw.title("Update Employee Details")
uw.configure(bg = "#FFC0CB")
uw.resizable(height = FALSE, width =FALSE)

def update():
    try:
        id = (uw_ent_empid.get())
        name = uw_ent_empname.get()
        salary = (uw_ent_empsalary.get())
        if ((id == "") and (name == "") and (salary == "")):
            messagebox.showerror("Error", "Please enter all details") 
            return
        if(id == ""):
            messagebox.showerror("Error" , "Enter Employee ID")
            return
        if(id.isspace()):
            messagebox.showerror("Error" , "Id should not contain blank spaces")
            uw_ent_empid.delete(0, tk.END)
            uw_ent_empid.focus()
            return
        if id.isalpha():
            messagebox.showerror("Error" , "Id should not contain alphabets")
            uw_ent_empid.delete(0, tk.END)
            uw_ent_empid.focus()
            return
        if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", id):
            messagebox.showerror("Error" , "Id should not contain special characters")
            uw_ent_empid.delete(0, tk.END)
            uw_ent_empid.focus()
            return
        id = int(uw_ent_empid.get())
        if (id < 1):
            messagebox.showerror("Error" , "Id cannot be zero or negative")
            uw_ent_empid.delete(0, tk.END)
            uw_ent_empid.focus()
            return
        if(name == ""):
            messagebox.showerror("Error" , "Name is empty")
            return
        if(name.isspace()):
            messagebox.showerror("Error" , "Name should not contain spaces")
            uw_ent_empname.delete(0, tk.END)
            uw_ent_empname.focus()
            return
        if (len(name) < 2):
            messagebox.showerror("Error" , "Name should contain atleast 2 letters")
            uw_ent_empname.delete(0, tk.END)
            uw_ent_empname.focus()
            return
        if name.isdigit():
            messagebox.showerror("Error" , "Name should not contain numbers")
            uw_ent_empname.delete(0, tk.END)
            uw_ent_empname.focus()
            return
        if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", name):
            messagebox.showerror("Error" , "Name should not contain special characters")
            uw_ent_empname.delete(0, tk.END)
            uw_ent_empname.focus_set()
            return
        if (salary == ""):
            messagebox.showerror("Error", "Salary is empty")
            uw_ent_empsalary.delete(0, tk.END)
            uw_ent_empsalary.focus()
            return
        if (salary.isspace()):
            messagebox.showerror("Error" , "Salary should not contain only blank spaces")
            uw_ent_empsalary.delete(0, tk.END)
            uw_ent_empsalary.focus()
            return
        if salary.isalpha():
            messagebox.showerror("Error" , "Salary should not contain alphabets")
            uw_ent_empsalary.delete(0, tk.END)
            uw_ent_empsalary.focus()
            return
        if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", salary):
            messagebox.showerror("Error" , "Salary should not contain special characters")
            uw_ent_empsalary.delete(0, tk.END)
            uw_ent_empsalary.focus()
            return
        salary = int(uw_ent_empsalary.get())
        if (salary <= 0):
            messagebox.showerror("Error" , "Salary cannot be negative")
            uw_ent_empsalary.delete(0, tk.END)
            uw_ent_empsalary.focus()
            return
        if (salary < 10000 or salary > 300000):
            messagebox.showerror("Error" , "Salary should be between 10,000 and 3,00,000")
            uw_ent_empsalary.delete(0, tk.END)
            uw_ent_empsalary.focus_set()
            return
        else:
            connection = sqlite3.connect("ems.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
            existing_employee = cursor.fetchone()

            if existing_employee:
            # Employee exists, update the record
                cursor.execute("UPDATE employees SET name=?, salary=? WHERE id=?",
                           (name, salary, id))
                connection.commit()
                messagebox.showinfo("Success", f"Employee with ID {id} updated successfully.")
                uw_ent_empid.delete(0, tk.END)
                uw_ent_empname.delete(0, tk.END)
                uw_ent_empsalary.delete(0, tk.END)
                uw_ent_empid.focus()
            else:
                messagebox.showerror("Error",f"Employee with ID {id} does not exist.")
                uw_ent_empid.delete(0, tk.END)
                uw_ent_empid.focus()

    except sqlite3.Error as e:
        messagebox.showerror(f"Error updating employee record: {e}")

    finally:
        connection.close()

lab_update = Label(uw, text = "Update Employee Details",font = f, bg = "black", fg = "white")
lab_update.place(x = 200, y = 20)
uw_lab_empid = Label(uw, text = "Enter id", font = f, bg = "#FFC0CB")
uw_lab_empid.place(x = 300, y = 100)
uw_ent_empid = Entry(uw, font = f)
uw_ent_empid.place(x = 200, y = 160)
uw_lab_empname = Label(uw, text = "Enter name", font = f,bg="#FFC0CB")
uw_lab_empname.place(x = 280, y = 220)
uw_ent_empname = Entry(uw, font = f)
uw_ent_empname.place(x = 200, y = 280)
uw_lab_empsalary = Label(uw, text = "Enter salary", font = f, bg="#FFC0CB")
uw_lab_empsalary.place(x = 280, y = 360)
uw_ent_empsalary = Entry(uw, font = f)
uw_ent_empsalary.place(x = 200, y = 420)

btn_update = Button(uw, text = "Update", bg = "#C25283", fg = "white", relief="solid",font = f, command = update)
btn_update.place(x = 180, y = 520)
uw_btn_back = Button(uw, text = "Back", font = f, bg = "#C25283",fg = "white",relief= "solid", command = updateback)
uw_btn_back.place(x = 420, y = 520)
uw.withdraw()

#Delete Employee Window
dw= Tk()
dw.geometry("700x650+400+100")
dw.title("Delete Employee Details")
dw.configure(bg = "#F6C6BD")
dw.resizable(height = FALSE, width =FALSE)

lab_delete= Label(dw, text = "Delete Employee Details",font = f, bg = "black", fg = "white")
lab_delete.place(x = 180, y = 20)
dw_lab_empid = Label(dw, text = "Enter id", bg = "#F6C6BD", font = f)
dw_lab_empid.place(x = 300, y = 100)
dw_ent_empid = Entry(dw, font = f)
dw_ent_empid.place(x = 200, y = 160)

#Delete 
def delete():
   con = None
   try:
      con =connect("ems.db")
      cursor = con.cursor()
      id = dw_ent_empid.get()
      if (id == ""):
         messagebox.showerror("Error" , "Id is empty")
         return
      elif (id.isspace()):
         messagebox.showerror("Error" , "Emp ID should not contain blank spaces")
         dw_ent_empid.delete(0, tk.END)
         dw_ent_empid.focus()
         return
      elif id.isalpha():
         messagebox.showerror("Error" , "Id should not contain alphabets")
         dw_ent_empid.delete(0, tk.END)
         dw_ent_empid.focus()
         return
      elif re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", id):
         messagebox.showerror("Error" , "Id should not contain special characters")
         dw_ent_empid.delete(0, tk.END)
         dw_ent_empid.focus()
         return
      id = int(dw_ent_empid.get())
      if (id <= 0 ):
         messagebox.showerror("Error" , "Id cannot be zero or negative")
         dw_ent_empid.delete(0, tk.END)
         dw_ent_empid.focus_set()
         return
      
      else:
         sql = "delete from employees where id = '%d' "
         cursor.execute(sql % (id))
         if cursor.rowcount == 1:
            con.commit()
            messagebox.showinfo("Success", "Employee record deleted successfully!!")
            dw_ent_empid.delete(0, tk.END)
            dw_ent_empid.focus()
         else:
            messagebox.showerror("Error", "Employee record for this ID does not exists")
            dw_ent_empid.delete(0, tk.END)
            dw_ent_empid.focus()
            return

   except Exception as e:
      con.rollback()
      messagebox.showerror("Issue ", e)
   finally:
        if con is not None:
             con.close()

btn_delete = Button(dw, text = "Delete", bg = "#C11B17",width=6, fg = "white",relief="solid",font = f, command = delete)
btn_delete.place(x = 300, y = 260)
dw_btn_back = Button(dw, text = "Back", bg = "#C11B17",font = f,fg = "white",relief="solid", width= 6, command = deleteback)
dw_btn_back.place(x = 300, y = 360)
dw.withdraw()

#Closing Window
def on_closing():
   if askokcancel("Close",  "Do you want to exit?"):
      root.destroy()
      mw.destroy()
      aw.destroy()
      vw.destroy()
      uw.destroy()
      dw.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)
aw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
uw.protocol("WM_DELETE_WINDOW", on_closing)
dw.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()