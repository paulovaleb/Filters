# Importar as bibliotecas necessárias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ler a imagem "lena_gray.bmp" em tons de cinza
img = cv2.imread("lena_gray.bmp", cv2.IMREAD_GRAYSCALE)

# Definir o kernel do operador Prewitt
kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)

# Aplicar o filtro Prewitt na imagem
prewitt_x = cv2.filter2D(img, cv2.CV_64F, kernel)
prewitt_y = cv2.filter2D(img, cv2.CV_64F, kernel.T) # transposta do kernel

# Calcular a magnitude do gradiente
prewitt = cv2.magnitude(prewitt_x, prewitt_y)

# Converter a imagem para o tipo uint8
prewitt = cv2.convertScaleAbs(prewitt)

# Exibir a imagem original e a imagem filtrada
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Imagem original")
plt.axis("off")
plt.subplot(122)
plt.imshow(prewitt, cmap="gray")
plt.title("Imagem filtrada com Prewitt")
plt.axis("off")
plt.show()
