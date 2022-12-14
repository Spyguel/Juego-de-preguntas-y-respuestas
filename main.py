from tkinter import Label, Button, Radiobutton, Frame, Tk, BOTTOM, TOP, StringVar, Entry, IntVar, LEFT
from tkinter import messagebox
from PIL import ImageTk, Image
import time

nombre = '' # Variable global para asignar el nombre
score = 0
contador = 3

def window():

    global score
    score = 0
    global contador
    contador = 3

    def exit():
        exit = messagebox.askyesno('Salir', '¿Desea salir del programa?')
        if exit == True:
            root.destroy()
        else:
            True
    #*******************************************************************************

    def beginning():
        beginning = messagebox.askyesno('Inicio', '¿Desea volver al Inicio?')
        if beginning == True:
            root.destroy()
            time.sleep(0.8)
            window()
        else:
            True
    #*******************************************************************************


    root = Tk()
    root.geometry("1180x550")
    root.title ("Juego - preguntas y respuestas")
    root.iconbitmap("icono.ico")
    root.resizable(0,0)
    root.configure(bg='#c0c0c0')
    image = Image.open("start_windows.png")
    image = image.resize((80,30), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    
    Frame(root, bg= '#000082', width= 1180, height= 50).pack(side=TOP)
    Frame(root, bg= '#000082', width= 1180, height= 50).pack(side=BOTTOM)
    Button(root, image= image, bg= '#000082',activebackground='#909090', command= lambda:beginning()).place(x=5, y=8, width=80, height=29)
    Button(root, text='shut down', bg='#c3c3c3',activebackground='#909090', font='mssans, 11', command=lambda:exit()).place(x=1085, y=10, width=90, height=29)
    bienvenida()
    root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def bienvenida():

    def comprobar():
        if not nombre.get():
            messagebox.showerror('Error', 'No ingresó ningún nombre')
        else:
            frame.destroy()

            preg_1()

    frame = Frame(width= 1180, height= 450, bg='#c0c0c0')
    frame.pack()
    global nombre
    nombre = StringVar()
    Label(frame,text=f'Bienvenido al juego de preguntas y respuestas\nHecho por Agustin Perez Di Santi',font='mssans, 14', bg='#c0c0c0').place(x=400,y=20)

    image = Image.open("wallpaper.png")
    image = image.resize((400,250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=400, y=100)

    Label(frame, text='Ingresa tu nombre por favor',font='mssans, 14', bg='#c0c0c0').place(x=485, y=360)
    Entry(frame, textvariable= nombre).place(x=500, y= 400)
    Button(frame, text='Continuar',font='mssans, 11',bg='#c3c3c3',activebackground='#909090', command=lambda:comprobar()).place(x= 650, y= 396,width= 80, height= 29)
    frame.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                           ******* INICIO DE LAS PREGUNTAS *******

# PREGUNTA 1 *******************************

def preg_1():

    def respuesta():
        if x.get() == 3:
            scores()
            frame.destroy()
            resp_1()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la A :(')               
                frame.destroy()
                print(contador)
                preg_2()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) MARK 1', ') Atari ST', 'C) Amstrad CPC', 'D) IMB 360']

    Label(frame, text= "¿Cuál fue el primer ordenador de circuitos integrados?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=435, y= 50)

    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=435, y=330)
    
    frame.mainloop()

def resp_1():

    def delete():
        frame.destroy()
        preg_2()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    Label(frame, text= f"Correcto!! \nEl IBM 360 fue unos de los primeros ordenadores comerciales que utilizó circuitos integrados. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("ibm360.png")
    image = image.resize((400,250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)

    frame.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# PREGUNTA 2 *******************************

def preg_2():
    global contador
    contador = 3

    def respuesta():
        if x.get() == 1:
            scores()
            frame.destroy()
            resp_2()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la B :(')
                #contador = 3
                frame.destroy()
                preg_3()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) 1968', 'B) 1971', 'C) 1980', 'D) 1976']

    Label(frame, text= "¿En qué año fue lanzado el primer microprocesador?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=390, y= 50)

    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=390, y=330)
    
    frame.mainloop()

def resp_2():
    global score

    def delete():
        frame.destroy()
        preg_3()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= f"Correcto!! \nEl microprocesador Intel 4004 fue lanzado al mercado en 1980 y resultó ser muy revolucionario para su época. \nGanaste 2 puntos :D\nPuntaje total: {score}", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("i4004.png")
    image = image.resize((400,250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()

def preg_3():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 0:
            scores()
            frame.destroy()
            resp_3()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                frame.destroy()
                preg_4()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) Kenbak-1', 'B) Apple 1', 'C) Altair 8800', 'D) PDP-8']

    Label(frame, text= "¿Cuál fue el primer ordenador comercial?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=450, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=435, y=330)

    frame.mainloop()

def resp_3():
    global score

    def delete():
        frame.destroy()
        preg_4()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl Kenbak-1 fue el primer ordenador comercial lanzado en 1971 y creado por Jhon Blankenbaker. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("kenbak-01.png")
    image = image.resize((400,250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_4():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 2:
            scores()
            frame.destroy()
            resp_4()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la C :(')
                frame.destroy()
                preg_5()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) Obsborne 1', 'B) Epson HX-20', 'C) IBM 5100', 'D) EeePC 701']

    Label(frame, text= "¿Cuál fue el primer ordenador portátil?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=450, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=470, y=330)

    frame.mainloop()

def resp_4():
    global score

    def delete():
        frame.destroy()
        preg_5()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl IBM 5100 fue el primer ordenador portátil, Llevaba 64 kb de RAM, procesador PALM a 1,9 Mhz. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("IBM_5100.png")
    image = image.resize((400,250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()

def preg_5():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 2:
            scores()
            frame.destroy()
            resp_5()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la C :(')
                frame.destroy()
                preg_6()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) IBM 5150', 'B) Apple 1', 'C) Xerox Star 8010', 'D) TRS-80']

    Label(frame, text= "¿Cuál fue el primer ordenador personal en utilizar un mouse?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=450, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=440, y=330)

    frame.mainloop()

def resp_5():
    global score

    def delete():
        frame.destroy()
        preg_6()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl modelo Xero Star 8010 lanzado en 1981 fue el primer ordenador comercial en integrar un mouse. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("xero_star.png")
    image = image.resize((300,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_6():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 0:
            scores()
            frame.destroy()
            resp_6()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la A :(')
                if score < 6:
                    messagebox.showerror('Mensaje', 'No pasaste al nivel 2')
                    final()
                elif score >=6:
                    messagebox.showinfo('Mensaje', 'FELICIDADES!! pasaste al nivel 2')
                    frame.destroy()
                    preg_7()
                    
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) 1976', 'B) 1981', 'C) 1979', 'D) 1975']

    Label(frame, text= "¿En qué año fue lanzado el ordenador Apple 1?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=350, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=370, y=330)

    frame.mainloop()

def resp_6():
    global score

    def delete():
        if score >= 6:
            messagebox.showinfo('Mensaje', 'FELICIDADES!! pasaste al nivel 2')
            frame.destroy()
            preg_7()

        else:
            messagebox.showerror('Mensaje', 'No pudiste pasar al nivel 2 :(')
            frame.destroy()
            final()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl ordenador Apple 1 fue lanzado oficialmente al mercado en el año 1976.", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("apple_1.png")
    image = image.resize((330,330), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack()
    frame.mainloop()


def preg_7():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 1:
            scores()
            frame.destroy()
            resp_7()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la B :(')
                frame.destroy()
                preg_8
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) 1989', 'B) 1985', 'C) 1980', 'D) 1981']

    Label(frame, text= "¿En qué año fue lanzado Microsoft Windows 1.0?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=370, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=370, y=330)

    frame.mainloop()

def resp_7():
    global score

    def delete():
        frame.destroy()
        preg_8()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nMicrosoft Windows 1.0 fue lanzado oficialmente en el año 1985. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("windows_1.0.png")
    image = image.resize((450,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_8():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 0:
            scores()
            frame.destroy()
            resp_8()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la A :(')
                frame.destroy()
                preg_9()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) Linus Torvalds', 'B) Bill Gates', 'C) Steve Jobs', 'D) John Romero']

    Label(frame, text= "¿Quién fue el creador de Linux?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=450, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=460, y=330)

    frame.mainloop()

def resp_8():
    global score

    def delete():
        frame.destroy()
        preg_9()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nLinus Torvalds Fue El creador del kernel de Linux. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("linux_creador.png")
    image = image.resize((420,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_9():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 3:
            scores()
            frame.destroy()
            resp_9()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la D :(')
                frame.destroy()
                preg_10()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) 2010', 'B) 2012', 'C) 2009', 'D) 2008']

    Label(frame, text= "¿En qué año fue lanzado el sistema operativo Android?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=370, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=380, y=330)

    frame.mainloop()

def resp_9():
    global score

    def delete():
        frame.destroy()
        preg_10()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl primer relase del sistema operativo de andoid fue lanzado en 2008. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("android_logo.png")
    image = image.resize((430,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_10():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 3:
            scores()
            frame.destroy()
            resp_10()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la D :(')
                frame.destroy()
                preg_11()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) Bill Gates', 'B) Alan Turing', 'C) Tim Cook', 'D) Leonardo Chiariglione']

    Label(frame, text= "¿Quién fue el creador del formato mp3?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=460, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=470, y=330)

    frame.mainloop()

def resp_10():
    global score

    def delete():
        frame.destroy()
        preg_11()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nLeonardo Chiariglione fue el creador del formato MP3. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("mp3_creador.png")
    image = image.resize((460,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_11():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 1:
            scores()
            frame.destroy()
            resp_11()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la B :(')
                frame.destroy()
                preg_12()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) 1990', 'B) 1989', 'C) 1985', 'D) 1991']

    Label(frame, text= "¿En qué año se lanzó la primera versión del paquete Microsoft Office?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=370, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=380, y=330)

    frame.mainloop()

def resp_11():
    global score

    def delete():
        frame.destroy()
        preg_12()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl primer paquete de Microsoft Office fue lanzado en 1989. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("office_1990.png")
    image = image.resize((330,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()


def preg_12():
    global contador
    contador = 3


    def respuesta():
        if x.get() == 0:
            scores()
            frame.destroy()
            resp_12()
        else:
            global contador
            contador -= 1
            messagebox.showwarning("Error",f"Pregunta incorrecta\nTe quedan N°{contador} intentos")
            if contador == 0:
                messagebox.showerror('Fallate', 'La respuesta correcta era la A :(')
                frame.destroy()
                final()
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()

    opciones = ['A) Tim paterson', 'B) Bill Gates', 'C) Tim Cook', 'D) Mark Zuckerberg']

    Label(frame, text= "¿Quién fue el creador de MS-DOS?", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)

    image = Image.open("clippy.png")
    image = image.resize((120,120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').place(x=450, y= 50)


    x = IntVar()

    for i in range(len(opciones)):
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=200, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=460, y=330)

    frame.mainloop()

def resp_12():
    global score

    def delete():
        frame.destroy()
        final()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl sistema operativo MS-DOS fue escrito originalmente por Tim Paterson. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("msdos_creador.png")
    image = image.resize((280,280), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image= image, bg='#c0c0c0').pack()
    Button(frame, text= "Continuar", background='#c3c3c3', activebackground='#909090', font='mssans, 12', command=lambda:delete()).pack(pady=10)
    frame.mainloop()



def final():
    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text=f'Llegaste al final del juego !! \n{nombre.get()} tienes un total de {score} puntos', font='mssans, 14', bg='#c0c0c0').place(x=440, y=1)
    image = Image.open("end_game.png")
    image = image.resize((350,300), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    Label(frame, image=image, bg='#c0c0c0').place(x=435, y=70)
    frame.mainloop()
    







def scores():
    global score
    score += 2
    print(score)
    return score

window()


