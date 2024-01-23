import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
imagem = cv2.imread('quadro.png')

# Exibindo a imagem original
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.axis('off')
# Convertendo a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Definindo as faixas de cores para azul, amarelo e verde
faixa_azul = np.array([100, 50, 50]), np.array([140, 255, 255])
faixa_amarelo = np.array([20, 100, 100]), np.array([30, 255, 255])
faixa_verde = np.array([40, 50, 50]), np.array([80, 255, 255])

# Criando máscaras para os objetos de cor azul, amarelo e verde
mascara_azul = cv2.inRange(imagem_hsv, *faixa_azul)
mascara_amarelo = cv2.inRange(imagem_hsv, *faixa_amarelo)
mascara_verde = cv2.inRange(imagem_hsv, *faixa_verde)

# Preenchendo os buracos usando a função cv2.fillPoly
cv2.fillPoly(imagem, [cv2.findNonZero(mascara_azul)], color=(255, 0, 0))
cv2.fillPoly(imagem, [cv2.findNonZero(mascara_amarelo)], color=(0, 255, 255))
cv2.fillPoly(imagem, [cv2.findNonZero(mascara_verde)], color=(0, 255, 0))

# Salvando a imagem com buracos preenchidos
cv2.imwrite('imagem_com_buracos_preenchidos.png', imagem)

# Exibindo a imagem com buracos preenchidos
plt.subplot(1, 2, 2)
plt.title('Imagem com Buracos Preenchidos')
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Mostrando os gráficos
plt.show()
