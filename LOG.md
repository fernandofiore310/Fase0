# LOG — Reativação Técnica

## Fase 0

### 2026-08-31 — Antes de começar
Realizei todo o setup em 1h:30min cravado.
Gastei bastante tempo entendendo sobre git, visto que estava enferrujado e quis criar o meu repositório via terminal. Foi uma tarefa difícil. Fiquei com dúvidas que vou usar o Gemini para me ajudar.
Também tive dúvida sobre as intalações do vs code, python e do git, no sentido de que não sabia em que local estavam sendo instaladas essas aplicações.

### 2026-09-03 — Diagnóstico a frio (4h)
Bloco A: 


No Bloco A, nao consegui completar nenhum exercicio. Teve uns que fui melhor que outros, mas em geral nao fui bem. Vou resumir como foi minha performance em cada um.


A1: Nesse tive dificuldade. No comeco, fiquei batendo cabeca, pois nao lembrava como escrever as funcoes lower e upper. Alem disso, tinha esquecido totalmente de funcoes como .split e outras (lembrei no A6). Logo, fiquei quebrando a cabeca para pensar em um bom raciocinio e acabei perdendo muito tempo nisso. Logo, depois de um tempo entre 15-20 minutos, decidi ir para o proximo exercicio.


A2: Nesse exercicio acredito que fui um pouco melhor que o anterior. No comeco, esqueci como usava os metodos .keys, .values e .items. Testei e vi como os escrevia da maneira correta. Calculei as medias das listas (tive um problema que esqueci a funcao que pega o tamanho da lista de uma vez, entao tive que usar um contador para isso, not very optimal) e consegui criar as tuplas com nomes e medias e coloca-las numa lista de tuplas. Na parte de pegar o top tres, a minha ideia era fazer um loop que percorria o bloco de codigo 3 vezes, no entanto, pensei em um raciocinio qualquer e estava meio apertado com o tempo, entao acabei esquecendo algumas coisas como atualizar o contador, entre outros.
Alem de tudo isso, esqueci como arredonda para 2 casas decimais e nao sabia como organiza-los por ordem alfabetica.
Outro exercicio que tive que prosseguir para o outro por conta de tempo.


A3: Esse aqui acredito que fui um pouco melhor. Consegui criar uma lista com todas as diferentes categorias nos diferentes dicionarios. E acredito que consegui criar a tupla que precisava colocar como valor do dicionario de categorias. No entanto, por estar apertado de tempo tambem, acabei nao criando o dicionario, para tentar otimizar meu tempo.


A4: Nesse exercicio, acredito que consegui percorrer o texto. Nao sei se o jeito que evitei pontuacoes foi o jeito mais eficiente de se fazer. Alem disso, nao consegui pensar em um metodo para pegar as n palavras mais frequentes de um modo que nao fosse comer todo o meu tempo de diagnostico. Novamente, nao sabia como organizar as palavras ordem alfabetica.


A5: Esse aqui tive o mesmo problema de ter esquecido a funcao para pegar o tamanho das listas. Acabei perdendo um tempo tentando. Quando fui pensar em como fazer a janela movel, nao consegui pensar em como fazer rapido, e por isso, decidi pular para o outro exercicio por uma questao de tempo.


A6: Nesse exericio, nao criei a lista com 25 linhas simulando o log, por questao de tempo. Nesse exercicio foi quando lembrei da existencia do metodo split (pensando agora, poderia ter usado o split passando ','como argumento, mas na hora nao passou pela minha cabeca). Acredito que consegui contar o numero de erros, porem na hora, nao consegui pensar em como conta-los por hora do dia e como criar o retornavel. Tambem nao queria perder muito tempo.


A7: Aqui, acredito que consegui criar a sequencia corretamente, nao sei se usei o codigo mais eficiente para fazer isso, mas consegui. Depois, apenas somei todos os elementos da lista e retornei.


A8: Esse aqui, estava com o tempo muito apertado (faltavam cerca de 3min e 30seg) e nao sabia como fazer esse exercicio. Logo, apenas abracei a derrota, passei rapidamente pelos outros exercicios e acabei.


Consultas que precisei fazer: Nesse Bloco, assim como as suas intrucoes falavam, nao consultei nada. Fiz tudo de cabeca.


Bloco B:


No Bloco B, comecei lendo a domcumentacao oficial do Python sobre classes para ir retomando os meus conhecimento no assunto, uma vez que nessa secao voce mencionou que eu poderia realizar consultas as documentacoes oficiais.
Entao aqui comecei criando a classe Cliente, que basicamente tinha os atributos que diferenciavam cada tipo de veiculo do outro.
Na classe Sistema, que representava o gerenciamento do estacionamento em si, comecei criando um metodo que registrava a entrada de um cliente no estacionamento.
Nessa parte, nao fazia ideia de como pegar o tempo ideal, acabei usando a biblioteca time, que acaba devolvendo o tempo em segundos, mas isso acabou gerando problemas na hora de pegar o tempo para o mensalista, visto que ele tinha aquelas 200 horas por mes, o que acabou complicando as minhas contas. No entanto, funcionou corretamente, acredito, para os outros tipos de clientes.
Tinha criado um metodo separado para calcular o valor que cada cliente deve para o Sistema, no entanto, depois percebi que poderia ter colocado isso junto com o metodo que registra a saida do cliente. E fiz isso.
Acredito que consegui calcular o quanto cada um deve (so nao tenho muita certeza quanto ao mensalista).
Em relacao a lista de veiculos estacionados, fiz ela, no entanto nao tenho certeza se fiz da melhor maneira e se esta correta.
No fim, vi que tinha que fazer o relatorio, que decidi fazer em formato de dicionario, onde acredito que consegui devolver corretamente os dois tipos de faturamento, porem, nao consegui calcular a permanencia media. Nao sei como poderia fazer isso e nao sei se o time possa ter me atrapalhado nessa tarefa.
Tinha criado a funcoa gera relatorio, no entanto, acabei nao usando ela, e apenas a usei para fazer um teste do Bloco C.
Nao coloquei type hints (pesquisei na hora o que era para entender, e acabei nao colocando). Tambem, nao sei o que eh o __repr__ que voce mencionou. E tambem, nao sabia usar o pytest, alem de estar com o tempo corrido para fazer os testes. Logo, nao testei nada do meu codigo.


Aqui, verifiquei a documentacao do python para classes principalmente.
https://docs.python.org/3/tutorial/classes.html
https://docs.python.org/pt-br/3.9/library/datetime.html#time-objects


Bloco C:


Aqui realmente acredito que nao mandei bem, mas vou explicar direito o que aconteceu.
Dos 45 minutos que esse bloco tinha, fiquei 30 minutos na parte do ambiente virtual. Basicamente, fiquei lendo a pagina do python sobre ambientes virtuais (https://docs.python.org/pt-br/3/tutorial/venv.html)
Primeiramente, tentei criar um ambiente virtual, mas nao sabia muito bem o que estava fazendo. Acredito que usei o seguinte comando: python -m venv \Users\ferna\dev\reativacao\Fase0 o que acabou criando um ambiente virtual chamado Fase0, que o seu gitignore tinha um *, que basicamente estava fazendo meu repositorio ignorar a pasta /diagnostico. Ai, ate eu entender que o erro era esse demorou um certo tempo e acabou me prejudicando bastante. Alem disso, depois ainda criei um outro ambiente virtual, chamado venv, enquanto esse Fase0 continuava funcionando, o que me deixou mais confuso ainda, com duas pastas Scripts, dois gitignores, etc. Li mais sobre a documentacao no site do git, e entendi que quando tinham dois gitignores o git considerava o de highest precedure. Entao o que fiz foi apagar tudo do ambiente Fase0.
Alem de tudo isso, nao ativei nenhum dos ambientes com comando. Eles basicamente ativavam sozinhos quando eu abria uma nova janela do terminal interno do vs code. Eu lembrava de usar um comando especifico para ativa-lo nos projetos da faculdade (mas usava Linux, o que poderia ser diferente).
No fim das contas, nao precisei escrever nada no gitignore do ambiente venv. Ele ja veio escrito (veio apenas com o *) e ja evitou que tudo dele subisse para o meu repositorio.
Nos 15 minutos restantes, consegui realizar o commit do Bloco B corretamente. Alem disso, consegui criar a nova branch, realizar as mudancas, fazer o pull request, fazer o merge, provocar o conflito e enfim arrumar o conflito.
Nao vizualizai o historico com o grafo de branches, pois nao sei usar e tinha pouquissimo tempo. Tambem nao desfiz o ultimo commit preservando o historico e nem expliquei as diferencas (passos 6 e 7) pois tambem fiquei sem tempo.

Basicamente como consulta usei:
https://docs.python.org/pt-br/3/tutorial/venv.html
https://git-scm.com/docs/gitignore
https://docs.python.org/3/library/venv.html
https://github.com/git-guides#create-a-branch



Sensacao x Resultado

Aqui para ser sincero, achei que ia um pouco melhor no Bloco A, mas acredito que fui pior do que esperava. Esperava que pelo menos o meu raciocinio logico de programacao estivesse mais afiado, no entanto, acho que todo o tempo parado e escrevendo codigos com IA acabaram enferrujando-o.

No Bloco B, em relacao a POO, eu achava que ia mandar muito mal, mas fui um pouco melhor do que esperava. Mas mesmo assim, acredito que tenha bastante coisas para melhorar, pois acredito que nao era um problema tao dificil. Ja em relacao ao pytest mencionado, realmente nao sei fazer.

No Bloco C, achava que ia me dar melhor com a questao do ambiente virtual, no entanto, acabei mandando bem pior do que eu esperava. Realmente comeu bastante tempo do meu desenvolvimento.
Ja em relacao aos comandos git, achei que fui como esperava ir. Git eh algo que vamos acabar usando bastante e tenho certeza que vou ir melhorando e entendendo com o tempo.

### 2026-09-04 — Correção (2h)
Reescrevi: ...
Aprendi: ...
Ainda não entendo: ...
```

Uma entrada por sessão. Três campos fixos em todas: **o que fiz**, **onde travei**,
**o que ainda não entendo**. O terceiro é o mais importante e é o que a maioria das
pessoas não escreve.