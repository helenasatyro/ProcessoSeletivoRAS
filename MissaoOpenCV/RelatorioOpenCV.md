# Relatório da Missão OpenCV
- OpenCV é uma biblioteca para visão computacional.
- Visão computacional por sua vez é um ramo de inteligência artificial que foca em obter informações de imagem/vídeo.

### Sobre o Programa do Capítulo 1
- Nesse capítulo criamos um programa que abre uma imagem, exibe informações sobre ela e a salva com outro nome.
- A única modificação feita no código a partir do exemplo foi o nome da imagem eum comentário sobre o atributo shape de imagem.

- A biblioteca opencv disponibiliza funções que nos permitem ver o tamanho e canais da imagem através do atributo shape, que guarda uma lista de três valores.
- Os canais referem-se aos canais de cor RGB: na imagm, cada pixel guarda uma tupla de três valores de 0 a 255, representando a quantidade de "pigmento" de cada uma das cores Red, Green e Blue, em 8 bits sem sinal.
- Isso nos dá, pelas dimensões da matriz frormada pelos 3 canais, 16.7 milhões de possibilidades de cor.
- Outra possibilidade seria a foto ser preta e branca, tendo apenas o canal de luminosidade, e ainda através de pesquisas externas foi constatado que pode também ter o canal Alfa de transparência, presente, por exemplo em imagens do tipo png.


### Sobre o programa do Capítulo 2

- Nesse capítulo, exploramos o sistema de coordenadas de pixels e aprendemos a manipulação básica deles.
- Pra uma imagem de 20x10 pixels coordenada (0,0) fica no canto superior esquerdo da imagem, e o pixel no canto inferior direito terá as coordenadas (19, 9).
- Através de loops foram desenhados padrões sobre a foto.
- O capítulo encoraja o leitor a criar sua própria forma, ao final do programa está um pequeno algoritmo que desenha um padrão de tiro ao alvo sobre a foto do tomate.
- Funcionamento: queremos desenhar quadrados concêntricos na imagem, e quando x é igual a y, temos que os pontos formam uma diagonal.
- Se pintarmos a linha e coluna de cada ponto onde x+y, preencheremos toda a imagem.
- Se pintarmos 10 a linhas e colunas a cada 10 pixels, teremos uma grade quadriculada.
- Se pintarmos apenas de x a -x, teremos uma linha que começa em x e não vai até o final, mas até um ponto simétrico.
- A partir dessa lógica, é possível construir o padrão de tiro ao alvo.