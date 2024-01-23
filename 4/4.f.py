import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('imagem_com_buracos_preenchidos.png')

# Converter a imagem para escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Extrair apenas os objetos vermelhos na imagem original
lower_red = np.array([0, 0, 100])
upper_red = np.array([100, 100, 255])
mask_red = cv2.inRange(imagem, lower_red, upper_red)

# Aplicar a transformada hit-or-miss à máscara vermelha
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

resultado_hit_or_miss = cv2.morphologyEx(mask_red, cv2.MORPH_HITMISS, kernel)

# Encontrar contornos na imagem resultante
contornos, _ = cv2.findContours(resultado_hit_or_miss, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar contornos na imagem original
imagem_contornos = imagem.copy()
cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2)

# Exibir a imagem original, a máscara vermelha, e a imagem com contornos
plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)), plt.title('Imagem Original')
plt.subplot(1, 3, 2), plt.imshow(mask_red, cmap='gray'), plt.title('Máscara Vermelha')
plt.subplot(1, 3, 3), plt.imshow(cv2.cvtColor(imagem_contornos, cv2.COLOR_BGR2RGB)), plt.title('Contornos')

plt.show()
