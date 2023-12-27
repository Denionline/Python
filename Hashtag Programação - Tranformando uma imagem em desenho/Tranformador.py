import cv2
import os

def transformar_desenho(arquivo, qtde):
    imagem = cv2.imread(f'imgs/{arquivo}')
    imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_invertida = cv2.bitwise_not(imagem_pb)
    qtde = 91
    imagem_blur = cv2.GaussianBlur(imagem_invertida, (qtde, qtde), 0)
    imagem_blur_invertida = cv2.bitwise_not(imagem_blur)
    imagem_desenho = cv2.divide(imagem_pb, imagem_blur_invertida, scale=256.0)

    cv2.imwrite(f'imgs-prontas/{arquivo}', imagem_desenho)

lista = os.listdir('imgs')

for arquivo in lista:
    transformar_desenho(arquivo, 90)