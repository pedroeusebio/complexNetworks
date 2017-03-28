---
fontsize: 10pt
geometry: margin=3cm
---

# Primeiro Trabalho Pratico
## Redes Complexas
#### Aluno: Pedro Santos Eusébio

Redes analisadas:

- [Facebook](http://snap.stanford.edu/data/egonets-Facebook.html)
- [Enron email network](http://snap.stanford.edu/data/email-Enron.html)
- [High Energy Physics](http://snap.stanford.edu/data/ca-HepPh.html)

## Ferramentas

Foi utilizado para o desenvolvimento do trabalho a linguagem de programação Python juntamente com as bibliotecas Graph Tool, para análise dos grafos, matplotlib, para gerar os gráficos, e por fim a biblioteca Numpy para realizar as operações com *arrays* mais facilmente.

## Análise


### 1. Facebook

![Grafo Facebook](https://i.imgur.com/rXixFSx.png){ width=70% }


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
    
![Grau x Probabilidade](https://i.imgur.com/5hr2Wco.png){ width=50% }


Podemos perceber através dos dados e do gráfico de Probalidade x Grau, a média baixa é explicada pelo fato de terem muitos vértices com um grau muito baixo e certas excessões com grau muito grande (como o grau máximo de 1045). Existem vértices isolados também, que são ligados a apenas um vertice.

Além disso, a maior distância do grafo é pequena se comparado ao número de vértices. Se observarmos a imagem do grafo veremos que temos diversos vértices que conectam os agrupamentos, fazendo um caminho mais rápido entre esses grupos, justificando dessa forma, a média da distância entre os vértices.
	

![Clusterização x Probabilidade](https://i.imgur.com/tkmA2Wh.png){ width=50% }

De acordo com o gráfico acima, podemos ver também a distribuição dos índices de clusterização e as suas respectivas probabilidades.
Observando o valor médio da clusterização e o gráfico acima, nos permite dizer que existem diversos agrupamentos e que estes são bastante conexos e interligados, tendo diversos vértices interligados uns com os outros aumentando assim o índice médio de clusterização.
Podemos perceber também, que o grafo é composto por apenas um componente, ou seja, existem pelo menos um caminho de um vértice para os demais.


![*Closeness* x Probabilidade](https://i.imgur.com/O7UDWZv.png){ width=50% }


### 2. Enron Email Network

![Grafo Enron Email](https://i.imgur.com/Ndp3gPS.png){ width=70% }

A rede de comunicação de e-mails da Enron dentro de um conjunto de dados de cerca de meio milhão de e-mails. Os vértices da rede são os endereços de e-mail e se o endereço *i* enviou pelo menos um e-mail para o endereço de e-mail *j*, forma-se uma aresta unidirecional entre os vértices *i* e *j*. O grafo contem  366692 vértices e 183831 arestas. 

#### **Métricas**

| Email | degrees     | distance     | clustering    |betweenness edges|betweeness vertex| components     | closeness    | 
|-------|-------------|--------------|---------------|-----------------|-----------------|----------------|--------------| 
| min   | 1           | 1            | 0             | 1,49E-09        | 0               |                | 0,114172     | 
| max   | 1383        | 13           | 1             | 0,016142        | 0,064851        | 33696          | 1            | 
| mean  | 10,020222   | 4,025143     | 0,496982      | 1,85E-05        | 6,95E-05        | 34,45258       | 0,307050     | 
| std   | 36,100004   |              | 0,002247      | 0,000073        | 0,000879        | 1.031,96       | 0,190206     | 

- Clusterização Global : 0,08531080
- Quantidade de Componentes: 1065

Como pode ser visto na imagem do grafo, o grafo não é fortemente conexo pois existem diversos vértices que não conseguem ser alcançados a partir de um vertice qualquer. Além disso, se observarmos os dados da métrica de grau, veremos que a distribuição de grau é bem discrepante, contendo muitos vértices com um grau baixo e poucos vértices com grau alto, mantendo assim a média baixa e a variação alta.

O grafo tem como maior distância entre dois vértices 13 arestas, e uma média de 4 arestas. Porém, vale a pena ressaltar que como o grafo não é fortemente conexo, existem pequenos componentes que não podem ser alcançados, gerando assim uma distancia infinita que foi desconsiderada para a realização do calculo.

	
![Clusterização x Probabilidade](https://i.imgur.com/GZdcJ8s.png){ width=50% }

O gráfico acima pode-se avaliar a distribuição dos índices de clusterização e a sua probabilidade. Podem perceber que existem diversos vértices com índice próximos de 0, porém uma boa parte está em uma componente em que muitos vértices se relacionam entre si, aumentando assim a media do índice de clusterização.

O gráfico abaixo é a representação do índice de *betweeness* do vertice pela probabilidade. Podemos concluir que a maioria dos vértices não fazem parte do menor caminho entre outros dois e que existem um numero baixo de vértices que funcionam como vertice de ligação entre outros dois formando assim, essa distribuição desequilibrada.

![*Betweeness* x Probabilidade](https://i.imgur.com/NPczzsy.png){ width=50% }

Como comprovado pelos dados de clusterização e de *betweeness*, os dados da métrica de componentes afirmam q existência de uma componente com mais de 92 por cento dados vértices e diversas componentes que não estão conectadas a componente principal. Dessa forma, a media do tamanho dos componentes é baixa, entretanto, o desvio padrão é elevado. 

![*Closeness* x Probabilidade](https://i.imgur.com/aT9mgRE.png){ width=50% }

Por último, o gráfico do índice *closeness* dos vértices pela sua probabilidade. Nos indica a existem de uma componente conexa grande, visto que a maior parte dos vértices possui centralidade entre 0,2 e 0,4. Além disso, nos valores de 0,0 até 0,2, estão a pequena quantidade de vértices que não estão na componente maior, justificando o seu índice. No fim da curva encontra-se vértices com alto grau e pertencentes a componente maior, justificando assim, seu alto índice de *closeness*.
![Grafo *High Energy Physics*](https://i.imgur.com/jbxPp1G.png){ width=70% }

O grafo *High Energy Physics* é uma rede de colaboração entre autores de artigos científicos da categoria de *High Energy Physics*. Os autores são representados pelos vértices e se um autor *i* for co-autor de um artigo com o autor *j*, forma-se uma aresta unidirecional entre *i* e *j*. Se o artigo for de *k* autorias, forma-se um sub-grafo completo entre esses vértices. O grafo possui 12008 vértices e 118521 arestas.


| Ph   | degrees     | distance | clustering    |betweeness edges|betweeness vertex| components   | closeness    | 
|------|-------------|----------|---------------|----------------|-----------------|--------------|--------------| 
| min  | 1           | 1        | 0             | 0              | 0               |              | 0,107145     | 
| max  | 491         | 13       | 1             | 0,004022       | 0,028025        | 11204        | 1            | 
| mean | 19,740340   | 4,67     | 0,611166      | 3,43E-05       | 0,000266        | 43,194245    | 0,266357     | 
| std  | 46,637997   |          | 0,003540      | 0,000087       | 0,000871        | 670,58964    | 0,182584     | 

- Clusterização Global : 0,65937213
- Quantidade de Componentes: 278
- **Métrica de Grau**

   
![Grau x Probabilidade](https://i.imgur.com/8A398Bs.png){ width=50% }

- **Métrica de Distância**
   

- **Métrica de Clusterização**
	

![](https://i.imgur.com/eynIYeg.png){ width=50% }

![Clusterização x Probabilidade](https://i.imgur.com/eynIYeg.png){ width=50% }


- **Métrica de *Betweeness***
	
![*Betweeness* x Probabilidade](https://i.imgur.com/aREtiC2.png){ width=50% }



- **Métrica de *Closeness***

![*Closeness* x Probabilidade](https://i.imgur.com/HtaBgax.png){ width=50% }
