import tkinter
import pafy
import os
import youtube_dl
carpeta_descarga = './Musica'





def open_folder():
    path = os.path.realpath(carpeta_descarga)
    os.startfile(path)




if __name__ == '__main__':
    ventana = tkinter.Tk()
    ventana.geometry("600x400")
    ventana.config(bg="orange")


    # titulo del programa

    ventana.title("Descargar Musica")

    # barra para introducir la url
    cajaTexto = tkinter.Entry(ventana, justify="center")
    cajaTexto.pack()

    # boton de hacer click


    caja_link = tkinter.Entry(ventana, justify="center" )
    caja_link.place(width=50,height=50)
    caja_link.pack()


    def mycb(total, recvd, ratio, rate, eta):
        caja_link.delete(0, tkinter.END)
        caja_link.insert(0, ratio )
        ventana.update()

    def descargarMusica():
        video = pafy.new(cajaTexto.get())

        bestaudio = video.getbestaudio()

        bestaudio.download(filepath=carpeta_descarga, callback=mycb)


    boton1 = tkinter.Button(ventana, text="Descargar", font=("Verdana", 10), justify="center", command=descargarMusica)
    boton1.pack(padx=30, pady=30)


    boton2 = tkinter.Button(ventana, text="Descargas" , font=("Verdana" , 12) , justify="center", command=open_folder)
    boton2.pack()








    ventana.mainloop()
