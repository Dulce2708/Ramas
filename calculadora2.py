from tkinter import *
ventana = Tk()
ventana.title("Calculadora sencilla")
ventana.geometry("400x400")

#Cajas de texto para ingresar los numeros que se van a operar
num1=Entry(ventana, font=('times new roman',20,'bold'),width=25,bd=10,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=50)
num2=Entry(ventana, font=('times new roman',20,'bold'),width=25,bd=10,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=100)

