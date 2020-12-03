from PIL import Image
import time


def algoritmoV1 (src):
	img = Image.open(src);
	img2 = img

	color
	tiempo = 0
	#Aquí watch
	start_time = time.time()


	for i in range(0, img2.height):
		for j in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb((255-color.R), (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)
	
	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v1: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./imagenesInvertidas/" + tamanio + ".bmp");

def algoritmoV2(src):
	img = Image.open(src);
	img2 = img

	color
	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for i in range(0, img2.height):
		for j in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, (255-color.R), color.G, color.B)
			img2.putPixel(tupla,color)
	
	for i in range(0, img2.height):
		for j in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, color.R, (255-color.G), color.B)
			img2.putPixel(tupla,color)

	for i in range(0, img2.height):
		for j in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, color.R, color.G, (255-color.B))
			img2.putPixel(tupla,color)


	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v2: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./imagenesInvertidas/" + tamanio + ".bmp");

def algoritmov3(src):
	img = Image.open(src);
	img2 = img

	color
	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for j in range(0, img2.height):
		for i in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb((255-color.R), (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)

	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v3: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./imagenesInvertidas/" + tamanio + ".bmp");

def algoritmov4(src):
	img = Image.open(src);
	img2 = img

	color
	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for i in range(0, img2.height):
		for j in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, (255-color.R), color.G, color.B)
			img2.putPixel(tupla,color)

	for i in range(0, img2.height):
		for j in range (0, img2.width):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, color.R, (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)

	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v4: " + str(tiempo))

	#Cambiar esta ruta
	img2.save("./imagenesInvertidas/" + tamanio + ".bmp");

def algoritmov5(src):
	img = Image.open(src);
	img2 = img

	color
	tiempo = 0
	#Aquí watch
	start_time = time.time()

	for i in range(0, img2.height-1,2):
		for j in range (0, img2.width-1,2):
			tupla = (i,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, (255-color.R), (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)

			tupla = (i,j+1)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, (255-color.R), (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)

			tupla = (i+1,j)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, (255-color.R), (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)

			tupla = (i+1,j+1)
			color = img2.getPixel(tupla)
			color = Color.FromArgb(255, (255-color.R), (255-color.G), (255-color.B))
			img2.putPixel(tupla,color)

	#Stop watch
	end_time = time.time()
	tiempo = ((end_time-start_time)*1000000000)
	print ("Algoritmo v4: " + str(tiempo)) 

	#Cambiar esta ruta
	img2.save("./imagenesInvertidas/" + tamanio + ".bmp");


##Falta main donde se llamen los métodos








