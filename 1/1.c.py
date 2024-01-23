import cv2

# Carregar a imagem em escala de cinza
imagem = cv2.imread("lena_gray.bmp", cv2.IMREAD_GRAYSCALE)

# Aplicar o filtro da média com tamanho 5x5
imagem_suavizada = cv2.blur(imagem, (5, 5))

# Aplicar o filtro passa-alta subtraindo a imagem suavizada da imagem original
imagem_passa_alta = cv2.subtract(imagem, imagem_suavizada)

# Aplicar a filtragem highboost com fator 2
imagem_highboost = cv2.addWeighted(imagem, 2, imagem_passa_alta, 1, 0)

# Salvar a imagem highboost
cv2.imwrite("lena_gray_highboost.bmp", imagem_highboost)