# Introdução
O objetivo deste trabalho consiste em utilizar vários métodos de redes neuronais para detetar malária em imagens de células. 
O dataset de treino utilizado pode ser visto no link: https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria

Foram escolhidos 3 métodos para resolver o problema proposto, estes métodos são:
-	MLP- Perceptron Multicamadas
-	CNN-Rede Neuronal Convolucional
-	CNN Transfer Learning- CNN treinada com outro problema.

Como segundo objetivo serão comparados os diferentes métodos escolhidos.

# MLP
Com o modelo MLP conseguimos obter uma accuracy de 70%, considerando que uma escolha aleatória obteria uma média a rondar os 50% 
e que este método não é o mais adequado para imagens consideramos que 70% seja um bom resultado para este método. 

Notou-se que uma quanto maior a imagem e consequentemente a camada de entrada pior o desempenho do modelo,
testando a função resize() nas imagens do dataset obteve-se melhor desempenho com o tamanho 28 por 28.

Em baixo podemos ver a arquitetura do modelo e o seu desempenho através de 100 épocas.

![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/mlp_arq.png)
![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/mlp_acc.png)


# CNN
Como era de esperar o modelo com melhor desempenho foi este tendo uma accuraccy superior a 95% como pode ser observado na figura 4.
Este modelo chega rapidamente a 95% de desempenho e sobe ligeiramente em cada época tendo sido observado accuraccys até 98%.
Considera-se este um resultado excelente visto a sua taxa de sucesso quase total.

![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/CNN_arq.png)


![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/CNN_acc.png)

# CNN Transfer-learning

Como esperado CNN transfer Learning não superou o resultado de CNN normal, 
este resultado não foi surpreendente devido à quantidade elevada de elementos no dataset utilizado. 
No entanto como podemos ver na figura 5 que a accuracy máxima obtida ronda 25%, apesar da grande oscilação entre épocas.

É de notar que este modelo foi treinado para distinguir objetos através do dataset imagenet. 
A arquitetura do modelo não se encontra representada neste ficheiro devido ao seu tamanho no entanto pode ser consultada no notebook python correspondente.

![Image description](https://github.com/nunoafonsogon/AA2/blob/master/images/CNN_TL_acc.png)

# Comparações
O modelo que obteu melhor resultados foi o modelo CNN. Este resultado era esperado devido a:

1- ser um método especializado em imagens ao contrário do método MLP

2- ter um dataset extenso podendo superar a aprendizagem de Transfer Learning







