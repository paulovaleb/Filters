import cv2
import numpy as np
import matplotlib.pyplot as plt

def morfologia_dilatacao(imagem, elemento_estruturante, centro):
    # Certifique-se de que a imagem é binária (objetos brancos em fundo preto)
    _, binarizada = cv2.threshold(imagem, 1, 255, cv2.THRESH_BINARY)

    # Realizar a operação de dilatação
    dilatacao = cv2.dilate(binarizada, elemento_estruturante, anchor=centro, iterations=1)

    return dilatacao

# Exemplo de uso:
# Suponha que você tenha uma imagem binária (0 para fundo preto, 255 para objeto branco)
imagem = np.zeros((100, 100), dtype=np.uint8)

# Criar um objeto na imagem (objeto branco)
imagem[20:40, 30:70] = 255

# Criar um elemento estruturante (por exemplo, um quadrado)
elemento_estruturante = np.ones((5, 5), dtype=np.uint8)

# Definir o centro do elemento estruturante
centro_elemento_estruturante = (2, 2)

# Aplicar a operação de dilatação
resultado_dilatacao = morfologia_dilatacao(imagem, elemento_estruturante, centro_elemento_estruturante)

# Exibir a imagem original e o resultado da dilatação
plt.subplot(1, 2, 1), plt.imshow(imagem, cmap='gray'), plt.title('Imagem Original')
plt.subplot(1, 2, 2), plt.imshow(resultado_dilatacao, cmap='gray'), plt.title('Dilatação')
plt.show()
