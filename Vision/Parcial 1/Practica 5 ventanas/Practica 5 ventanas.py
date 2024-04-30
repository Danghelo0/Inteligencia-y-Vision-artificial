import cv2

def mostrar(imagen, window_name="Imagen"):
    cv2.imshow(window_name, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def clasificador(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    binarizada = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return binarizada

def etiquetado(imagent):
    contornos, _ = cv2.findContours(imagent, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contornos

imagen = cv2.imread("ventanas.jpg")
mostrar(imagen)

imagent = clasificador(imagen)
mostrar(imagent, "Clasificado")

contornos = etiquetado(imagent)

for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

mostrar(imagen, "Objetos Detectados")