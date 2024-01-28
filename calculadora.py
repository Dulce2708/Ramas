from tkinter import *
ventana = Tk()
ventana.title("Calculadora sencilla")
ventana.geometry("400x350")

#Cajas de texto para ingresar los numeros que se van a operar
num1=Entry(ventana, font=('times new roman',20,'bold'),width=25,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=50)
num2=Entry(ventana, font=('times new roman',20,'bold'),width=25,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=100)

Boton_suma=Button(ventana,text="Sumar",width=11,height=3,font=('arial black',10,'bold'),bg="#663333").place(x=60,y=180)
#Boton_resta=Button(ventana, text="Restar", width=11,height=3).place(x=60,y=180)
#Boton_multiplica=Button(ventana, text="Multiplicar", width=11,height=3).place(x=-20,y=180)
#Boton_divide=Button(ventana, text="Dividir", width=11,height=3).place(x=-60,y=180)
