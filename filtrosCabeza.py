import cv2
import imutils

cap = cv2.VideoCapture(0)

image = cv2.imread('Objects/Cabeza/mexico.png', cv2.IMREAD_UNCHANGED)

# Detector de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
	
	ret, frame = cap.read()
	if ret == False: print("no estoy")
	frame = imutils.resize(frame, width=640)

	# Detección de los rostros presentes en el fotograma
	faces = faceClassif.detectMultiScale(frame, 1.3, 5)

	for (x, y, w, h) in faces: 
		# Redimensionar la imagen de entrada de acuerdo al ancho del rostro detectado
		resized_image = imutils.resize(image, width=w)
		filas_image = resized_image.shape[0]
		col_image = w

		# Determinar una porción del alto de la imagen de entrada redimensionada
		porcion_alto = filas_image // 4

		dif = 0

		# Mirar si cabe el objeto, si no avisar para cambiar posición cámara
		if y + porcion_alto - filas_image >= 0:
			n_frame = frame[y + porcion_alto - filas_image : y + porcion_alto,
				x : x + col_image]
		else:
			# Determinamos la sección de la imagen que excede a la del video
			dif = abs(y + porcion_alto - filas_image) 
			# Tomamos la sección de frame, en donde se va a ubicar
			# el gorro/tiara
			n_frame = frame[0 : y + porcion_alto,
				x : x + col_image]

		# Determinamos la máscara que posee la imagen de entrada
		# redimensionada y también la invertimos
		mask = resized_image[:, :, 3]
		mask_inv = cv2.bitwise_not(mask)
			
		# Creamos una imagen con fondo negro y el gorro/tiara/2021
		# Luego creamos una imagen en donde en el fondo esté frame
		# y en negro el gorro/tiara/2021
		bg_black = cv2.bitwise_and(resized_image, resized_image, mask=mask)
		bg_black = bg_black[dif:, :, 0:3]
		bg_frame = cv2.bitwise_and(n_frame, n_frame, mask=mask_inv[dif:,:])

		# Sumamos las dos imágenes obtenidas
		result = cv2.add(bg_black, bg_frame)
		if y + porcion_alto - filas_image >= 0:
			frame[y + porcion_alto - filas_image : y + porcion_alto, x : x + col_image] = result

		else:
			frame[0 : y + porcion_alto, x : x + col_image] = result
		
	
	cv2.imshow('frame',frame)

	if cv2.waitKey(1) == ord(' '):
    		break

cap.release()
cv2.destroyAllWindows()