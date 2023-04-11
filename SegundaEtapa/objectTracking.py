import cv2
import numpy as np

# Determinar range de detecção no formato hsv 
# hue - cor, 
# saturation - intensidade, 
# value - luminosidade

# Através das trackbars, são determinados valores mínimos e máximos para os componentes de cor HSV.
trackbars = "trackbars"
cv2.namedWindow(trackbars) # Cria uma janela chamada trackbars, atribui-se seu nome à uma variável por conveniência

def onChange(val): # função de callback executada sempre que o valor muda
    pass


def getContourCol(min, max):
    hsvCol = [[[(min[0] + max[0]) / 2, (min[1] + max[1]) / 2, (min[2] + max[2]) / 2]]]
    bgrCol = cv2.cvtColor(hsvCol, cv2.COLOR_HSV2BGR) 
    return bgrCol



# garante que o mínimo seja sempre menor que o máximo nas trackbars
def normalizador():
    if cv2.getTrackbarPos("Min Hue", "trackbars") > cv2.getTrackbarPos("Max Hue", "trackbars"):
        cv2.setTrackbarPos("Max Hue", "trackbars", cv2.getTrackbarPos("Min Hue", "trackbars"))

    if cv2.getTrackbarPos("Min Sat", "trackbars") > cv2.getTrackbarPos("Max Sat", "trackbars"):
        cv2.setTrackbarPos("Max Sat", "trackbars", cv2.getTrackbarPos("Min Sat", "trackbars"))

    if cv2.getTrackbarPos("Min Val", "trackbars") > cv2.getTrackbarPos("Max Val", "trackbars"):
        cv2.setTrackbarPos("Max Val", "trackbars", cv2.getTrackbarPos("Min Val", "trackbars"))



# Na janela trackbars, cria trackbars para definição dos valores 
cv2.createTrackbar("Min Hue", trackbars, 0, 255, onChange)
cv2.createTrackbar("Max Hue", trackbars, 0, 255, onChange)
cv2.createTrackbar("Min Sat", trackbars, 0, 255, onChange)
cv2.createTrackbar("Max Sat", trackbars, 0, 255, onChange)
cv2.createTrackbar("Min Val", trackbars, 0, 255, onChange)
cv2.createTrackbar("Max Val", trackbars, 0, 255, onChange)

cv2.createTrackbar("Detectar Múltiplos", trackbars, 0, 1, onChange)


# criamos um objeto VideoCapture que auxilia no recebimento do video
# pode receber um endereço de memória para um vídeo ou o index
# de uma câmera, no caso 0 se refere à webcam, ou à primeira 
# câmera conectada ao computador
video = cv2.VideoCapture(0)

while True: 
# OBTENÇÃO DO FRAME e CONVERSÂO
    # Sucesso guarda um booleano que diz se foi possível ler o vídeo
    # img recebe o frame do video
    sucesso, img = video.read()
    if not sucesso:
        break

    # converte a imagem de RGB para HSV
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# OBTENÇÃO DOS VALORES DOS TRACKBARS    
    # recebe o valor de input das trackbars
    minHue = cv2.getTrackbarPos("Min Hue", trackbars)
    maxHue = cv2.getTrackbarPos("Max Hue", trackbars)
    minSat = cv2.getTrackbarPos("Min Sat", trackbars)
    maxSat = cv2.getTrackbarPos("Max Sat", trackbars)
    minVal = cv2.getTrackbarPos("Min Val", trackbars)
    maxVal = cv2.getTrackbarPos("Max Val", trackbars)

    normalizador() # garante que o mínimo será menor que o máximo

    minimo = np.array([minHue, minSat, minVal])
    maximo = np.array([maxHue, maxSat, maxVal])

# MÀSCARA
    # máscara que mostra o que está sendo detectado (preto e branco), será passada como parâmetro para encontrar seu contorno
    mask = cv2.inRange(img, minimo, maximo)
    # máscara que permite exibir apenas os pixels que estão sendo capturados no range
    mask = cv2.bitwise_and(img, img, mask = mask)
    # converte imagem para preto e branco
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) 
    # aplica limiarização binary com o limiar definido por OTSU
    _,mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# CONTORNOS
    # Modo de recuperação RETR_EXTERNAL retorna a borda externa
    # CHAIN_APPROX_SIMPLE guarda apenas as coordenadas necessárias para contorno
    # Hierarquia se refere à topologia dos contornos, é retornada pela função findContours.
    contornos, hierarquia = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Filtragem para que apenas objetos de tamanho relevante sejam considerados
    if len(contornos) > 0:
        if cv2.getTrackbarPos("Detectar Múltiplos", trackbars) == 1: 
            for contorno in contornos:
                if cv2.contourArea(contorno) > 400:
                    rect = np.int32(cv2.boxPoints(cv2.minAreaRect(contorno)))
                    cv2.drawContours(img, [rect], -1, (168, 95, 66),2)
        else:
            contorno = sorted(contornos, key = cv2.contourArea, reverse = True)[0]
            if cv2.contourArea(contorno) > 400:
                # É encontrado o retângulo de menor área que pode ser desenhado a partir dos pontos do contorno, 
                # boxPonts encontra seus vértices, gerando assim um retângulo possivelmente rotacionado, de menor área, que contém os pontos do contorno
                rect = np.int32(cv2.boxPoints(cv2.minAreaRect(contorno)))
                cv2.drawContours(img, [rect], -1, (168, 95, 66),2)

# EXIBIÇÂO
    # Exibem a imagem da webcam com os objetos destacados
    cv2.imshow("webcam", img)
    # Exibe a máscara do que está sendo detectado
    cv2.imshow("mask", mask)

    #aguarda 1 milissegundo antes de mostrar o pròximo frame e checa para ver se a tecla de saída foi pressionada para encerrar o loop
    if cv2.waitKey(1) & 0xFF == ord("q") or 0xFF == 27:
        break
# ENCERRAMENTO    
# Fecha o acesso à câmera e as janelas abertas
video.release()
cv2.destroyAllWindows()