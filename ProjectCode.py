"""
File: Term_Project#94844.py
Priyanka Deshmukh-94844[Term Project]

The Below scipt is design and developed for a Gardening/Nursery shop GUI.This will allow you to select different plants(vegetable/Flowrs/Herbs)
for three seasons(Fall,Summer,Spring).It has GUI interface developed with tkinter module of python. MongoDB database is used for interacting with data
Use canvas for showing images. Csv file format is created for storing data and for accessing[CSV file contains data for each selection from database]
Used Version:
Python Version: 3.7.3
MongoDB version: v4.0.10

"""
import tkinter as tk
import tkinter as tk1
from tkinter import *
import tkinter.ttk as tkk
from PIL import ImageTk, Image
from pymongo import MongoClient
import csv
from tkinter import messagebox

"""---------------MongoDb Code Start-------------------------"""
client=MongoClient('mongodb://localhost:27017')
db=client['Term-Project']

"""---------collections of Term-Project database------------"""
s1_veggies = db.s1_veggies
s1_flower  = db.s1_flower
s1_herbs   = db.s1_herbs

s2_veggies = db.s2_veggies
s2_flower  = db.s2_flower
s2_herbs   = db.s2_herbs

s3_veggies = db.s3_veggies
s3_flower  = db.s3_flower
s3_herbs   = db.s3_herbs

"""-------------------Creating Data for collection-----------------"""
s1_v_data = [
  { "_id":1,"name": "Kale", "price": "$12","Condition":"Full Sun-3Hrs, To Harvest-70 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Cabbage", "price": "$20","Condition":"Full Sun-4Hrs, To Harvest-90 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Beets", "price": "$15","Condition":"Full Sun-4Hrs, To Harvest-10 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Garlic", "price": "$22","Condition":"Full Sun-3.5Hrs, To Harvest-50 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Lettuce", "price": "$17","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Fava Bean", "price": "$13","Condition":"Full Sun-1Hrs, To Harvest-25 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Parsely", "price": "$15","Condition":"Full Sun-2Hrs, To Harvest-50 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Spanich", "price": "$14","Condition":"Full Sun-5Hrs, To Harvest-70 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Aurgula", "price": "$10","Condition":"Full Sun-6Hrs, To Harvest-25 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Potato", "price": "$11","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]
s1_f_data = [
  { "_id":1,"name": "Stone Crop", "price": "$14","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Aster", "price": "$27","Condition":"Full Sun-4Hrs, To Harvest-50 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Cone-Flower", "price": "$11","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Day-Lily", "price": "$28","Condition":"Full Sun-3.5Hrs, To Harvest-60 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Russian Sage", "price": "$12","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Black Eye", "price": "$15","Condition":"Full Sun-1Hrs, To Harvest-45 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Yarrows", "price": "$12","Condition":"Full Sun-2Hrs, To Harvest-70 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Crocus", "price": "$10","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Anymone", "price": "$10","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Eryngos", "price": "$18","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]

s1_h_data = [
  { "_id":1,"name": "Sage", "price": "$15","Condition":"Full Sun-3Hrs, To Harvest-30 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Rosemarry", "price": "$23","Condition":"Full Sun-4Hrs, To Harvest-50 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Thyme", "price": "$17","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Cilantro", "price": "$29","Condition":"Full Sun-3.5Hrs, To Harvest-60 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Lavender", "price": "$12","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Mint", "price": "$16","Condition":"Full Sun-1Hrs, To Harvest-45 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Chives", "price": "$12","Condition":"Full Sun-2Hrs, To Harvest-70 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Sweet Mint", "price": "$11","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Corriander", "price": "$19","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Basil", "price": "$15","Condition":"Full Sun-3Hrs, To Harvest-70 days, Height-4ft, Depth-3.5ft"},]

s2_v_data = [
  { "_id":1,"name": "Pepper", "price": "$12","Condition":"Full Sun-3Hrs, To Harvest-40 days, Height-3ft, Depth-3ft"},
  { "_id":2,"name": "Green Bean", "price": "$20","Condition":"Full Sun-4Hrs, To Harvest-70 days, Height-1ft, Depth-2ft"},
  { "_id":3,"name": "Okra", "price": "$15","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "squash", "price": "$22","Condition":"Full Sun-3.5Hrs, To Harvest-80 days, Height-2ft, Depth-1ft"},
  { "_id":5,"name": "Tomato", "price": "$17","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Egg Plant", "price": "$13","Condition":"Full Sun-1Hrs, To Harvest-82 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Carrot", "price": "$15","Condition":"Full Sun-2Hrs, To Harvest-20 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Cucumber", "price": "$14","Condition":"Full Sun-5Hrs, To Harvest-70 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Corn", "price": "$10","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Pumpkin", "price": "$11","Condition":"Full Sun-3Hrs, To Harvest-70 days, Height-4ft, Depth-3.5ft"},]

s2_f_data = [
  { "_id":1,"name": "Marrygold", "price": "$12","Condition":"Full Sun-3Hrs, To Harvest-90 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Perowinkle", "price": "$20","Condition":"Full Sun-4Hrs, To Harvest-20 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Zinnia", "price": "$19","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Impatiens", "price": "$23","Condition":"Full Sun-3.5Hrs, To Harvest-50 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Corn-Flower", "price": "$19","Condition":"Full Sun-5Hrs, To Harvest-30 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Petunia", "price": "$17","Condition":"Full Sun-1Hrs, To Harvest-25 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Nasturtium", "price": "$12","Condition":"Full Sun-2Hrs, To Harvest-50 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Begonia", "price": "$20","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Geranium", "price": "$19","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Vinca", "price": "$12","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]


s2_h_data = [
  { "_id":1,"name": "Oregano", "price": "$15","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Dill", "price": "$28","Condition":"Full Sun-4Hrs, To Harvest-50 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Mint", "price": "$12","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Corriander", "price": "$20","Condition":"Full Sun-3.5Hrs, To Harvest-60 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Tarragon", "price": "$18","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Bay", "price": "$10","Condition":"Full Sun-1Hrs, To Harvest-45 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Culantro", "price": "$11","Condition":"Full Sun-2Hrs, To Harvest-70 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Lemon-Grass", "price": "$12","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "cat-Mint", "price": "$15","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Borage", "price": "$13","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]


s3_v_data = [
  { "_id":1,"name": "Snow-Peas", "price": "$12","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Lettuce", "price": "$20","Condition":"Full Sun-4Hrs, To Harvest-50 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Kale", "price": "$15","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Reddish", "price": "$22","Condition":"Full Sun-3.5Hrs, To Harvest-60 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Broccoli", "price": "$17","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Beets", "price": "$13","Condition":"Full Sun-1Hrs, To Harvest-45 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Arugula", "price": "$15","Condition":"Full Sun-2Hrs, To Harvest-70 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Cauliflower", "price": "$14","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Onion", "price": "$10","Condition":"Full Sun-2.5Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Egg-Plant", "price": "$11","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]



s3_f_data = [
  { "_id":1,"name": "Irises", "price": "$18","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Peony", "price": "$10","Condition":"Full Sun-4Hrs, To Harvest-50 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Daffodil", "price": "$19","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Hyacinth", "price": "$23","Condition":"Full Sun-3.5Hrs, To Harvest-60 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Sage", "price": "$12","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Common-daisy", "price": "$19","Condition":"Full Sun-1Hrs, To Harvest-45 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Crocus", "price": "$13","Condition":"Full Sun-2Hrs, To Harvest-70 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Tulip", "price": "$18","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Phlox", "price": "$13","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Stone-Crop", "price": "$16","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]



s3_h_data = [
  { "_id":1,"name": "Chervil", "price": "$34","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-3ft, Depth-2ft"},
  { "_id":2,"name": "Lime-leaf", "price": "$25","Condition":"Full Sun-4Hrs, To Harvest-50 days, Height-1ft, Depth-1ft"},
  { "_id":3,"name": "Marjoram", "price": "$19","Condition":"Full Sun-4Hrs, To Harvest-30 days, Height-1ft, Depth-2ft"},
  { "_id":4,"name": "Thyme", "price": "$24","Condition":"Full Sun-3.5Hrs, To Harvest-60 days, Height-2ft, Depth-2ft"},
  { "_id":5,"name": "Dill", "price": "$16","Condition":"Full Sun-5Hrs, To Harvest-40 days, Height-1ft, Depth-3ft"},
  { "_id":6,"name": "Chives", "price": "$19","Condition":"Full Sun-1Hrs, To Harvest-45 days, Height-3ft, Depth-1ft"},
  { "_id":7,"name": "Parseley", "price": "$18","Condition":"Full Sun-2Hrs, To Harvest-70 days, Height-2ft, Depth-1.5ft"},
  { "_id":8,"name": "Chamomile", "price": "$18","Condition":"Full Sun-5Hrs, To Harvest-20 days, Height-1ft, Depth-2ft"},
  { "_id":9,"name": "Choclate-Mint", "price": "$15","Condition":"Full Sun-6Hrs, To Harvest-35 days, Height-1.5ft, Depth-2.5ft"},
  { "_id":10,"name": "Mentha-longifolia", "price": "$16","Condition":"Full Sun-3Hrs, To Harvest-60 days, Height-4ft, Depth-3.5ft"},]


"""------------------Inserting data into respective collections-------------------------------"""
"""
Insertion can be done only once. If we run program for second time,this insertion code has to be comment out, because we already inserted data.

"""

#Fall Season
result=s1_veggies.insert_many(s1_v_data)
result=s1_flower.insert_many(s1_f_data)
result=s1_herbs.insert_many(s1_h_data)
#Summer Season
result=s2_veggies.insert_many(s2_v_data)
result=s2_flower.insert_many(s2_f_data)
result=s2_herbs.insert_many(s2_h_data)
#Spring season
result=s3_veggies.insert_many(s3_v_data)
result=s3_flower.insert_many(s3_f_data)
result=s3_herbs.insert_many(s3_h_data)

"""------------------Inserting data END-------------------------------"""

"""----------------------MongoDb Code END------------------------------------------------------"""

def calldb(database):
    database_name=database
    """---------creating CSV file-----------"""
    header = ['Index','Name', 'Price','Condition']

    with open("test.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for index in database_name.find():
            writer.writerow([str(index['_id']),str(index['name']),str(index['price']),str(index['Condition'])])


    output_name = []
    output_price=[]
    output_index=[]
    output_Condition=[]
    """---------Accessing CSV file-----------"""
    f = open( 'test.csv', 'r' ) #open the file in read universal mode
    for line in f:
        cells = line.split( "," )
        #since we want the first, second and third column
        output_index.append(cells[0])
        output_name.append(cells[ 1 ]) 
        output_price.append(cells[2])
        output_Condition.append(cells[3])
    f.close()
    
    def op_1():
    
        messagebox.showinfo("Information","Your Selection is completed.Unfortunately, banking system is not available")
        
    """---------Function display details[price and condition] for user's requested data-----------""" 
    def operation():
        
        data=str(combo.get())
        for index in database_name.find({"name":data}):
            data=str(index['name'])
            data_price=str(index['price'])
            data_Condition=str(index['Condition'])
            
            data=data.replace('[',' ')
            data=data.replace(']',' ')
            
            LB1 = Listbox(window,height=6,bg='light green',width=50)
            LB1.insert(1,data)
            LB1.insert(2,data_price)
            LB1.insert(3,data_Condition)
            LB1.place(x=35,y=100)
            
    window = tk.Toplevel(top)
    window.geometry("400x300")
    window.title("Available plants with all Description")
    window.resizable(False, False)
    
    canv=Canvas(window,width=400,height=300,bg="blue")
    canv.place(x=0,y=0)

    img = ImageTk.PhotoImage(Image.open('image3.jpg'))
    canv.create_image(0,0,image=img,anchor=NW)
    
    combo=tkk.Combobox(window,values=output_name,state="readonly",width=30)
    combo.place(x=30,y=30)
    combo.current(1)

    done=Button(window,text="Submit",width=10,height=1,command=operation)
    done.place(x=250,y=30)

    okay=Button(window,text="Proceed to Payment",width=20,height=1,command=op_1)
    okay.place(x=100,y=250)

    window.mainloop()
    
"""---------------Function display GUI showing for main page-------------------------"""

def press_okay():
    
    
#Fall data
    if combo1.get()=="Fall" and combo2.get()=="Veggies":
        print("you selected veggies from Fall")
        database=s1_veggies
        calldb(database)
        
    if combo1.get()=="Fall" and combo2.get()=="Flower":
        print("you selected Decorative Flower from Fall")
        database=s1_flower
        calldb(database)
            

    if combo1.get()=="Fall" and combo2.get()=="Herbs":
        print("you selected Herbs from Fall")
        database=s1_herbs
        calldb(database)
            
#Summer data
    if combo1.get()=="Summer" and combo2.get()=="Veggies":
        print("you selected veggies from Summer")
        database=s2_veggies
        calldb(database)
            

    if combo1.get()=="Summer" and combo2.get()=="Flower":
        print("you selected Decorative Flower from Summer")
        database=s2_flower
        calldb(database)
            

    if combo1.get()=="Summer" and combo2.get()=="Herbs":
        print("you selected Herbs from Summer")
        database=s2_herbs
        calldb(database)
            
# Spring data
    if combo1.get()=="Spring" and combo2.get()=="Veggies":
        print("you selected veggies from Spring")
        database=s3_veggies
        calldb(database)
            

    if combo1.get()=="Spring" and combo2.get()=="Flower":
        print("you selected Decorative Flower from Spring")
        database=s3_flower
        calldb(database)
            

    if combo1.get()=="Spring" and combo2.get()=="Herbs":
        print("you selected Herbs from Spring")
        database=s3_herbs
        calldb(database)
          

top = tk.Tk()

pad=3
top._geom='200x200+0+0'
top.geometry("{0}x{1}+0+0".format(
top.winfo_screenwidth()-pad, top.winfo_screenheight()-pad))
top.title("TERM-PROJECT(NURSERY)")
top.configure(background='light blue')
top.resizable(False, False)
w=top.winfo_screenwidth()-pad
h=top.winfo_screenheight()-pad


canvas=Canvas(width=w,height=h-50,bg="blue")
canvas.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open('Webp.net-resizeimage.jpg'))
canvas.create_image(0,0,image=img,anchor=NW)

f = Frame(top,bg="yellow",width=1000,height=500)
f.place(x=200,y=80)
f.update()
    
logo = tk.PhotoImage(file="image.gif")
    
L=Label(f,compound = tk.CENTER,text="Welcome to Priyanka's Gardening Shop,\n'we might think we are nurturing our garden but ofcourse its our garden that is really nurturing us'\n-Genny Uglow  ",image=logo,fg="yellow",font = "Helvetica 16 bold italic")
L.place(width=1000,height=120)


L1 = Label( f, text="Here you get full information of your plants according to the season\n Choose your options",width=60,height=3,font = "Helvetica 16 bold italic",bg="light green")
L1.place(x=80,y=170)

combo1 = tkk.Combobox(f, values=["Fall", "Summer", "Spring"],width=60,height=60,state="readonly")
combo1.place(x=400,y=250)
combo1.current(0)

combo2 = tkk.Combobox(f, values=["Veggies", "Flower", "Herbs"],width=60,height=5,state="readonly")
combo2.place(x=400,y=320)
combo2.current(0)

okay=Button(f,text="OKAY",fg="red",command=press_okay,width=10,height=1)
okay.place(x=400,y=390)

    
top.mainloop()

