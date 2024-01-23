import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
imagem = cv2.imread('quadro.png')

# Convertendo a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Criando uma máscara para os pixels pretos
mascara_preta = (imagem_cinza == 0)

# Aplicando a máscara na imagem original
imagem_sem_pretos = np.where(mascara_preta[:, :, None], 255, imagem)

# Exibindo a imagem original
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Exibindo a imagem sem objetos pretos
plt.subplot(1, 2, 2)
plt.title('Imagem sem Pretos')
plt.imshow(cv2.cvtColor(imagem_sem_pretos, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Mostrando os gráficos
plt.show()
