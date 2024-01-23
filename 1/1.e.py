import cv2

# Carregar a imagem em escala de cinza
imagem = cv2.imread("lena_gray.bmp", cv2.IMREAD_GRAYSCALE)

# Aplicar as máscaras de Sobel na imagem usando a função Sobel
imagem_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
imagem_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)

# Calcular a magnitude das bordas usando a função sqrt
imagem_magnitude = cv2.sqrt(imagem_x**2 + imagem_y**2)

# Calcular a orientação das bordas usando a função phase
imagem_orientacao = cv2.phase(imagem_x, imagem_y)

# Salvar as imagens resultantes
cv2.imwrite("lena_gray_sobel_x.bmp", imagem_x)
cv2.imwrite("lena_gray_sobel_y.bmp", imagem_y)
cv2.imwrite("lena_gray_sobel_magnitude.bmp", imagem_magnitude)
cv2.imwrite("lena_gray_sobel_orientacao.bmp", imagem_orientacao)
