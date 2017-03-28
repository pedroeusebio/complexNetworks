---
fontsize: 10pt
geometry: margin=3cm
---

# Primeiro Trabalho Pratico
## Redes Complexas
#### Aluno: Pedro Santos Eusébio
##### repositório : [ComplexNetwork](https://github.com/pedroeusebio/complexNetworks/tree/master/TP1)

Redes analisadas:

- [Facebook](http://snap.stanford.edu/data/egonets-Facebook.html)
- [Enron email network](http://snap.stanford.edu/data/email-Enron.html)
- [High Energy Physics](http://snap.stanford.edu/data/ca-HepPh.html)

## Ferramentas

Foi utilizado para o desenvolvimento do trabalho a linguagem de programação Python juntamente com as bibliotecas Graph Tool, para análise dos grafos, matplotlib, para gerar os gráficos, e por fim a biblioteca Numpy para realizar as operações com *arrays* mais facilmente.

## Análise


### 1. Facebook

![Grafo Facebook](https://i.imgur.com/rXixFSx.png){ width=95% }


Como pode ser observado na imagem, o grafo é conexo, ou seja, todos os vértices são conectados. Além disso, o grafo é não direcionado, visto que, as arestas representam a relação de amizade entre duas pessoas (vértices). É um grafo com **4039 vértices** e **88234 arestas**. Os dados foram coletados por participantes que são usuários do aplicativo do Facebook *Social Circles*.

#### **Métricas**

|          | degrees     | distance   | clustering    |betweeness edges|betweeness vertex| components | closeness    | 
|----------|-------------|------------|---------------|----------------|-----------------|------------|--------------| 
| min      | 1           | 1          | 0             | 1,23E-07       | 0               | 0          | 0,178254     | 
| max      | 1045        | 8          | 1             | 0,171493       | 0,480518        | 4039.0     | 0,459699     | 
| mean     | 43,691012   | 3,692507   | 0,605547      | 4,18E-05       | 0,000667        | 4039.0     | 0,276168     | 
| std      | 52,414115   |            | 0,003374      | 0,001103       | 0,011645        | 0,0        | 0,036119     | 


- Clusterização Global : 0,51917428
- Quantidade de Componentes : 1

Podemos perceber através dos dados e do gráfico de Grau x Probabilidade(figura 2), a média baixa é explicada pelo fato de terem muitos vértices com um grau muito baixo e certas excessões com grau muito grande (como o grau máximo de 1045). Existem vértices isolados também, que são ligados a apenas um vertice.

Além disso, a maior distância do grafo é pequena se comparado ao número de vértices. Se observarmos a imagem do grafo (figura 1) veremos que temos diversos vértices que conectam os agrupamentos, fazendo um caminho mais rápido entre esses grupos, justificando dessa forma, a média da distância entre os vértices.

De acordo com o gráfico abaixo (figura 3), podemos ver também a distribuição dos índices de clusterização e as suas respectivas probabilidades. Observando o valor médio da clusterização e o gráfico acima, nos permite dizer que existem diversos agrupamentos e que estes são bastante conexos e interligados, tendo diversos vértices interligados uns com os outros aumentando assim o índice médio de clusterização. 

Podemos perceber também, que o grafo é composto por apenas um componente, ou seja, existem pelo menos um caminho de um vértice para os demais.

Analisando o gráfico abaixo (figura 4), nota-se que existam uma distribuição do índice de *closeness* mais uniforme, justificado pelo fato do grafo ser uma componente conexa. A concentração está entre 0,25 e 0,33, com uma pequena parcela abaixo de 0,20, que seriam as folhas do grafo e vértices que possuem grau baixo, e um outra parcela com valores acima de 0,33, que seriam os vértices de grau elevado que conectam dois ou mais agrupamentos.

![Grau x Probabilidade](https://i.imgur.com/5hr2Wco.png){ width=50% }

![Clusterização x Probabilidade](https://i.imgur.com/tkmA2Wh.png){ width=50% }

![*Closeness* x Probabilidade](https://i.imgur.com/O7UDWZv.png){ width=50% }


