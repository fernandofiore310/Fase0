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