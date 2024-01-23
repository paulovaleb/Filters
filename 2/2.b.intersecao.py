import cv2
import numpy as np
import matplotlib.pyplot as plt

def morfologia_intersecao(imagem1, imagem2):
    # Certifique-se de que as imagens têm o mesmo tamanho
    assert imagem1.shape == imagem2.shape, "As imagens devem ter o mesmo tamanho"

    # Binarizar as imagens, assumindo que os objetos são brancos em um fundo preto
    _, binarizada1 = cv2.threshold(imagem1, 1, 255, cv2.THRESH_BINARY)
    _, binarizada2 = cv2.threshold(imagem2, 1, 255, cv2.THRESH_BINARY)

    # Realizar a operação de interseção
    intersecao = cv2.bitwise_and(binarizada1, binarizada2)

    return intersecao

# Exemplo de uso:
# Suponha que você tenha duas imagens binárias (0 para fundo preto, 255 para objeto branco)
imagem1 = np.zeros((100, 100), dtype=np.uint8)
imagem2 = np.zeros((100, 100), dtype=np.uint8)

# Criar objetos nas imagens (objetos brancos)
imagem1[20:40, 30:70] = 255
imagem2[30:60, 40:80] = 255

# Aplicar a operação de interseção
resultado_intersecao = morfologia_intersecao(imagem1, imagem2)

# Exibir as imagens em uma única tela usando matplotlib
plt.subplot(1, 3, 1), plt.imshow(imagem1, cmap='gray'), plt.title('Imagem 1')
plt.subplot(1, 3, 2), plt.imshow(imagem2, cmap='gray'), plt.title('Imagem 2')
plt.subplot(1, 3, 3), plt.imshow(resultado_intersecao, cmap='gray'), plt.title('Interseção')
plt.show()
