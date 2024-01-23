import cv2
import numpy as np
import matplotlib.pyplot as plt

def preencher_buracos(imagem):
    # Inverter a imagem (objetos pretos em fundo branco)
    imagem_invertida = cv2.bitwise_not(imagem)

    # Criar um elemento estruturante (pode ser ajustado conforme necessário)
    elemento_estruturante = np.ones((15, 15), dtype=np.uint8)

    # Aplicar a operação de fechamento para preencher buracos
    imagem_preenchida = cv2.morphologyEx(imagem_invertida, cv2.MORPH_CLOSE, elemento_estruturante)

    # Inverter novamente para obter a imagem final
    imagem_final = cv2.bitwise_not(imagem_preenchida)

    return imagem_final

# Carregar a imagem
imagem_quadro = cv2.imread('quadro.png', cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if imagem_quadro is None:
    print("Erro ao carregar a imagem.")
else:
    # Preencher buracos na imagem
    imagem_preenchida = preencher_buracos(imagem_quadro)

    # Exibir as imagens original e preenchida
    plt.subplot(1, 2, 1), plt.imshow(imagem_quadro, cmap='gray'), plt.title('Imagem Original')
    plt.subplot(1, 2, 2), plt.imshow(imagem_preenchida, cmap='gray'), plt.title('Imagem Preenchida')
    plt.show()
