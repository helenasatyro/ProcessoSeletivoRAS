# Relatório da Segunda Etapa do Processo Seletivo RAS

## Introdução:

O presente relatório tem objetivo de documentar o processo do desenvolvimento do projeto Object Tracking by Color, citando etapas, aprendizado e conclusões que puderam ser tomadas da missão. O projeto consiste em criar um programa que, através das bibliotecas de python OpenCV e Numpy, detecte objetos por cor, apresentando seu contorno e trajetória.

## Metodologia:

A forma de condução deste trabalho está descrita em três partes:
1. Desenvolvimento: descrito em etapas, com anexos mostrando o progresso.
2. Descrição do código: em anexo, o código usado no programa está documentado descrevendo cada ação.

## 1. Desenvolvimento
### A. Calibrar a detecção de cores - Estudo
Para compreender completamente cada parte do funcionamento do código e da biblioteca, diversas implementações foram testadas, o histórico de código e comentários de cada uma está descrito no relatório ou no próprio código.

Para compreender a detecção pura de cor: calibrando detecção de azul.
A partir do mapa de HSV em anexo (M), foram escolhidos valores iniciais para a calibragem: 
> H - 110 a 130, S - 120 a 255, V - 20 a 255

Foi necessário ajustar os valores para que ignorasse por exemplo o azulado de paredes brancas ou pretos azulados, que criavam ruído na identificação de objetos bem definidos, além de contornos gerados por ruído na imagem. (Anexos Aa 1-2)

O range obtido é de um azul de tom médio a escuro, foram usados como base os valores na apostila[1] disponibilizada, com alguns ajustes. 
> H - 90 a 255, S - 0 a 90, V - 0 a 255

Observando a máscara criada com a função inRange, pequenos incrementos e decrementos foram feitos até atingir um nível satisfatório de precisão. (Anexos A 1-4) Note, no arquivo parcialB.py, linhas 10 e 11, os valores estão definidos em um array numpy.

### B. Desenhar os contornos dos objetos
A partir do vídeo[2] disponibilizado, foi possível desenhar retângulos sobre os objetos de forma rudimentar, desconsiderando a rotação e as bordas reais. (Anexos B 1-5)

Implementação inicial

```
if len(contours) != 0:
    for contour in contours:
        # filtra ruído
        if cv2.contourArea(contour) > 300:
            x, y, w,h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x,y), (x+w, y+h), (168, 95, 66), 3)
    
    # Os contornos são ordenados da maior para a menor área, e é selecionada a maior para ser processada.
    contorno = sorted(contornos, key = cv2.contourArea, reverse = True)[0]
```


Seguindo o exemplo da apostila, novamente, foi implementado código que permite aproximar melhor a forma do objeto, através dos métodos boxPoints e minAreaRectangle, que permitem encontrar o retângulo, possivelmente rotacionado, de menor área que engloba os pontos passados como segundo parâmetro. (Anexo B6)

Na apostila, é adicionada uma linha de código que faz com que apenas o maior objeto da mesma cor seja contornado (Anexo B9). Apesar da  implementação anterior funcionar bem para rastrear múltiplos objetos de cor sólida, como visto nos Anexos B 7-8, ela não é tão efetiva para objetos com mais de uma cor, e é muito afetada por ruído. Para uma melhor implementação nesse caso, caberia a introdução de, por exemplo, uma busca por contornos Canny, associada à análise de cor, que pudesse dar uma melhor visão geral dos contornos dos objetos da imagem. Para os propósitos deste projeto, foi decidido manter o tracking restrito ao maior objeto de determinada cor.

É válido mencionar que caso fosse preciso contornar cada objeto de acordo com as bordas (da cor) reais, seria pertinente usar o parâmetro CHAIN_APPROX_NONE no momento da busca pelo contorno, e o próprio objeto contorno retornado como parâmetro em drawContours ao invés do retângulo. 


### C. Criação da GUI, aprimoramento do tracking e encapsulamento em funções

Após os testes em A e B, iniciou-se a adaptação ao modo de GUI. O código parcial antes da implementação da GUI está disponível no arquivo parcialB.py.
Utilizando de referência o vídeo tutorial [3] são inicializadas trackbars dentro de uma janela que recebe input do usuário, e é criada uma função normalizadora que garante que os valores de input sejam válidos, além disso, é introduzida a limiarização através da função threshold. 

A função é aplicada com as flags BINARY e OTSU, binary se refere à simples ativação ou desativação do pixel na máscara se o valor estiver acima ou abaixo do limiar, já a flag OTSU aplica um algoritmo que encontra o melhor valor para essa limiarização. A função de gaussian blur foi removida pois a limiarização gera melhores resultados. (Anexo C1 tem blur, C4 não tem)

Foi permitido que o usuário escolha se quer identificar ou não múltiplos objetos. (Anexos C6 e C7)

### D. 
--------
BIBLIOGRAFIA:

[1] Apostila - Introdução a Visão Computacional com Python e OpenCV (https://professor.luzerna.ifc.edu.br/ricardo-antonello/wp-content/uploads/sites/8/2017/02/Livro-Introdu%C3%A7%C3%A3o-a-Vis%C3%A3o-Computacional-com-Python-e-OpenCV-3.pdf)

[2] How to Detect Colors in OpenCV [Python] (https://www.youtube.com/watch?v=cMJwqxskyek)

[3] Tracking com Ajuste Dinâmico de Cores - Python & OpenCV 4 #08 (https://www.youtube.com/watch?v=NxyY3JBWoR4&t=30s&ab_channel=UniversoDiscreto)