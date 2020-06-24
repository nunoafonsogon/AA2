# Projeto de Aprendizagem Automática II

## Grupo 9

* [André Gonçalves](https://github.com/andregclvs)
* [Nuno Valente](https://github.com/nunoafonsogon)
* [Paulo Barbosa](https://github.com/PauloAFBarbosa)
* [Rui Ribeiro](https://github.com/mrr37)

### Introdução
O presente repositório reflete o resultado do trabalho elaborado no âmbito da entrega do Trabalho Prático da Unidade Curricular de Aprendizagem Automática II, que se insere no 2º semestre do 4º ano do Mestrado Integrado em Engenharia Informática.
O objetivo deste trabalho consiste em utilizar vários métodos de redes neuronais para detetar malária em imagens de células. 
O dataset de treino utilizado pode ser visto no link: https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria

Foram escolhidos 3 métodos para resolver o problema proposto, estes métodos são:
*	[MLP- Perceptron Multicamadas](https://github.com/nunoafonsogon/AA2/blob/master/MalariaMLP.ipynb)
*	[CNN-Rede Neuronal Convolucional](https://github.com/nunoafonsogon/AA2/blob/master/Cnn.ipynb)
*	[CNN Transfer Learning](https://github.com/nunoafonsogon/AA2/blob/master/Cnn-Transfer-Learning.ipynb)

Como segundo objetivo serão comparados os diferentes métodos escolhidos.

### Análise do Dataset
- O Dataset é formado por 27558 imagens.
- O Dataset está dividido em 2 partes iguais: 13780 infetados e 13780 não infetados.
- Altura  de imagem oscila entre 40 e 385
- Largura de imagem oscila entre 46 e 394

A análise deste dataset foi feita no seguinte [script](https://github.com/nunoafonsogon/AA2/blob/master/Analise_do%20_dataset.ipynb)


### MLP
Com o modelo MLP conseguimos obter uma accuracy de 70%, considerando que uma escolha aleatória obteria uma média a rondar os 50% 
e que este método não é o mais adequado para imagens consideramos que 70% seja um bom resultado para este método. Utilizaremos este resultado como baseline para os métodos apresentados à frente.

Notou-se que uma quanto maior a imagem e consequentemente a camada de entrada pior o desempenho do modelo,
testando a função resize() nas imagens do dataset obteve-se melhor desempenho com o tamanho 28 por 28.

Em baixo podemos ver a arquitetura do modelo e o seu desempenho através de 100 épocas.

![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/mlp_arq.png)
![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/mlp_acc.png)


### CNN
Como era de esperar o modelo com melhor desempenho foi este tendo uma accuraccy superior a 95% como pode ser observado na figura 4.
Este modelo chega rapidamente a 95% de desempenho e sobe ligeiramente em cada época tendo sido observado accuraccys até 99%.
Considera-se este um resultado excelente visto a sua taxa de sucesso quase total.

![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/CNN_arq.png)


![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/CNN_acc.png)

### CNN Transfer-learning

Como esperado CNN transfer Learning não superou o resultado de CNN normal, 
este resultado não foi surpreendente devido à quantidade elevada de elementos no dataset utilizado. 
No entanto como podemos ver na figura 5 que a accuracy máxima obtida ronda 95%, apesar da grande oscilação entre épocas, este resultado mostra-se insatisfatório visto que uma rede muito mais simples a CNN obteve 99% de accuracy constantemente.

É de notar que este modelo foi treinado para distinguir objetos através do dataset imagenet. 
A arquitetura do modelo não se encontra representada neste ficheiro devido ao seu tamanho no entanto pode ser consultada no notebook python correspondente.

![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/CNN_TL_acc.png)

### Comparações
O modelo que obteu melhor resultados foi o modelo CNN. Este resultado era esperado devido a:

1- ser um método especializado em imagens ao contrário do método MLP

2- ter um dataset extenso podendo superar a aprendizagem de Transfer Learning

### Conclusões

Em jeito de conclusão, gostaríamos de dizer que aprendemos bastante na realização deste projeto, nomeadamente, na análise de dados, na sua manipulação e tratamento, na definição de modelos, análise de resultados e claro, aprofundamos o nosso conhecimento em relação a algumas técnicas e ferramentas utilizadas. Tivemos algumas dificuldades na obtenção das melhores dimensões para as imagens do dataset bem como alguns impasses no tratamento e análise de dados mas, no geral, pensamos que o estudo desenvolvido permitiu responder às questões propostas inicialmente, pelo que podemos considerar que o trabalho desenvolvido foi positivo.
Damos assim concluído o nosso trabalho prático, saindo do mesmo felizes e confiantes que os objetivos foram cumpridos com sucesso.
