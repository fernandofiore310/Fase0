# DIAGNÓSTICO A FRIO — quinta 03/09, 4h

## Antes de começar, leia isto uma vez

Este teste **foi desenhado para não ser terminado**. Se você terminar tudo, o
instrumento é que estava mal calibrado. O objetivo não é a nota, é o mapa: onde você
travou, quanto tempo levou, o que precisou consultar.

Por isso a única forma de invalidar o diagnóstico é trapacear com você mesmo — pular a
anotação de consultas, estourar o cronômetro em silêncio, ou "só dar uma olhadinha" no
ChatGPT. Um diagnóstico ruim me faz montar as duas semanas erradas.

**Regras:**
- Cronômetro visível. Cada bloco tem tempo fechado. Estourou, para.
- Bloco A: **nada**. Sem IA, sem busca, sem documentação, sem autocompletar de IA no
  editor (desligue o Copilot se estiver ligado).
- Blocos B e C: documentação oficial liberada. IA continua proibida.
- Toda consulta que você fizer, anote: o que procurou e em que exercício.
- Não apague nada. O código feio é dado.

Crie a pasta `diagnostico/` no repositório. Um arquivo por bloco.

---

## BLOCO A — Fluência bruta · 75 min · sem consultar nada

Oito problemas. Python puro: nada de `pandas`, `numpy` ou qualquer pacote externo. A
biblioteca padrão está liberada, e saber que ela existe faz parte do que está sendo
medido.

Marque o horário ao começar cada um. Se um problema passar de 12 minutos, pule e siga.

**A1.** Recebe uma lista de nomes escritos de forma inconsistente — `"silva, joão"`,
`"JOÃO SILVA"`, `"  joao   silva "`, `"Maria de Souza"` — e devolve a lista normalizada
no formato `"João Silva"`, sem duplicatas, em ordem alfabética. Decida você o que fazer
com as preposições (`de`, `da`, `dos`) e registre a decisão em um comentário.

**A2.** Recebe um dicionário que mapeia aluno para lista de notas. Devolve os três
alunos de maior média como lista de tuplas `(nome, média)`, média arredondada em duas
casas, desempate por ordem alfabética. Alunos sem nota não entram.

**A3.** Recebe uma lista de dicionários representando transações, cada uma com `id`,
`categoria`, `valor` e `data`. Devolve um dicionário que mapeia cada categoria a uma
tupla com total, quantidade e maior valor individual daquela categoria.

**A4.** Recebe um texto e um inteiro `n`, e devolve as `n` palavras mais frequentes,
ignorando maiúsculas e pontuação, e descartando uma lista de stopwords que também vem
por parâmetro. Empate resolvido em ordem alfabética.

**A5.** `janela_movel(seq, k)` devolve a lista das médias de cada janela deslizante de
tamanho `k`. Sem bibliotecas de array. Defina e trate os casos degenerados: `k` maior
que a sequência, `k` zero ou negativo, sequência vazia.

**A6.** Você cria à mão um arquivo de texto com umas 25 linhas simulando um log, no
formato `2026-09-03 14:22:07 ERROR mensagem aqui`, misturando níveis `INFO`, `WARNING`
e `ERROR`. Escreva a função que lê esse arquivo e devolve a contagem de linhas `ERROR`
por hora do dia. O arquivo deve ser lido por caminho, não por conteúdo colado.

**A7.** Um gerador que produz números de Fibonacci enquanto forem menores que um limite.
Depois, usando esse gerador, some os pares. O gerador não pode construir a lista inteira
na memória.

**A8.** `tentar(funcao, max_tentativas)` executa `funcao()`. Se ela levantar exceção,
tenta de novo até `max_tentativas`, registrando cada tentativa numa lista. Se todas
falharem, levanta uma exceção customizada sua que carregue o histórico de tentativas e
a última exceção original. Se alguma der certo, devolve o resultado.

Ao fim dos 75 minutos, anote: quantos terminou, quais ficaram pela metade, e em qual
você perdeu mais tempo.

---

## BLOCO B — Modelagem orientada a objetos · 75 min · documentação liberada

Um problema só. Domínio deliberadamente sem graça, para que o que esteja em teste seja
o desenho e não o seu interesse pelo assunto.

### Sistema de cobrança de um estacionamento

Registra entrada e saída de veículos e calcula o valor devido.

Regras de tarifação, hoje:
- **Carro:** primeira hora cheia por R$ 12, cada hora adicional ou fração por R$ 8.
- **Moto:** metade da tarifa de carro, mesma estrutura.
- **Caminhão:** taxa fixa de entrada de R$ 25 mais R$ 15 por hora ou fração, sem
  primeira hora especial.
- **Mensalista:** não paga por permanência, mas tem franquia de 200 horas no mês. O que
  passar disso é cobrado como carro.

O sistema precisa: registrar entrada, registrar saída calculando o valor, listar o que
está estacionado agora, e emitir um relatório do dia com faturamento total, faturamento
por tipo de veículo e permanência média.

**Os três requisitos que estão realmente sendo avaliados:**

1. Adicionar um tipo novo de veículo — digamos, ônibus — **não pode exigir alteração na
   classe que calcula o valor**. Se você precisar mexer nela, seu desenho não passou.
2. Toda função e método com type hints. Toda classe de domínio com `__repr__` útil para
   debug.
3. Pelo menos três testes com `pytest`, sendo um deles do caso de fração de hora.

Se você nunca usou `pytest`, tente mesmo assim e anote onde emperrou. Essa informação
vale mais para mim do que o teste funcionando.

---

## BLOCO C — Git e ambiente · 45 min · documentação liberada

Tarefas descritas como objetivo, não como comando. Descobrir o comando faz parte.

1. Ambiente virtual criado e ativo. `pytest` e `ruff` instalados dentro dele.
   Dependências declaradas em arquivo versionado.
2. `.gitignore` que impeça de subir o ambiente virtual, os caches de bytecode e
   arquivos de configuração local.
3. O Bloco B commitado em pelo menos três commits, cada mensagem descrevendo a intenção
   da mudança, não o arquivo alterado.
4. Um branch novo. Nele, altere uma linha específica de um arquivo do Bloco B. Volte ao
   branch principal e altere **a mesma linha** de forma diferente. Faça o merge, provoque
   o conflito, resolva.
5. Visualize o histórico com o grafo de branches e escreva, em duas ou três frases num
   arquivo de texto, o que aconteceu ali.
6. Desfaça o último commit **preservando o histórico** — sem reescrever o passado.
   Depois, num arquivo só, descarte alterações ainda não commitadas.
7. Diga por escrito qual é a diferença entre descartar uma alteração não commitada,
   desfazer um commit preservando histórico, e apagar um commit do histórico. Se você
   não souber, escreva "não sei" — é resposta válida e é informação.

---

## FECHAMENTO · 20 min

Escreva a entrada no `LOG.md`:

- Bloco A: quantos de 8, tempo por problema, onde travou.
- Lista completa das consultas feitas nos Blocos B e C.
- Bloco B: o desenho que você escolheu, em três frases. E: você conseguiu satisfazer o
  requisito 1 (tipo novo sem mexer no calculador)? Como sabe?
- Bloco C: quais das sete tarefas você concluiu.
- **Sensação vs. resultado:** onde você achou que ia bem e não foi, e onde você achou
  que ia mal e foi. Essa é a linha que eu mais leio.

Depois, cole aqui na conversa: a entrada do `LOG.md` e o código dos três blocos, do
jeito que ficou. Não limpe, não conserte, não reescreva antes de mandar. Eu devolvo a
análise antes do seu bloco de sexta.
