from tkinter import *
ventana = Tk()
ventana.title("Calculadora sencilla")
ventana.geometry("400x400")

num1=Entry(ventana, font=('times new roman',20,'bold'),width=25,bd=20,insertwidth=4,bg="#b3b6b7", justify="left").place(x=15,y=65)
num2=Entry(ventana, font=('times new roman',20,'bold'),width=25,bd=20,insertwidth=4,bg="#b3b6b7", justify="left").place(x=15,y=65)