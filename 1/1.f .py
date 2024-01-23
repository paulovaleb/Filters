import cv2
import numpy as np
from matplotlib import pyplot as plt

# Função para calcular métricas
# Carregar a imagem
imagem_original = cv2.imread('lena_ruido.bmp', cv2.IMREAD_GRAYSCALE)

# Aplicar os filtros
kernel1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]) / 5.0
kernel2 = np.ones((3, 3), np.float32) / 9.0
kernel3 = np.array([[1, 3, 1], [3, 16, 3], [1, 3, 1]]) / 32.0
kernel4 = np.array([[0, 1, 0], [1, 4, 1], [0, 1, 0]]) / 8.0

resultado1 = cv2.filter2D(imagem_original, -1, kernel1)
resultado2 = cv2.filter2D(imagem_original, -1, kernel2)
resultado3 = cv2.filter2D(imagem_original, -1, kernel3)
resultado4 = cv2.filter2D(imagem_original, -1, kernel4)

# Aplicar o filtro da mediana
resultado_mediana = cv2.medianBlur(imagem_original, 3)

# Mostrar as imagens
plt.figure(figsize=(12, 6))

plt.subplot(231), plt.imshow(resultado1, cmap='gray'), plt.title('Filtro 1')
plt.subplot(232), plt.imshow(resultado2, cmap='gray'), plt.title('Filtro 2')
plt.subplot(233), plt.imshow(resultado3, cmap='gray'), plt.title('Filtro 3')
plt.subplot(234), plt.imshow(resultado4, cmap='gray'), plt.title('Filtro 4')
plt.subplot(235), plt.imshow(resultado_mediana, cmap='gray'), plt.title('Filtro da Mediana')
plt.subplot(236), plt.imshow(imagem_original, cmap='gray'), plt.title('Imagem Original')

plt.show()