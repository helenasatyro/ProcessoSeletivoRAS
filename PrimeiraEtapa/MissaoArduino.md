# Relatório Sobre a Missão Arduíno
> Link do TinkerCAD - https://www.tinkercad.com/things/elvyj3PFEBz-arduinoblink

### 1. Introdução
O seguinte relatório pretende listar conhecimentos obtidos durante o processo de desenvolvimento da missão arduíno,para a primeira parte do processo seletivo da RAS.

### 2.Resumo
Para completar a missão, foi necessário aprender os conceitos básicos de funcionamentos do arduíno, além do uso de componentes eletrônicos como o LED e a protoboard. Foi utilizado como base o material passado na descrição da missão, além de consultas outros projeto básicos de tinkerCAD. Foi experimentado com alguns outros códigos e setups com a protoboard para entender melhor a parte elétrica. 

## 3. Componentes eletrônicos

### 3.1 Sobre o Arduíno UNO
- O arduíno é uma placa microcontroladora de hardware  e software livre, desenvolvido para uso em projetos interativos. O modelo utilizado para esta missão foi o Arduino UNO, um dos modelos de arduíno para iniciantes.
- Ele é alimentado por uma fonte USB de 7-12V, e opera em 5V, além de poder ser alimentado por fontes externas pela porta VIN, e oferecer 3,3V através do chip FDTI.
- Possui 14 pinos digitais, 6 pinos analógicos, e alguns pinos para funcionalidades específicas.

### 3.2Sobre Resistores
- O resistor é um componente eletrônico utilizado para reduzir a corrente.
- Existem diversos tipos de resistores, alguns de resistência fixa, outros ajustáveis manualmente, e até alguns que funcionam como sensores.
- É possível saber a resistência oferecida por um resistor observando os anéis coloridos em seu corpo.
- O resistor utilizado para a missão tem resistência de 125-130 Ohms, como pode ser observado pelos anéis:
> Marrom = 1 | 
> Laranja = 3 | 
> Marrom = x10 | 
> Dourado = tolerância de 5% | 
> 13 x 10 = 130 +-5

### 3.3 Sobre os LEDs
- LEDs ou Light Emitting Diodes são, com o nome indica, diodos que emitem luz.
- Difere da lâmpada por emitir luz de um material sólido. Não emite calor, e gasta menos energia.
- Os primeiros LEDs eram de cor vermelha, mas na década de 70, foram inventados os LEDs azul e branco, que abriram portas para mais aplicações do LED no dia a dia.
- Hoje em dia, temos leds de diversas cores e níveis de luminosidade.
- O terminal longo do LED (ânodo) se conecta ao lado positivo da fonte, e o terminal menor (cátodo), é ligado ao negativo.
- LEDs suportam tensões específicas, e são geralmente pareados a um resistor, cuja resistência pode ser determinada da seguinte forma: 
> Consultar a tabela de tensões e amperagens para cada cor de LED: 
> No caso foi usado um LED azul, cuja tensão recomendada é de 2,5 a 3.0 volts, e a amperagem é de 0.02A.
> Saber a tensão da fonte de alimentação: O arduíno tem pinos digitais de saída que operam em 5V.
> Calcular a resistência desejada usando a seguinte fórmula:

> R = (Vfonte - Vled) / Iled

> R = (5 - 2.5) / 0.02 = 125 Ohms

### 4. Código

- O arduíno UNO pode ser operado usando a linguagem C++
- Segue o código comentado.
- A base para o código pode ser econtrada nos exemplos inclusos com o arduíno, ela foi modificada para permitir as três velocidades de piscar.

```void setup() // inicializa o pino como output, executado uma vez
{
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() // permanece em loop durante toda a execução
{
  for (int i = 0; i < 3; i++) // repete 3 vezes
  {
  	digitalWrite(LED_BUILTIN, HIGH); // output alto = 1 = ligado
  	delay(1000); // aguarda 1 segundo
  	digitalWrite(LED_BUILTIN, LOW); // output baixo = 0 = desligado
  	delay(1000); // aguarda 1 segundo
  }
  for (int i = 0; i < 3; i++)
  {
  	digitalWrite(LED_BUILTIN, HIGH);
  	delay(2000); // aguarda 2 segundos
  	digitalWrite(LED_BUILTIN, LOW);
  	delay(2000); //aguarda 2 segundos
  }
  
  for (int i; i < 3; i++)
  {
  	  digitalWrite(LED_BUILTIN, HIGH);
  	  delay(3000); // aguarda 3 segundos
  	  digitalWrite(LED_BUILTIN, LOW);
  	  delay(3000); // aguarda 3 segundos
    }
  }
  ```

### 5. Considerações finais
- A missão permitiu adquirir conhecimentos básicos sobre uso do arduíno além de conceitos simples de eletrônica, apesar de não ter alta complexidade, foi uma ótima atividade introdutória e gerou ideias para outros projetos.
