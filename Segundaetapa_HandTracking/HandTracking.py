import cv2
import mediapipe as mp

# Mediapipe oferece diversos pacotes de "soluções" focados em tipos diferentes de análise de imagem, 
# aqui, usaremos o pacote hands e o pacote drawing utils, que permitem, respectivamente analisar imagens de mãos e desenhar sobre essas imagens
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# recebe o vídeo da webcam (videocapture 0 se refere à primeira câmera do computador, que geralmente é a webcam integrada)
video = cv2.VideoCapture(0)

while True:
    # a função read retorna um valor booleano indicando se a leitura teve sucesso, e o frame atual
    sucesso, frame = video.read()

    # como openCV trabalha em BGR e MediaPipe trabalha em RGB, é necessário converter a imagem de um sistema para o outro
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # a função Hands().process(img) de mediapipe analisa a imagem passada como argumento, reconhecendo as mãos presentes
    resultado = mp_hands.Hands().process(frame)


    cv2.imShow(frame, "WebCam")
    cv2.waitKey()