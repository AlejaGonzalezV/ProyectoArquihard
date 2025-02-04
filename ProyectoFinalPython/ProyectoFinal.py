from PIL import Image
from colour import Color
import time


def algoritmoV1 (src, tam):
	img = Image.open(src);
	img2 = img

	tiempo = 0
	#Aquí watch
	start_time = time.time()


	for i in range(0, img2.width):
		for j in range (0, img2.height):
			
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2=((255-color[0]),(255-color[1]),(255-color[2]))
			img2.putpixel(tupla,color2)
	
	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v1: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./../inv/imgalg1inv"+ tam + ".bmp");

def algoritmoV2(src, tam):
	img = Image.open(src);
	img2 = img

	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for i in range(0, img2.width):
		for j in range (0, img2.height):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), color[1], color[2])
			img2.putpixel(tupla,color2)
	
	for i in range(0, img2.width):
		for j in range (0, img2.height):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = (color[0], (255-color[1]), color[2])
			img2.putpixel(tupla,color2)

	for i in range(0, img2.width):
		for j in range (0, img2.height):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = (color[0], color[1], (255-color[2]))
			img2.putpixel(tupla,color2)


	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v2: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./../inv/imgalg2inv"+ tam + ".bmp");

	#CAMBIOOOOOOOOOO
def algoritmoV3(src, tam):
	img = Image.open(src);
	img2 = img

	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for j in range(0, img2.height):
		for i in range (0, img2.width):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), (255-color[1]), (255-color[2]))
			img2.putpixel(tupla,color2)

	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v3: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./../inv/imgalg3inv"+ tam + ".bmp");

def algoritmoV4(src, tam):
	img = Image.open(src);
	img2 = img

	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for i in range(0, img2.width):
		for j in range (0, img2.height):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), color[1], color[2])
			img2.putpixel(tupla,color2)

			#CAMBIO--------------------------
	for i in range(img2.width-1, 0, -1):
		for j in range (img2.height-1, 0, -1):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = (color[0], (255-color[1]), (255-color[2]))
			img2.putpixel(tupla,color2)

	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v4: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./../inv/imgalg4inv"+ tam + ".bmp");

def algoritmoV5(src, tam):
	img = Image.open(src);
	img2 = img

	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for i in range(0, img2.width-1,2):
		for j in range (0, img2.height-1,2):
			tupla = (i,j)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), (255-color[1]), (255-color[2]))
			img2.putpixel(tupla,color2)

			tupla = (i,j+1)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), (255-color[1]), (255-color[2]))
			img2.putpixel(tupla,color2)

			tupla = (i+1,j)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), (255-color[1]), (255-color[2]))
			img2.putpixel(tupla,color2)

			tupla = (i+1,j+1)
			color = img2.getpixel(tupla)
			color2 = ((255-color[0]), (255-color[1]), (255-color[2]))
			img2.putpixel(tupla,color2)

	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v5: " + str(tiempo)) 

	#Cambiar esta ruta
	img2.save("./../inv/imgalg5inv"+ tam + ".bmp");


def start():

    print("Inserte el algoritmo a usar")
    version = input()
    print("Inserte el tamaño de la imagen")
    tam = input()

    src = "./../img/" + tam + ".bmp"

    if version == "1":
        algoritmoV1(src, tam)
    elif version == "2":
        algoritmoV2(src, tam)
    elif version == "3":
        algoritmoV3(src, tam)
    elif version == "4":
        algoritmoV4(src, tam)
    elif version == "5":
        algoritmoV5(src, tam)
    else:
        print("Opción no válida")


start()







