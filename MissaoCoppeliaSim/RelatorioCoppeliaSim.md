# Relatório Sobre a Missão CoppeliaSim

## 1. Introdução
- CoppeliaSim é um software gratuito de modelagem e simulação 3D que traz a possibilidade de simular no computador o comportamento de entidades afetadas pela física.
- A missão permitiu aprender os comandos e funções essenciais do CoppeliaSim através da construção de um pêndulo.

### 2. Objetivos e Resumo

- A atividade consistiu em criar um pêndulo simples usando objetos sólidos e uma junta de revolução. Através dela foi possível aprender conceitos básicos de modelagem e utilização da ferramenta, particularmente uso de:
- Formas de movimentação da câmera e objetos na interface, com atalhos do mouse e as ferramentas de translação por valores, além da compreensão dos eixos.
- Objetos dinâmicos e responsivos, e como usá-los em diferentes situações.
- Controles simples de movimento com a junta e seu menu de propriedades dinâmicas.
- Como funciona a hierarquia de objetos no CoppeliaSim

### 3. Etapas e Componentes

- Foi criado um cuboide de dimensões 0.25 x 0.10 x 1.5 para servir como apoio, e ele foi definido como não diinâmico para ficar fixado ao solo -- se for deixado como dinâmico, o peso do pêndulo o derruba, a não ser que seja balanceado.
- Foi adicionada uma revolute joint como filha do apoio, e dimensionada para ficar no topo dele. 
- Foi criado um novo cuboide e uma esfera como sua child, e eles foram agrupados, este grupo então foi ligado à ponta da junta e transformado em child da mesma.
- A junta inicia a simulação em um ângulo de +30 graus, o que a faz "cair" e iniciar o movimento de vai e vem, inicialmente reduzindo sua amplitude e depois atingindo um ritmo e abertura consistentes.

### 4. Dificuldades encontradas

- O movimento do pêndulo não para, provavelmente por que forças resistivas não estão sendo levadas em consideração, isso poderia ser melhorado para ter uma simulação mais natural e acurada de um pêndulo real.
- O software em si tem uma grande quantidade de funções e menus que são complexos para iniciantes, tendo utilizado apenas o básico, as possibilidades oferecidas pela linguagem Lua e scripting nas cenas não foram utilizadas.

### 5. Conclusão
O software CoppeliaSim, assim como outros programas de simulação, oferece uma grande praticidade em prototipagem de componentes físicos, permitindo a observação de diversos testes e configurações que, na vida real, resultaria em grandes gastos. O programa é complexo à primeira vista, mas através dessa missão, foi possível entender o mínimo necessário para criar uma cena e dar movimento a ela, precisamente o objetivo que foi proposto.
