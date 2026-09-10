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


### 2026-09-06 — POO e correção de bugs (2h)

O que fiz:

No Bloco 1, precisava consertar os bugs de 4 exercícios do Bloco A do diagnostico dentro de 30 minutos. Fiz na ordem A1, A2, A4 e A6. No entanto, dentro do limite de tempo, só consegui fazer os três primeiros. Não deu tempo de arrumar o último.
No exercício A1, troquei o metodo de deixar a primeira letra do nome maiuscula usando manipulacao de strings ao inves do replace que estava usando antes, que basicamente bugava quando tinha nomes em que a letra inicial era repetida, como anna. E tambem, retornei a lista sorted para arrumar o problema da ordem alfabetica.
No A2, arrumei todos os problemas. Acredito que o meu problema era o fato de eu nao ter entendido muito bem a diferenca entre um aluno sem nota e um aluno que tirou 0. Pra mim, eram a mesma coisa. Quando entendi a diferenca, consegui consertar.
No A4, foi mais tranquilo, tanto que foi o que resolvi mais rapido (todos os tempos estao na mensagem de commit individual de cada exercicio). Arrumei a questao do return e das stopwords muito rapido, visto que eram erros de atencao, e o da pontuacao, apenas criei uma lista, percorri as palavras e usei um replace.
Infelizmente nao deu tempo de fazer o A6, logo, nem toquei no exercicio.


No Bloco 2, comecei usando o terminal python e o Gemini para entender certinho a funcionalidade do yield e funcoes geradoras.
Tendo lido e testado, comecei a programar. A principio, estava usando a lista de novo. Com um aviso do Gemini, percebi que nao era essa rota. Pensei em um raciocinio e apliquei no meu codigo. Fiz o codigo em cerca de 19 minutos.


Depois, no Bloco 3, pedi a aula para o Gemini e sanei umas duvidas que tinha. Particularmente nao conhecia o dataclass, o repr, o str e o eq, entao foi bom para pegar uma visao daora.


O negocio foi no Bloco 4. Mesmo com o tempo que tinha para desenvolver o codigo e a aula do Gemini, mesmo assim nao fiz o exercicio completo, por sinal, acredito que ele esteja bem cru ainda. 


Onde travei:
A unica coisa que posso dizer que "travei" (nao fui muito bem uma travada) foi no Bloco 4. Por mais que eu tenha tido a aula, a estrtura que o codigo deveria ter apenas nao estava surgindo na minha cabeca. Tanto que, a adicao da classe veiculo e cliente, e o atributo de placa que criei para diferenciar os veiculos, foi algo que o Gemini acabou provocando e me fez pensar. Nao foi uma ideia que eu pensei no momento que o timer comecou a rodar.


O que eu ainda nao entendo:
Ainda nao saquei como pode ser tao mais vantajoso o uso de funcoes geradoras. Sei la, na minha cabeca era mais util ter uma funcao que retornasse direto o que era pedido, ao inves de algo que eu preciso ficar chamando mais de uma vez.

Ja no Bloco 4, o meu problema eh mais entender a estrutura e onde tem que ir certas coisas. Por exemplo, quando acabou o exercicio, fui tirar umas duvidas com o gemini, e ele disse, por exemploi, que o horario de entrada e saida deveriam ser atualizados por um metodo dentro de veiculos, e nao de Sistema (que era o que eu pensava que era o correto). Logo, acredito que falta uma certa experiencia, ou talvez um entendimento de estrutura e de "o que fica em que lugar" e coisas do tipo. Na minha cabeca era bem mais simples desenvolver um estacionamento. Nao sei como nao usar os bloco de if/else para diferenciar os veiculos, mesmo voce falando que nao era o correto. E usei um dicionario para simular o estacionamento, mas novamente, foi algo que o Gemini me provocou. Eu ia usar uma lista, que realmente nao faz muito sentido usar.
Em conclusao, acredito que meu problema nao esta muito em entendimento de instancias, classes, atributos etc. Esta mais na parte de montar o diagrama do Sistema completo e saber/ter mais clareza sobre o que cada classe deve ter e fazer.


Sensacao vs. resultado
Acredito que mandei mal no Bloco 4. De resto acho que fui bem.


### 2026-09-07 — Revisão (1h)

O que fiz:
Fiz o exercício A6 da maneira correta. Fiz ele eu um tempo de 11-12 minutos, e depois fiquei mais 12 apenas tirando duvidas com o Gemini e fazendo comentários no arquivo.
Depois, fiz o A1 de cabeça, mas não consegui fazer em under 15 minutos.
Por fim, atualizei o .md do Bloco C.
E ainda sobrou uns 12 minutos da 1 hora disponível.

Onde travei:
Teve alguns momentos no desenvolvimento do A1, em que eu estava tentando raciocinar em como fazer o exercício, no entanto, acreddito que o fato de ter um tempo curto acabou me deixando meio ansioso, o que nao me fez pensar com calma, e acho que perdi uns minutos com isso.

O que eu ainda nao entendo:
Acho que estou tranquilo quanto a revisao de hoje.


Sensacao vs. resultado
Fui bem, mas esperava que concluísse o A1 em under 15, algo que não aconteceu.


### 2026-09-08 — Drills (2h)

O que fiz:
Fiz os 20 exs do drill. Os tempos de cada bateria estao na mensagem de commit. Mas dos 100 minutos que tinha disponivel para faze-los, fiz em 76minutos e 30segundos.
Nao foram todos os exercicios que acertei de primeira, mas eventualmente consegui arrumar todos. So teve um no qual estourei o tempo limite (todos os tempos estao documentados como comentarios em cada arquivo de exercicio).
Todas as minhas consultas de funcoes e python foram com o gemini. Usei o gpt para discutir alguns contextos e motivos sobre as minhas respostas dos exercicios.

Onde travei:
Nao diria que travei, mas teve algumas coisas que tive que tirar um tempo para ler sobre, entender e ver como usar no exercicio. Dentre elas estao o any() e o all(), o max e sorted com o parametro key, o list e dict comprehension, o zip, e todas os metodos da colecao collection que o chat pediu para usar (Counter e defaultdict).

O que eu ainda nao entendo:
Nao vou falar que estou com todo o conteudo de hoje quentinho e decorado, mas acredito que nao hora que consigo identificar um problema que pode ser resolvido com essas ferramentas, e entao, vou ler a documentacao dessas funcoes para lembrar sobre a estrutura delas.


Sensacao vs. resultado
Acredito que fui bem, considerando o tempo abaixo do tempo total e que apenas estourei o tempo de 6min em um exercicio.


### 2026-09-09 — Fixação e conteúdo novo (3h)

O que fiz:
Basicamente, comecei estudando os 4 contúdos que você me passou, mas principalmente focando nas duas primeiras perguntas da leitura dirigida, que eram sobre Packaging em python. Vou ter que admitir algo, passei bem dos 25 minutos, pois fui ficando curioso e fazendo mais perguntas e anotando cada vez mais coisa, o que consumiu bastante tempo, e mais importante, consumiu bastante da minha energia.
Mas, entendi o que é um pacote e o que significa empacotar, que é basicamente disponibilizar certos códigos e arquivos para que possam ser usados em outro ambiente, diretório, e até mesmo outra máquina (essa parte de ver em outra máquina não me aprofundei tanto), e entendi o que o pyproject.toml é responsável (imagino que isso seja uma mudança recente, pois lembro de trabalhar em um projeto da faculdade no primeiro semestre de 2024 e usar steup.py ainda). Entendi sobre o build-system e o project, sobre o Build-backend (por mais que eu ainda não saiba qual o melhor tipo para se usar) e Build-frontend (que é onde o usuário interage). Também entendi sobre os dois diferentes formatos de distribuição que o backend gera e entendi a importânncia de sempre criar o projeto que você quer empacotar na pasta src/. Por fim, ficou claro também a diferença dos dois tipos de dependências que o meu projeto tem.
Como gastei bastante tempo e energia nessa parte, passei um pouco rápido pelo pytest, onde pedi uma aula para o Gemini, mas acredito que eu tenha entendido sua função: testar o seu código, para ver se o resultado que você quer está saindo como você espera. Isso evita o uso de vários prints ao longo do código. O fixture e o parametrize eu entendi a função até, mas tenho que admitir que a implementação não foi tão boa (vou explicar mais para frente).

No Bloco 2, li bem rápido sobre ABC e Protocol. Tenho que admitir que não me esforcei muito para tentar entender o Protocol, e foquei só no ABC, que pelo que entendi, é uma ferramenta que permite classes filhas absorverem o conteúdo de uma classe pai, sem precisar repetir código. Criei o documento docs/classes.md e escrevi bem brevemente e até com uma certa falta de vontade o que fiz.

No Bloco 3, comecei criando a pasta src/, e passei as instruções do Claude do Bloco 3 para o Gemini e falei para ele me ajudar a pensar em como resolver, porém sem dar respostas. 
Então, a primeira coisa que fiz foi pesquisar na internet sobre o arquivo __init__.py e ver que podia não colocar nada dentro dele, e que ele era apenas um arquivo que tornava o meu projeto "importável". Em seguida, desenvolvi sozinho o project.toml, tirando algumas dúvidas com o Gemini, como qual versão do Python colocar, se eu podia escolher a version, e quais versões colocar de ruff e pytest.
Depois, rodei o pip install -e, que confesso que ainda não entendi o porque de usa-lo (a flag -e no caso, sei que o pip install é quem roda o pyproject.toml). Mas deu certo e consegui rodar em outro diretório.
Por fim, vi que não precisava trocar o nome do ambiente virtual no .gitignore.

Em seguida parti para o desenvolvimento, onde acredito que fui bem melhor do que das vezes anteriores (fiz no arquivo src/projeto_estacionamento/main.py). Nem tentei fazer o mensalista, e tive problemas em pensar como gerar o relatório. Talvez com mais tempo em mãos eu conseguiria pensar em algo. Mas acredito que fui bem melhor quando ao desenvolvimento das diferentes Classes e seus métodos e atributos. Peguei esse função field com o Gemini e tirei uma dúvida de um erro com o Claude.

Feito isso, fui para a parte de testes, onde consegui escrever umas linhas mas não consegui rodar o arquivo. Quando clicava na seta so canto superior direito para rodar o arquivo test_estacionamento.py que criei, ele rodava o main.py, algo que não entendi. Então não consegui ver muito bem se está certo. Além disso, o tempo acabou quando tinha acabado de escrever o código do parametrizer, que acredito que esteja errado.

Por fim, rodei o ruff (pedi ao gemini o comando pois não sabia como usá-lo), e não li o que ele devolveu, apenas colei no arquivo src/projeto_estacionamento/ruff_result.md.

Onde travei:
Diria que dei uma travada na hora de escrever e rodar os pytests. 
E diria que travei na hora de pensar em como fazer para gerar o relatório, contar o faturamento total e por catergoria. E também um pouco no que colocar como valor no dict de estacionamento.


O que eu ainda nao entendo:
pip intall -e. Sei que ele é o Build-Frontend, mas tipo não entendi o que a flag -e faz de diferente.
Não estou mandando tão bem ainda na aplicação e desenvolvimentos de testes com pytest.
Não entendi o Protocol ainda.
E não li o que o ruff devolveu, então não sei como usá-lo para melhorar meu código.

Sensacao vs. resultado
Acredito que não soube respeitar o tempo, o que me desgastou e me prejudicou no resto. Sempre faço isso com teoria nova: quero entender todos os minimos detalhes sem aplicar e construir toda a história e o funcionamento passo a passo das coisas, que acabo me desgastando muito com isso e acabo me ferrando.