# jsdict
Dicionário python que implementa também a notação de ponto, igual a usada em JavaScript

Exemplo de uso
import JSDict

jsdict = JSDict.JSDict()
jsdict.name = "some name"
jsdict.tel = {"home": "975246585", "office": "98542885", "work": {"morning": "942862865", "evening": "905455855"}}

Podemos adicionar informações no dicionário com a notação de colchetes (principalmente quando as chaves são números ou palavras reservadas) e também podemos usar a notação de ponto. No exemplo do código acima, pra acessar o número de telefone do trabalho no período da noite, todas essas notações são válidas.

jsdict["tel"]["work"]["evening"]
jsdict.tel.work.evening
jsdict.tel["work"].evening
jsdict["tel"].work["evening"]


Para criar um JSDict podemos inicializar o objeto sem argumento (cria um dicionário vazio) ou podemos inicializá-lo com qualquer expressão válida para criar um dict python. E o JSDict aceita todos os métodos pertencentes a um dict python.
