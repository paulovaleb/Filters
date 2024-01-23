import cv2
import numpy as np
import matplotlib.pyplot as plt

def morfologia_abertura(imagem, elemento_estruturante, centro):
    # Certifique-se de que a imagem é binária (objetos brancos em fundo preto)
    _, binarizada = cv2.threshold(imagem, 1, 255, cv2.THRESH_BINARY)

    # Realizar a operação de abertura
    abertura = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, elemento_estruturante, anchor=centro)

    return abertura

# Exemplo de uso:
# Suponha que você tenha uma imagem binária (0 para fundo preto, 255 para objeto branco)
imagem = np.zeros((100, 100), dtype=np.uint8)

# Criar um objeto na imagem (objeto branco)
imagem[20:40, 30:70] = 255

# Criar um elemento estruturante maior (por exemplo, um quadrado de 9x9)
elemento_estruturante = np.ones((9, 9), dtype=np.uint8)

# Definir o centro do elemento estruturante
centro_elemento_estruturante = (4, 4)

# Aplicar a operação de abertura
resultado_abertura = morfologia_abertura(imagem, elemento_estruturante, centro_elemento_estruturante)

# Exibir a imagem original e o resultado da abertura
plt.subplot(1, 2, 1), plt.imshow(imagem, cmap='gray'), plt.title('Imagem Original')
plt.subplot(1, 2, 2), plt.imshow(resultado_abertura, cmap='gray'), plt.title('Abertura')
plt.show()
