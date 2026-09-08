self.veiculos e Sistema.veiculos nao sao a mesma coisa. Isso porque a primeira é uma variável de instância e a outra é uma variável de Classe. Self.veiculos, que no caso é uma lista, é um atributo de um Sistema (objeto) criado. Logo, cada objeto Sistema que eu criar (s1=Sistema(), s2=Sistema()) vai ter a sua própria lista veículos. Por outro lado, caso eu criasse Sistema.veiculos (que agora percebi que nem poderia ter feito isso, dado o código que escrevi em B1.py) seria uma lista compartilhada entre todos os objetos Sistemas que eu criasse.


Uma dataclass gera para mim três métodos importantes: o __init__, o __repr__ e o __eq__, sem que eu precise cria-los manualmente.O primeiro eh o metodo de iniciação da classe, o segundo é um método que facilita a vizualização do objeto e de seus atributos e o terceiro permite a comparação completa entre objetos. Isso torna a criação e manipulação de classes bem mais fácil para o programador, sendo uma ferramenta bem útil.


O __repr__ é usado separado de __str__ pois o primeiro eh uma vizualização mais completa e técnica do objeto (melhor para o programador) e o segundo é uma vizualização mais bonita e amigável, melhor para o usuário final do programa.


No programa vão existir 3 classes: Cliente, que vai ser usado para identificar quem é mensalista e quem não é, Veículo, usado para identificar e diferenciar cada tipo de veículo, e Sistema, usado para gerenciar entradas e saídas, controlar quem está estacionado, gerar relatório diário e calcular as tarifas.


