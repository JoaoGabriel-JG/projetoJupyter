import csv
import sys
import matplotlib.pyplot as plt
from datetime import datetime

"""
import csv para trabalhar com arquivos csv
import sys aumenta o limite de dados de um csv para se trabalhar
import matplotlib é uma lib para criação e edição de gráficos
import datetime usado para manipular os valores de tempo
"""

dates = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'out', 'Nov', 'Dez']
qntd = [0] * 12

"""
As datas dentro de um array
E o array de quantidade com 12 casas 
"""

with open ('Novos.csv', 'r') as csvfile:
    csv.field_size_limit(sys.maxsize)
    path = csv.reader(csvfile, delimiter=';')
    
    for row in path:
        data = row[6]
        
        if not 'Data de abertura' in data:
            d = datetime.strptime(data, '%Y-%m-%d %H:%M')
            qntd[d.month - 1] += 1
            
plt.plot([0, len(dates)], [max(qntd), 0], 'k--', linewidth = 1)
plt.plot([1, len(dates)], [max(qntd), 1], 'k--', linewidth = 1)
plt.plot([2, len(dates)], [max(qntd), 2], 'k--', linewidth = 1)
plt.plot([3, len(dates)], [max(qntd), 3], 'k--', linewidth = 1)
plt.bar(dates, qntd, color = 'g', width = 0.80, label = 'Problemas')
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.title('Novos Problemas - 2022')
plt.legend()
plt.show()

"""
Primeiro abrir o csv e tirar o limite dele, utilizando a lib sys e também delimitar por ; que é a separação do 
arquivo
Logo após fazer uma seleção do row 6 onde estão as datas
Filtrar as informações com if not pegando somente as datas
E por ultimo montar o gráfico com a matplotlib
"""




"""
Eu e o Leo procuramos uma melhor forma para demonstrar as informações em um gráfico e achamos a solução com a 
matplotlib e assim pensamos em como resolver alguns problemas que deram no começo como a questão de filtrar
somente a quantidade de meses do csv, e para isso encontramos a datetimelib e conseguimos seguir sem problemas, a 
nossa preferencia foi o gráfico em barras por ser melhor de utilizar com a linha de tendencia ficando mais visivel.
"""
