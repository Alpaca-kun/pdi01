import numpy as np
import cv2 as cv
import time

def trataBordas(matriz):
    return np.pad(matriz, pad_width=1, mode='constant', constant_values=0)

def soma_e_multiplicacao(matriz, mascara, i, j):
    return (matriz[i-1][j-1] * mascara.item(0)) + (matriz[i-1][j] * mascara.item(1)) + (matriz[i-1][j+1] * mascara.item(2)) + (matriz[i][j-1] * mascara.item(3)) + (matriz[i][j] * mascara.item(4)) + (matriz[i][j+1] * mascara.item(5)) + (matriz[i+1][j-1] * mascara.item(6)) + (matriz[i+1][j] * mascara.item(7)) + (matriz[i+1][j+1] * mascara.item(8))
    

def convolucaoNormal(matriz, mascara):
    
    altura, largura = matriz.shape
    matriz_tratada = trataBordas(matriz)
    altura_tratada, largura_tratada = matriz_tratada.shape
    matriz_convolucao = np.empty([altura_tratada, largura_tratada])

    print("Matriz preenchida com zeros:")
    print(matriz_tratada)

    for i in range(1, altura_tratada - 1):
        for j in range(1, largura_tratada - 1):

            # novo_valor = soma_e_multiplicacao(matriz_tratada, mascara, i, j)
            # vetor_convolucao = np.append(vetor_convolucao, novo_valor)
            matriz_convolucao[i][j] = soma_e_multiplicacao(matriz_tratada, mascara, i, j)

    # print("Vetor Convolução:")
    # print(vetor_convolucao)
    # matriz_convolucao = vetor_convolucao.reshape(altura, largura)
    # print("Matriz Convolução: ")
    # print(matriz_convolucao)
    
    # return matriz_convolucao
    return matriz_convolucao


def transladaMatriz(matriz, valor_pad_vertical, valor_pad_horizontal, elem_mascara):

	print(matriz)

	if(valor_pad_vertical == 1):
		matriz = np.roll(matriz, 1, axis=0)[1:, :]  # shift down e apaga primeira linha
		matriz = np.pad(matriz, ((1,0),(0,0)), mode='constant', constant_values=0) # preenche primeira linha com zeros


	elif(valor_pad_vertical == -1):
		matriz = np.roll(matriz, -1, axis=0)[:-1, :]  # shift up e apaga última linha
		matriz = np.pad(matriz, ((0,1),(0,0)), mode='constant', constant_values=0) #preenche última linha com zeros
	
		
	if(valor_pad_horizontal == 1):
		matriz = np.roll(matriz, 1, axis=1)[:, 1:]  # shift right e apaga coluna esquerda
		matriz = np.pad(matriz, ((0,0),(1,0)), mode='constant', constant_values=0) #preenche coluna esquerda com zeros

	elif(valor_pad_horizontal == -1):
		matriz = np.roll(matriz, -1, axis = 1)[:, :-1] # shift left e apaga coluna direita
		matriz = np.pad(matriz, ((0,0),(0,1)), mode='constant', constant_values=0) # preenche coluna direita com zeros

	altura, largura = matriz.shape

	matriz = matriz * elem_mascara

	print(matriz)

	return matriz



def convolucaoTranslação(matriz, mascara):

	altura, largura = matriz.shape

	matrix_resultante = np.empty([altura, largura])

	matrix_resultante = transladaMatriz(matriz, 1, 1, mascara.item(0))
	matrix_resultante += transladaMatriz(matriz, 1, 0, mascara.item(1))
	matrix_resultante += transladaMatriz(matriz, 1, -1, mascara.item(2))
	matrix_resultante += transladaMatriz(matriz, 0, 1, mascara.item(3))
	matrix_resultante += transladaMatriz(matriz, 0, 0, mascara.item(4))
	matrix_resultante += transladaMatriz(matriz, 0, -1, mascara.item(5))
	matrix_resultante += transladaMatriz(matriz, -1, 1, mascara.item(6))
	matrix_resultante += transladaMatriz(matriz, -1, 0, mascara.item(7))
	matrix_resultante += transladaMatriz(matriz, -1, -1, mascara.item(8))

	print("Matriz Convolução: ")
	print(matrix_resultante)
	
	return matrix_resultante


def main():

	teste = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

	imgLena = cv.imread('./images/lena_original.png', 0)
	# imgLena = cv.imread('./images/cat.png', 0)
	# imgLena = cv.imread('lena_5x5.png', 0)
	# imgLena = cv.imread('kent-plantation-house.jpg', 0)

	cv.imshow('Leninha', imgLena)
	cv.waitKey(0)
	cv.destroyAllWindows()

	print("Matriz da imagem:\n")
	print(imgLena)


	mascara = np.matrix([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9],[1/9, 1/9, 1/9]])  # filtro média
	# mascara = np.matrix([[-1,-1,-1], [2,2,2], [-1,-1,-1]])    # detecção de linha (horizontal)
	# mascara = np.matrix([[-1,2,-1], [-1,2,-1], [-1,2,-1]])    # detecção de linha (vertical)
	# mascara = np.matrix([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])  # Detecção de borda
	# mascara = np.matrix([[-1,-2,-1], [0,0,0], [1,2,1]])  # Sobel Edge
	# mascara = np.matrix([[1,1,1], [1,1,1], [1,1,1]])
	# mascara = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
	# mascara = np.matrix([[1,2,1], [2,4,2], [1,2,1]])

	print("\nMáscara 3x3:\n")
	print(mascara)
	print()

	imagem_convolucao = [[]]

	print("Digite o número da convolução desejada:")
	op = int(input("1 - Normal\n2 -Translação de imagem\n"))


	while(op != 1 and op != 2):
		print("Escolha um valor entre 0 e 1:")
		op = input("1 - Normal\n2 -Translação de imagem\n")

	if(op == 1):
		print("Convolução Normal selecionada!")
		start = time.time()
		imagem_convolucao = convolucaoNormal(imgLena, mascara)

	elif(op == 2):
		print("Convolução por Translação de imagem selecionada!")
		start = time.time()
		imagem_convolucao = convolucaoTranslação(imgLena, mascara)


	alt, lar = imagem_convolucao.shape
	maior_tonalidade = np.amax(imagem_convolucao)

	for i in range(alt):
		for j in range(lar):
			imagem_convolucao[i][j] = (imagem_convolucao[i][j]/maior_tonalidade) * 255

	nova_img = imagem_convolucao.astype(np.int8)
	end = time.time()

	print("Imagem Convolução Normalizada: ")
	print(nova_img)

	print("Tempo total de execução: " + str(end - start))

	cv.imshow('lena convolucao', nova_img)
	cv.waitKey(0)
	cv.destroyAllWindows()

	cv.imwrite('./images/lena grayscale.png', imgLena)
	cv.imwrite('./images/lena convolucao.png', nova_img)

main()
