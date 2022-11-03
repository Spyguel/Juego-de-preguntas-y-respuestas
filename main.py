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
    #root.iconbitmap("icono.ico")
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
    Button(frame, text='Continuar',font='mssans, 11',bg='#c3c3c3',activebackground='#909090', command=lambda:comprobar()).place(x= 670, y= 398,width= 80, height= 29)
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
                contador = 3
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
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=150, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=435, y=310)
    
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
                contador = 3
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
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=150, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=390, y=310)
    
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
                contador = 3
                frame.destroy()
                preg_1()
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
        Radiobutton(frame, text= opciones[i], variable= x, value= i,indicatoron= 1, font='mssans, 13', bg='#c0c0c0', activebackground='#c0c0c0').pack(side=LEFT, pady=150, padx=60)

    Button(frame, text= "seleccionar", command= lambda:respuesta(), background='#c3c3c3', activebackground='#909090', font='mssans, 12').place(x=435, y=310)

    frame.mainloop()

def resp_3():
    global score

    def delete():
        frame.destroy()
        final()

    frame = Frame(width=1180, height=450, bg='#c0c0c0')
    frame.pack()
    Label(frame, text= "Correcto!! \nEl Kenbak-1 fue el primer ordenador comercial lanzado en 1971 y creado por Jhon Blankenbaker. \nGanaste 2 puntos :D", font='mssans, 14', bg='#c3c3c3' ).pack(side=TOP)
    image = Image.open("kenbak-01.png")
    image = image.resize((400,250), Image.ANTIALIAS)
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
    return score


window()


