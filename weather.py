from tkinter import *
import datetime
import requests
from bs4 import BeautifulSoup

# hello manish
#hello gandhi
root=Tk()
city=StringVar()
def temp():
    search="weather in "+city.get()
    url=f"https://www.google.com/search?&q={search}"
    r=requests.get(url)
    s=BeautifulSoup(r.content,'html.parser')
    update=s.find('div',class_="BNeawe")
    Label4.config(text=update.text)

#GUI

root.title("Temprature Check")
root.config(bg="lightblue")
root.geometry('600x500')

Label1=Label(root,text="Know Your city Temprature: ",bg="lightblue",fg="green",font=("normal", 30 ,"bold"))
Label1.place(x=27,y=40)

localtime="Date: "+str(datetime.date.today())+"\nTime: "+datetime.datetime.now().strftime("%H:%M:%S")
Label2=Label(root,text=localtime,bg="lightblue",fg="red",font=("normal", 15 ,"bold"))
Label2.place(x=200,y=100)

Label3=Label(root,text="Enter your city name: ",bg="lightblue",fg="gray",font=("normal", 20 ,"bold"))
Label3.place(x=50,y=200)
entry1=Entry(root,textvariable=city,justify="center",font=("normal", 20 ,"bold"))
entry1.place(x=350,y=200,width=200)

button=Button(root,text="Check Temprature",bg="gray",fg="white",font=("normal", 20 ,"bold"),command=temp)
button.place(x=180,y=270)

Label4=Label(root,bg="lightblue",fg="gray",font=("normal", 30 ,"bold"))
Label4.place(x=280,y=400)

root.mainloop()
