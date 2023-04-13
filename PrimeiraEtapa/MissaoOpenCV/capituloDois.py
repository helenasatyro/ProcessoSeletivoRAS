import cv2
imagem = cv2.imread('tomato.jpg')
# lendo e anotando os valores de Azul, Verde e Vermelho no pixel 0,0
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
cv2.imshow("Tomate!", imagem)
cv2.waitKey(0) 

for y in range(0, imagem.shape[0]):
 for x in range(0, imagem.shape[1]):
    imagem[y, x] = (255,0,0) # tudo azul
cv2.imshow("Tela azul", imagem)
cv2.waitKey(0) 

# gera um gradiente verde e roxo
for y in range(0, imagem.shape[0]): 
 for x in range(0, imagem.shape[1]): 
    imagem[y, x] = (x%256,y%256,x%256)
cv2.imshow("Gradientes", imagem) 
cv2.waitKey(0)

#gera uma imagem com algumas áreas "quadradas" 
# preenchidas por "ondas" verdes e pretas
for y in range(0, imagem.shape[0], 1): 
 for x in range(0, imagem.shape[1], 1): 
    imagem[y, x] = (0,(x*y)%256,0)
cv2.imshow("Interferencia!", imagem)
cv2.waitKey(0)

#gera quadradinhos amarelos de 5x5 pixels a cada 10 pixels da imagem
imagem = cv2.imread('tomato.jpg')
for y in range(0, imagem.shape[0], 10): 
    for x in range(0, imagem.shape[1], 10): 
        imagem[y:y+5, x: x+5] = (0,255,255)
cv2.imshow("Tomate Pontilhado", imagem)
cv2.waitKey(0)


# Criando minha própria fórmula - psicologia reversa, o tomate é o alvo :Da
imagem = cv2.imread('tomato.jpg')
for y in range(0, imagem.shape[0], 10): 
    for x in range(0, imagem.shape[1], 10): 
        if x == y:
           imagem[-x:x, y: y+5] = (0,0,0)
           imagem[x:x +5, -y:y] = (0,0,0)
           imagem[x:-x, y: y+5] = (0,0,0)
           imagem[x:x +5, -y:y] = (0,0,0)
           imagem[x:x +5, y:-y] = (0,0,0)
cv2.imshow("Tiro ao Alvo!", imagem)
cv2.waitKey(0)