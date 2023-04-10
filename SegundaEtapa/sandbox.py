import cv2
import numpy as np

# Determinar range de detecção no formato hsv 
# hue - cor, 
# saturation - intensidade, 
# value - luminosidade

# Detectar Azul médio:
minAzul = np.array([110, 120, 20], dtype = "uint8")
maxAzul = np.array([130, 255, 255], dtype = "uint8")

# criamos um objeto VideoCapture que auxilia noprocessamento de video
# pode receber um endereço de memória para um vídeo ou o index
# de uma câmera, no caso 0 se refere à webcam, ou à primeira 
# câmera concectada ao computador
video = cv2.VideoCapture(0)
while True: 
    # Sucesso guarda um booleano que diz se foi possível ler o vídeo
    # img recebe o frame do video
    sucesso, img = video.read()
    if not sucesso:
        break

    # é necessário converter a imagem de RGB para HSV
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # máscara que mostra o que está sendo detectado (preto e branco)
    # blur ajuda na busca de contornos
    maskAzul = cv2.inRange(img, minAzul, maxAzul)
    #mask = cv2.GaussianBlur(mask, (3, 3), 0)

    # Modo de recuperação retr external retorna a borda maior
    # Chain Approx Simple guarda apenas as coordenadas necessárias do contorno
    contours, hierarquia = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Antes da implementação que permite que apenas um contorno seja rastreado
    """     if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 300:
                x, y, w,h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y), (x+w, y+h), (168, 95, 66), 3)
     """

    cv2.imshow("webcam", img)
    cv2.imshow("mask", maskAzul)

    #aguarda 1 milissegundo antes de mostrar o pròximo frame
    cv2.waitKey(1)