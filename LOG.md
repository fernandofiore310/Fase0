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

O que fiz:

Antes de atacar os exercicios, mandei a documentacao de ambiente virutal do python, git guides e documentacao do gitignore para o Gemini e pedi um resumo. Li e fui para os exercicios

No exercicio A1, fiz uma tatica que usei em todos os exercicios: usei muitos prints, de modo que pudesse ver o que cada coisa estava retornando. Primeira coisa que fiz foi percorrer a lista de entrada e deixar todos os nomes em minusculas.
Em seguida veio a parte que  acabei ficando mais tempo, que foi raciocinando como ia tratar os diferentes tipos de nomes que poderiam vir na lista. Tendo mapeado os tipos, tratei, com um b loco if/else primeiro os nomes que vinham com virgula e os que nao vinham. Comecei dando um split para separar nome e sobrenome e depois juntei eles usando a funcao format (eu lembrava que strings podiam ser somadas). Em ambos os blocos, usei algumas funcoes que perguntei para o Gemini e adicionei ao meu repertorio, dentre elas, o replace, que me ajudou a remover a virgula, e ate mesmo o join. Tambem, criei uma lista de preposicoes, para nao colocar maiusculas nelas. Tudo isso, sempre testando com varios prints e entendendo os estados.


No exercicio A4, lembrei de como adicionava valor e chaves a um dicionario vazio e tratei o testo de forma melhor. Usei o gemini para tirar a duvida da ordem alfabetica, e ele me apresentou o sorted, que me ajudou tanto nesse exercicio quanto em outros. Tambem, ele me apresentou o del, que tinha esquecido como usava, para tirar palavras que ja tinha adicionado a lista final da lista intermediaria.


No A2, tambem usei o gemini para me lembrar da funcao round, que arredondava para 2 casas decimais. Lembrei de usar o len tambem, que nesse exercicio foi bem importante. Tambem tratei o caso dos alunos que nao tinham notas registradas. E o gemini tambem me lembrou da funcao remove, que usei para tirar os alunos sem nota.


No A6, ja estava com o tempo mais curto, faltava cerca de 15 minutos para acabar. Usei o Chatgpt para gerar as 25 linhas de log. E de resto, fiz tudo por conta, sem problemas.


O A7 fiquei sem tempo para fazer infelizmente. Fa;tavam poucos minutos, cerca de 2, e nao sabia o que era yield. Teria que ler documentacao e passar um tempo pensando no raciocinio logico por tras.


Vale ressaltar, que em todos os exercicios, eu que criei a estrutura e o desenvolvimento do algoritmo. Nao usei nenhuma ajuda para pensar em COMO fazer o exercicio. O raciocinio logico por tras foi todo meu. O ponto era, por exemplo, quando queria tirar algo de uma lista, e nao lembrava de uma funcao. Nesse caso, consultava o gemini para me explicar que funcao eu poderia usar.


No Bloco 2, ativei o venv usando o resumo que o Gemini me passou da documentacao oficial do python. Aprendi a desativar (deactivate) e ativar de novo. Foi bem util.
Em seguida, rodei os dois casos que voce mencionou usando o where python. No entanto, em ambos os casos, o terminal nao mostrou nada, apenas aparecia que o comando tinha sido rodado, mas o terminal nao "printava" nada.
Depois, criei o arquivo .gitignore na raiz do repositorio, e com o resumo do gemini, montei meu proprio arquivo, e ainda coloquei comentarios didaticos para me ajudar. Comecei a ter nocao da funcionalidade de *, /, **, entre outros. 
Usei o comando git checkout para voltar para  a versao antiga do A7, que tinha apagado no Bloco 1. Entendi que eh como se fosse uma volta no tempo, visto que eu nao tinha commitado o exercicio A7 apagado ainda.
Criei a pasta BlocoC e coloquei dois arquivos, um deles com o que fiz na vizualizacao dos grafos e a minha interpretacao.
Em seguida, usei o comando git revert para reverter o commit teste que fiz. Peguei no Git Guides isso. Documentei tudo tambem na pasta BlocoC.
Removi a linha de teste do B1.py, e commitei separado tudo, no entanto, acredito que as mensagens nao seguiram o seu padrao.


Onde travei:
Acredito que usei bastante tempo nos exs do Bloco1. Como disse anteriormente, nas 1h30min de trabalho, fiz 4 exs, sendo que o A6 faltavam 15 minutos. Muito disso por conta de um raciocinio que ia se desenvolvendo aos poucos, e varios testes e tentativas e algumas mudancas na logica em alguns exercicios. No Bloco 2 acredito que nao travei, so levei mais tempo, pois estava lendo documentacao e preparando um .gitignore mais didatico.


O que ainda nao entendo:
Como vimos, toda questao de yield do A7, pois nunca vi isso em aulas. Alem do A8, que por masi que nao tenha aberto ele hoje, lembro que nao tinha muita ideia de como faze-lo.
As minhas duvidas sobre o segundo bloco estao nos documentos .md da pasta BlocoC. La vc vai ver as minhas duvidas.


Sensacao vs Resultado
Acredito que fui bem nos exericios que fiz. Bem melhor que ontem, mesmo com um exercicio incompleto por falta de tempo. Me senti melhor hoje programando com a consulta.


Consultas:
Gemini

https://docs.python.org/pt-br/3/tutorial/venv.html

https://git-scm.com/docs/gitignore

https://github.com/git-guides