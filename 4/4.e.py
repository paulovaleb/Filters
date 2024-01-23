import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leitura da imagem
image = cv2.imread('imagem_com_buracos_preenchidos.png')

# Conversão da imagem para o espaço de cores HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definindo os intervalos de cor para azul, amarelo e verde
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Segmentação de cores
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Encontrar o esqueleto dos objetos
def find_skeleton(mask):
    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Criar uma imagem em branco para desenhar os contornos
    skeleton = np.zeros_like(mask)
    
    # Desenhar os contornos na imagem em branco
    cv2.drawContours(skeleton, contours, -1, 255, 1)
    
    # Encontrar o esqueleto
    skeleton = cv2.ximgproc.thinning(skeleton)
    
    return skeleton

# Encontrar o esqueleto para cada cor
skeleton_blue = find_skeleton(mask_blue)
skeleton_yellow = find_skeleton(mask_yellow)
skeleton_green = find_skeleton(mask_green)

# Exibir os resultados usando Matplotlib
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.title('Blue Skeleton')
plt.imshow(skeleton_blue, cmap='gray')

plt.subplot(132)
plt.title('Yellow Skeleton')
plt.imshow(skeleton_yellow, cmap='gray')

plt.subplot(133)
plt.title('Green Skeleton')
plt.imshow(skeleton_green, cmap='gray')

plt.tight_layout()
plt.show()
