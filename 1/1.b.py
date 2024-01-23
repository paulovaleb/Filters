import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregando a imagem
imagem = cv2.imread('lena_gray.bmp', cv2.IMREAD_GRAYSCALE)

# Aplicando um desfoque à imagem original
desfoque = cv2.GaussianBlur(imagem, (5, 5), 0)

# Calculando a máscara de realce (Unsharp Mask)
mascara = cv2.addWeighted(imagem, 1.5, desfoque, -0.5, 0)

# Exibindo a imagem original, o desfoque e o resultado do Unsharp Masking
plt.subplot(131), plt.imshow(imagem, cmap='gray'), plt.title('Imagem Original')
plt.subplot(132), plt.imshow(desfoque, cmap='gray'), plt.title('Desfoque')
plt.subplot(133), plt.imshow(mascara, cmap='gray'), plt.title('Unsharp Masking')
plt.show()

