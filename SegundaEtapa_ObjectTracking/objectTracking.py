import numpy as np
import cv2
import time


# Determinar range de detecção no formato hsv 
# hue - cor, 
# saturation - intensidade, 
# value - luminosidade

### FUNÇÕES ###
def onChange(val): # função de callback executada sempre que o valor muda
    pass

# garante que o mínimo seja sempre menor que o máximo nas trackbars
def normalizador():
    # se a menor posição for igual à maior, a maior passa a "ser arrastada" junto à menor
    if cv2.getTrackbarPos("Min Hue", "trackbars") > cv2.getTrackbarPos("Max Hue", "trackbars"):
        cv2.setTrackbarPos("Max Hue", "trackbars", cv2.getTrackbarPos("Min Hue", "trackbars"))

    if cv2.getTrackbarPos("Min Sat", "trackbars") > cv2.getTrackbarPos("Max Sat", "trackbars"):
        cv2.setTrackbarPos("Max Sat", "trackbars", cv2.getTrackbarPos("Min Sat", "trackbars"))

    if cv2.getTrackbarPos("Min Val", "trackbars") > cv2.getTrackbarPos("Max Val", "trackbars"):
        cv2.setTrackbarPos("Max Val", "trackbars", cv2.getTrackbarPos("Min Val", "trackbars"))

# controla e desenha contornos, coordenadas, e trajetória na tela, 
# periodo determina o intervalo entre capturas, inversamente proporcional à precisão
# comprimento determina a quantidade de pontos que devem ser guardados, o tamanho do rastro
def contornador(contorno, frame, contador, arrayPontos, periodo, comprimento):

    # Filtragem para que apenas objetos de tamanho relevante sejam considerados
    if cv2.contourArea(contorno) > 400:
        # É encontrado o retângulo de menor área que pode ser desenhado a partir dos pontos do contorno, 
        # boxPonts encontra seus vértices, gerando assim um retângulo possivelmente rotacionado, de menor área, que contém os pontos do contorno
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(contorno)))

        # moments retorna o momento da imagem, uma média de densidade de pixeis que ajuda a calcular o centroide do objeto
        M = cv2.moments(contorno)
        # fórmula para achar o centróide doobjeto baseado nos momentos e posições cx e cy (detalhes no item D)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # a cada <periodo> frames guardamos uma posição do centro do objeto
            # sçao adicionados itens até que o tamanho do array -1 seja atingido
            if contador % periodo == 0 and len(arrayPontos) <= comprimento:
                arrayPontos.append((cx, cy))
            # no segundo if desenhamos os últimos <comprimento> pontos, com o mais antigo sendo o mais esbranquiçado
            if len(arrayPontos) >= 1:
                for i in range(len(arrayPontos) -1):
                    # subtraindo i * 11 ao valor de azul e verde, a cor fica mais escura a cada ponto
                    cv2.circle(frame, arrayPontos[i], 4, (110 - i*11, 110 - i*11, 255), -1)
                    # os pontos são movidos uma posição para trás como em um array, e o mais antigo é descartado
                    arrayPontos[i] = arrayPontos[i+1]
                    # é adicionado o ponto atual na última posição, a mais recente
                    arrayPontos[-1] = (cx, cy)
            # coordenadas do ponto atual, que serão impressas na tela
            coordenada = f"x: {cx} y: {cy}"
            # desenho do círculo atual é feito em todos os frames, não a cada dez, para explicitar a continuidade
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            # texto indicando a posição atual do objeto é impresso na tela com um pequeno offset do ponto central
            cv2.putText(frame, coordenada, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #retângulo que contém o objeto é desenhado na tela
        cv2.drawContours(frame, [rect], -1, (0, 0, 255),2)

#### EXECUÇÃO ###

# Através das trackbars, são determinados valores mínimos e máximos para os componentes de cor HSV.
trackbars = "trackbars"
cv2.namedWindow(trackbars) # Cria uma janela chamada trackbars, atribui-se seu nome à uma variável por conveniência

# Na janela trackbars, cria trackbars para definição dos valores 
cv2.createTrackbar("Min Hue", trackbars, 0, 255, onChange)
cv2.createTrackbar("Max Hue", trackbars, 0, 255, onChange)
cv2.createTrackbar("Min Sat", trackbars, 0, 255, onChange)
cv2.createTrackbar("Max Sat", trackbars, 0, 255, onChange)
cv2.createTrackbar("Min Val", trackbars, 0, 255, onChange)
cv2.createTrackbar("Max Val", trackbars, 0, 255, onChange)
# trackbar que funciona como switch e permite o usuário determinar o que quer computar
cv2.createTrackbar("Detectar Múltiplos", trackbars, 0, 1, onChange)
                

# criamos um objeto VideoCapture que auxilia no recebimento do video
# pode receber um endereço de memória para um vídeo ou o index
# de uma câmera, no caso 0 se refere à webcam, ou à primeira 
# câmera conectada ao computador
video = cv2.VideoCapture(0)

# contador registra qual é o frame atual, para ser usado na trajetória, e pontos mantém as coordenadas relevantes para o mesmo propósito
contador = 0
pontos = []

while True: 
    contador += 1
# OBTENÇÃO DO FRAME e CONVERSÂO
    # Sucesso guarda um booleano que diz se foi possível ler o vídeo, se falso, encerra o programa
    # img recebe o frame do video
    sucesso, frame = video.read()
    if not sucesso:
        break

    # converte a imagem de RGB para HSV
    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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
    mask = cv2.inRange(frame, minimo, maximo)
    # máscara que permite exibir apenas os pixels que estão sendo capturados no range
    mask = cv2.bitwise_and(frame, frame, mask = mask)
    # converte imagem para preto e branco
    # usamos a máscara pois queremos considerar apenas a cor sendo processada
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) 
    # blur ajuda a remover ruído
    mask = cv2.GaussianBlur(mask, (3, 3), 0)

    # aplica limiarização binary com o limiar definido por OTSU
    _,mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# CONTORNOS
    # Modo de recuperação RETR_EXTERNAL retorna a borda externa
    # CHAIN_APPROX_SIMPLE guarda apenas as coordenadas necessárias para contorno
    # Hierarquia se refere à topologia dos contornos, é retornada pela função findContours.
    contornos, hierarquia = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# se houver algum contorno
    if len(contornos) > 0:
        # checa quantos contornos deve acompanhar
        if cv2.getTrackbarPos("Detectar Múltiplos", trackbars) == 1: 
            # roda o contornador para todos os contornos relevantes
            for contorno in contornos:
                contornador(contorno, frame, contador, pontos, 10, 10)
        else:
            # seleciona o maior contorno
            contorno = sorted(contornos, key = cv2.contourArea, reverse = True)[0]
            # roda o contornador para todos os contornos relevantes
            contornador(contorno, frame, contador, pontos, 5, 20)


# EXIBIÇÂO
    # Exibem a imagem da webcam com os objetos destacados
    img = np.concatenate((frame, mask), axis=1)
    cv2.imshow("webcam - mask", img)
    # Exibe a máscara do que está sendo detectado
    #cv2.imshow("mask", mask)

    #aguarda 1 milissegundo antes de mostrar o pròximo frame ou checa para ver se a tecla de saída foi pressionada para encerrar o loop
    if cv2.waitKey(1) & 0xFF == ord("q") or 0xFF == 27:
        break
# ENCERRAMENTO    
# Fecha o acesso à câmera e as janelas abertas
video.release()
cv2.destroyAllWindows()