# Relatório CoppeliaSim
> CoppeliaSim é um software de modelagem e simulação 3D.

### Sobre a atividade

- A atividade consistiu em criar um pêndulo simples usando objetos sólidos e uma junta de revolução. Através dela foi possível aprender conceitos básicos de modelagem e utilização da ferramenta, particularmente uso de:
- Formas de movimentação da câmera e objetos na interface, com atalhos do mouse e as ferramentas de translação por valores, além da compreensão dos eixos.
- Objetos dinâmicos e responsivos, e como usá-los em diferentes situações.
- Controles simples de movimento com a junta e seu menu de propriedades dinâmicas.
- Como funciona a hierarquia de objetos no CoppeliaSim

### Como foi realizada

- Foi criado um cuboide de dimensões 0.25 x 0.10 x 1.5 para servir como apoio, e ele foi definido como não diinâmico para ficar fixado ao solo -- se for deixado como dinâmico, o peso do pêndulo o derruba, a não ser que seja balanceado.
- Foi adicionada uma revolute joint como filha do apoio, e dimensionada para ficar no topo dele. 
- Foi criado um novo cuboide e uma esfera como sua child, e eles foram agrupados, este grupo então foi ligado à ponta da junta e transformado em child da mesma.
- A junta inicia a simulação em um ângulo de +30 graus, o que a faz "cair" e iniciar o movimento de vai e vem, inicialmente reduzindo e depois atingindo um ritmo consistente.

### Dificuldades encontradas

- O movimento do pêndulo não para, provavelmente por que forças resistivas não estão sendo levadas em consideração, isso poderia ser melhorado para ter uma simulação mais natural e acurada de um pêndulo real.
