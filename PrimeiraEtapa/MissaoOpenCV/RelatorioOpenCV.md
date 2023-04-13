# Relatório da Missão OpenCV

# 1. Introdução e Resumo
A missão openCV foi voltada ao ramo de visão computacional, área da computação que se propõe a processar vídeo e imagens através de algoritmos. 
Durante o processo de desenvolvimento da missão, foi necessário aprender os princípios básicos de processamento de imagem--pixels, o sistema de cores RGB e compreender a ideia de matrizes de cor. Também foi necessário instalar e aprender sobre a biblioteca OpenCV, o que foi uma tarefa simples dado o material disponibilizado e a documentação da biblioteca.
No segundo capítulo, foram exploradas algumas possibilidades de manipulação de cores através de iteração pelos pixels, experimentar com diferentes fórmulas foi um desafio interessante, especialmente por desenvolver o pensamento sobre matrizes.

## 2. Programas

### 2.1. Sobre o Programa do Capítulo 1

  2.1.1 Resumo 
- Nesse capítulo foi criado um programa que abre uma imagem, exibe informações sobre ela e a salva com outro nome.
- A única modificação feita no código do exemplo foi o nome da imagem e um comentário sobre o atributo shape de imagem.
 
 2.1.2. O que foi aprendido
- A biblioteca opencv disponibiliza funções que nos permitem ver o tamanho e canais da imagem através do atributo shape, que guarda uma lista de três valores.
- Os canais referem-se aos canais de cor RGB: na imagm, cada pixel guarda uma tupla de três valores de 0 a 255, representando a quantidade de "pigmento" de cada uma das cores Red, Green e Blue, em 8 bits sem sinal.
- Isso nos dá, pelas dimensões da matriz formada pelos 3 canais, 16.7 milhões de possibilidades de cor.
- Outra possibilidade seria a foto ser preta e branca, tendo apenas o canal de luminosidade. 
- Ainda através de pesquisas externas foi constatado que é possível também ter o canal Alfa de transparência, presente, por exemplo, em imagens do tipo png.


### 2.2. Sobre o programa do Capítulo 2
  2.2.1. Resumo
- Nesse capítulo, foi explorado o sistema de coordenadas de pixels e a manipulação básica deles através de loops e princípios de matrizes em python. Por exemplo, a forma de leitura de pixels iniciando em (0,0) no canto superior esquerdo e terminando em (n,n) no canto inferior direito. Foram feitos alguns programas que editam as cores da imagem de maneiras diferentes: criando formas, gradientes ou a colorindo completamente.
 
  2.2.2 Exercício de implementação
- O capítulo encoraja o leitor a criar sua própria forma, ao final do programa está um pequeno trecho de código que desenha um padrão de tiro ao alvo sobre a foto do tomate.
- Funcionamento: queremos desenhar quadrados concêntricos na imagem, e quando x é igual a y, temos que os pontos formam uma diagonal.
- Se pintarmos a linha e coluna de cada ponto onde x+y, preencheremos toda a imagem.
- Se pintarmos 10 a linhas e colunas a cada 10 pixels, teremos uma grade quadriculada. (aprendido através de exemplo do livro)
- Se pintarmos apenas de x a -x, teremos uma linha que começa em x e não vai até o final, mas até um ponto simétrico.
- A partir dessa lógica, é possível construir o padrão de tiro ao alvo.

## 3. Conclusão
Sendo a missão que mais se encaixava no perfil do presente relator, a atividade foi simples em questão de técnica, e a instalação do openCV talvez tenha sido a parte mais desafiadora devido a particularidades de sistema operacional. A atividade de experimentação com formas de processar pixels certamente será fundamental para o desenvolvimento de algoritmos de reconhecimento.
