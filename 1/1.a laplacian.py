import cv2
import matplotlib.pyplot as plt

# Carregar a imagem "lena_gray.bmp" em escala de cinza
img = cv2.imread("lena_gray.bmp", cv2.IMREAD_GRAYSCALE)

# Aplicar o filtro Laplaciano na imagem
edges = cv2.Laplacian(img, -1)

# Mostrar a imagem original e a imagem com bordas detectadas usando Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Laplacian')

plt.show()

