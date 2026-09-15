## ABC ou Protocol: Qual usar?

Decidi usar o ABC, isso porque, para ser sincero, foi a que eu entendi melhor. Sinceramente, nao entendi muito bem como o protocol funciona.
Vou chamar a classe abstrata que os tipos de automoveis herdam de "Veiculo".

## Questão do Mensalista

Sobre o mensalista, acredito que ele seria um atributo da classe Veiculo, de tipo bool. Caso todos os mensalistas fossem usuarios de carros, eu criaria esse atributo apenas na classe Carro, ja que moto e caminhao nem precisariam se preocupar com isso.
Considerando esse segundo caso do Carro, la eu poderia fazer uma condicao antes de calcular a tarifa se ele eh mensalista ou nao, atraves de uma verificacao do atributo.
No entanto, ai que caio no problema do if/else que conversamos bastante.
Logo, talvez eu poderia criar uma outra classe filha de Veiculo, que seria o mensalista. Isso nao seria um problema, pois como obviamente ele teria um veiculo, ele teria uma placa. Ai, a grande questao eh que ele teria um atributo proprio especifico, como self.horas que seria o que acompanharia as 200 horas mensais dele.
Ou, ate mesmo, filha da classe Carro mesmo. Pensei nisso em quanto desenvolvia o codigo. O unico problema eh que nao sei como eu posso fazer uma classe filha de uma outra classe filha. Posso tentar aqui.
Imagino que seja assim.

## Um mensalista é um tipo de veículo?

Refleti sobre o assuntoo agora, e na minha cabeça, de fato faz mais sentido o mensalista ser um tipo de veículo, e não um tipo de carro. Isso porque, (a) o mensalista, na teoria, pode dirigir qualquer tipo de veículo, a questão é que ele só vai ser cobrado como um carro. Logo, o que penso em fazer é criar a classe Mensalista herdando de veículo, criar o atributo de franquia único desse tipo de Classe e no método de calcular a tarifa, apenas copiar o do Carro. O fato do método de calcular a tarifa ser igual não deve justificar a herança.

## A franquia de 200 horas pertence a quê?

Pensei aqui, e talvez faça mais sentido a franquia pertencer ao mensalista. Inicialmente, havia pensado que faria sentido ele ser um atributo de veículo, onde para quem não é mensalista ele seria igual a 0. No entanto, a classe Sistema, vai apenas chamar o metodo de calcular a tarifa, e como esse eh um metodo abstrato, todo o seu corpo vai estar nas classes de "menor" herança, como Carro, Moto, Mensalista, etc. Logo, como apenas o Mensalista vai precisar referenciar ao atributo franquia, faz mais sentido criar esse atributo dentro dessa própria classe.

## Quando a franquia acaba, o excedente é cobrado como carro?

Vai ser a própria classe Mensalista que vai fazer essa conta. Ela basicamente vai ter o mesmo corpo do método de calcular tarifa da classe Carro, no entanto, sempre verificando o valor da franquia antes de iniciar qualquer iteração do método de calcular tarifa.

## Minha escolha

Escolhi criar a classe Mensalista, herdando de Veiculo, e dentro dela (Mensalista) criar o atributo de franquia e no seu método de calcular tarifa, basicamente copiar o método do Carro, porém com uma verificação da franquia antes de chegar nesse cálculo.

## Questão da dupla função de calcular tarifa de carro

Como escolhi herdar Mensalista de Veículo, preferi criar uma função "solta", no começo do arquivo, para evitar a repetição de código no meu arquivo. Preferi fazer dessa maneira, do que criar um atributo com valor Carro() na classe Mensalista. Isso porque, mesmo que eu so fosse usar a funcao de calcular a tarifa, ia parecer que todo o Mensalista dirige um carro, o que não é verdade e é o princípio que desenhei todo o corpo do meu código em cima.
