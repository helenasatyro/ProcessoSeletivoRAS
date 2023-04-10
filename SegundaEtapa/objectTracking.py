import cv2
import numpy as np

# Determinar range de detecção no formato hsv 
# hue - cor, 
# saturation - intensidade, 
# value - luminosidade

# Detectar Azul, valores mínimos e máximos de cada componente HSV:
minimo = np.array([90, 0, 0], dtype = "uint8")
maximo = np.array([255, 90, 255], dtype = "uint8")

# criamos um objeto VideoCapture que auxilia no recebimento do video
# pode receber um endereço de memória para um vídeo ou o index
# de uma câmera, no caso 0 se refere à webcam, ou à primeira 
# câmera conectada ao computador
video = cv2.VideoCapture(0)

while True: 
    # Sucesso guarda um booleano que diz se foi possível ler o vídeo
    # img recebe o frame do video
    sucesso, img = video.read()
    if not sucesso:
        break

    # é necessário converter a imagem de RGB para HSV
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # máscara que mostra o que está sendo detectado (preto e branco), será passada como parâmetro para encontrar seu contorno.
    # blur ajuda na busca de contornos
    mask = cv2.inRange(img, minimo, maximo)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)

    # Modo de recuperação RETR_EXTERNAL retorna a borda externa
    # CHAIN_APPROX_SIMPLE guarda apenas as coordenadas necessárias para contorno
    # Hierarquia se refere à topologia dos contornos, é retornada pela função findContours.
    contornos, hierarquia = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    
    # Filtragem para que apenas objetos de tamanho relevante sejam considerados
    for contorno in contornos:
        if cv2.contourArea(contorno) > 400:
            # É encontrado o retângulo de menor área que pode ser desenhado a partir dos pontos do contorno, 
            # boxPonts encontra seus vértices, gerando assim um retângulo possivelmente rotacionado, de menor área, que contém os pontos do contorno
            rect = np.int32(cv2.boxPoints(cv2.minAreaRect(contorno)))
            cv2.drawContours(img, [rect], -1, (168, 95, 66),2)

    # Exibem a imagem da webcam com os objetos destacados
    cv2.imshow("webcam", img)
    # Exibe a máscara do que está sendo detectado
    cv2.imshow("mask", mask)

    #aguarda 1 milissegundo antes de mostrar o pròximo frame e checa para ver se a tecla de saída foi pressionada para encerrar o loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Fecha o acesso à câmera e as janelas abertas
video.release()
cv2.destroyAllWindows()