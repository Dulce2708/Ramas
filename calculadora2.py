from tkinter import *
ventana = Tk()
ventana.configure(background="#330033")
ventana.title("Calculadora sencilla")
ventana.geometry("370x350")

#Cajas de texto para ingresar los numeros que se van a operar
num1=Entry(ventana, font=('times new roman',20,'bold'),width=25,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=15)
num2=Entry(ventana, font=('times new roman',20,'bold'),width=25,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=60)

#Botones para las operaciones básicas
Boton_suma=Button(ventana,text="Sumar",width=13,height=3,font=('arial black',10,'bold'),bg="#99cc00").place(x=30,y=110)
Boton_resta=Button(ventana, text="Restar", width=13,height=3,font=('arial black',10,'bold'),bg="#cc0000").place(x=220,y=110)
Boton_multiplica=Button(ventana, text="Multiplicar", width=13,height=3,font=('arial black',10,'bold'),bg="#003399").place(x=30,y=210)
Boton_divide=Button(ventana, text="Dividir", width=13,height=3,font=('arial black',10,'bold'),bg="#663366").place(x=220,y=210)

num2=Entry(ventana, font=('times new roman',20,'bold'),width=25,insertwidth=4,bg="#b3b6b7", justify="left").place(x=10,y=300)
