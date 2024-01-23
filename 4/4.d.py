import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para encontrar o fecho convexo de objetos de uma cor específica
def encontrar_fecho_convexo(imagem, cor):
    # Converte a imagem para o espaço de cor HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Define as faixas de cor (nesse exemplo, substitua pelos valores corretos)
    if cor == 'azul':
        lower_range = np.array([90, 50, 50])
        upper_range = np.array([130, 255, 255])
    elif cor == 'amarelo':
        lower_range = np.array([20, 100, 100])
        upper_range = np.array([30, 255, 255])
    elif cor == 'verde':
        lower_range = np.array([40, 50, 50])
        upper_range = np.array([80, 255, 255])
    else:
        raise ValueError("Cor não suportada")

    # Cria uma máscara usando a faixa de cor
    mascara = cv2.inRange(hsv, lower_range, upper_range)

    # Encontra contornos na máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontra e desenha o fecho convexo para cada contorno
    fecho_convexo = []
    for contorno in contornos:
        hull = cv2.convexHull(contorno)
        fecho_convexo.append(hull)

    return fecho_convexo

# Carrega a imagem
imagem = cv2.imread('imagem_com_buracos_preenchidos.png')

# Encontra o fecho convexo para cada cor
azul_fecho_convexo = encontrar_fecho_convexo(imagem, 'azul')
amarelo_fecho_convexo = encontrar_fecho_convexo(imagem, 'amarelo')
verde_fecho_convexo = encontrar_fecho_convexo(imagem, 'verde')

# Cria uma imagem vazia
imagem_resultado = np.zeros_like(imagem)

# Desenha o fecho convexo na imagem resultante
cv2.drawContours(imagem_resultado, azul_fecho_convexo, -1, (255, 0, 0), 2)
cv2.drawContours(imagem_resultado, amarelo_fecho_convexo, -1, (0, 255, 255), 2)
cv2.drawContours(imagem_resultado, verde_fecho_convexo, -1, (0, 255, 0), 2)

# Mostra a imagem resultante usando Matplotlib
plt.imshow(cv2.cvtColor(imagem_resultado, cv2.COLOR_BGR2RGB))
plt.title('Fecho Convexo para Azul, Amarelo e Verde')
plt.show()
