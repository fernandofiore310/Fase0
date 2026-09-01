# FASE 0 — REATIVAÇÃO

**Janela:** quinta 03/09 → quarta 16/09 (duas semanas, 30h)
**Objetivo de saída:** abrir o editor e resolver um problema sem travar em sintaxe;
modelar um domínio com classes que se justificam; operar git além de add/commit/push;
montar um projeto Python com estrutura, dependências e testes.

**Regra desta fase:** zero código gerado por IA. Explicação, dica, apontamento de erro
e exercício, sim. Solução, não. Vale para Claude, ChatGPT e Gemini.

---

## Antes de começar (30/08 a 02/09)

Esses três dias **não são de conteúdo técnico**. São de infraestrutura e de
candidatura aos clubes, que têm prazo e não esperam a Fase 0 terminar.

**Domingo 30/08 (3h) — montar o terreno**
- Python instalado e no PATH; VS Code com extensão Python e Ruff; git configurado
  (`user.name`, `user.email`, editor padrão).
- Criar o repositório em `C:\Users\<usuario>\dev\reativacao\`. Público desde já.
- Criar `LOG.md` (template no anexo A) e `BRIEFING.md` (o arquivo da conversa anterior).
- Colar o `BRIEFING.md` nas instruções personalizadas do ChatGPT e do Gemini. Testar
  se pegou: peça a qualquer um deles uma função simples e veja se ele te entrega o
  código. Se entregar, o briefing não está sendo respeitado e precisa ser reforçado.
- Primeiro commit.

**Segunda 31/08 (1h), terça 01/09 (2h), quarta 02/09 (3h) — clubes**
Candidaturas, currículo, o que estiver aberto. DataStory, Sports Analytics Group, MDB.

> ⚠️ **Não escreva Python entre hoje e quinta.** Se você aquecer antes, o diagnóstico
> mede um estado que não é o seu estado real, e eu calibro as duas semanas em cima de
> um número falso. O desconforto de quinta é o dado.

---

## Semana 1 — Quinta 03/09 a quarta 09/09

### Qui 03/09 — 4h — Diagnóstico a frio
Bloco nobre. Arquivo separado: `DIAGNOSTICO-D0.md`. Cronometrado, sem IA, sem busca.

Ao fim, escreva o autorrelato no `LOG.md` e **cole aqui na conversa** o log + o código
dos três blocos. Eu reviso antes do seu bloco de sexta.

### Sex 04/09 — 2h — Correção e primeira faxina
Com a minha devolutiva na mão e a documentação oficial aberta (não IA):
- Reescreva três exercícios do Bloco A que ficaram feios. Não os que você errou — os
  que você acertou de um jeito ruim. Errar é lacuna; acertar feio é hábito, e hábito
  demora mais para sair.
- Anote no `LOG.md` cada coisa que você precisou consultar. Essa lista vira o material
  dos drills de terça.

### Dom 06/09 — 3h — POO de verdade, parte 1
Reescreva o Bloco B do diagnóstico **do zero**, sem olhar a primeira versão.
Alvo conceitual desta sessão:
- Composição vs. herança — quando cada um, e por que herança é a escolha errada na
  maioria das vezes em que ela parece natural.
- `dataclass` — o que ela gera por você e o que ela não resolve.
- Interface: `Protocol` (duck typing tipado) vs. `ABC` (herança obrigatória).
- `__repr__` que serve para debug, não para o usuário final.
- Por que "adicionar um tipo novo não pode exigir mexer no calculador" é o critério que
  separa POO de `if/elif` disfarçado.

Leitura permitida **só depois de travar de verdade**, e específica: você abre a página
que responde à sua dúvida, não um capítulo inteiro "para entender melhor".

### Seg 07/09 — 1h — Revisão espaçada
Só revisão. Refaça de memória, cronometrado, três exercícios do Bloco A — os três que
você não terminou na quinta. Compare o tempo. Registre no `LOG.md`.

### Ter 08/09 — 2h — Drills de Python moderno
Bateria de exercícios curtos, gerados pelo ChatGPT a partir da sua lista de consultas
de sexta. Formato: 20 problemas de 3 a 6 minutos, sem projeto, sem contexto, só volume.
Eixos obrigatórios: comprehensions com condição, `enumerate`/`zip`, desempacotamento,
`sorted` com `key`, `collections` (`Counter`, `defaultdict`), f-strings com formatação,
generators, `pathlib`, exceções customizadas.

### Qua 09/09 — 3h — Ambiente e ferramental
Transformar o exercício de POO de domingo num pacote de verdade:
- Ambiente virtual e `pyproject.toml`. Entender a diferença entre dependência de
  execução e de desenvolvimento.
- Layout `src/`. Saber dizer por que ele existe e o que quebra sem ele.
- `pytest`: pelo menos seis testes, sendo um com `fixture` e um com `parametrize`.
- `ruff` rodando limpo. Não silencie regra que você não entendeu.
- `.gitignore` correto.

---

## Semana 2 — Quinta 10/09 a quarta 16/09

O artefato público da fase.

### O artefato: simulador de partidas de basquete

Um pacote Python instalável que simula uma partida posse a posse e emite o box score.
Nada de realismo estatístico — o objetivo é **design**, não fidelidade.

**Núcleo mínimo (obrigatório):**
- Modelagem de jogador e time, com atributos que influenciam o resultado da posse.
- Uma posse é uma unidade: recebe um estado, produz um evento (cesta de 2, de 3, erro,
  rebote, turnover, falta) e um novo estado.
- Pelo menos três estratégias de time intercambiáveis, implementando a mesma interface.
  Trocar de estratégia não pode exigir mexer no motor do jogo.
- Agregação: ao fim da partida, box score por jogador e placar por quarto.
- Aleatoriedade **injetada**, não importada dentro das classes. Isso não é preciosismo:
  é a única forma de a partida ser testável e reprodutível com semente fixa.
- CLI: rodar a simulação pelo terminal, escolhendo times e semente.

**Corte, se o tempo apertar:** derrube os quartos (simule 100 posses corridas), derrube
faltas e rebote ofensivo, derrube o CLI e deixe só a função de entrada. Não derrube os
testes nem a injeção de aleatoriedade — é neles que está o aprendizado.

**Esticada, se sobrar tempo:** substituições por minutagem, ou um segundo modo de saída
(JSON) sem alterar o motor.

### Qui 10/09 — 4h — Design antes de código
Primeira hora **sem escrever implementação**: escreva no README quais são as entidades,
quais são as fronteiras entre elas, onde está a interface que permite trocar estratégia,
e o que você decidiu *não* fazer. Depois implemente o núcleo do estado e da posse.

Se você começar a implementar antes de a primeira hora acabar, você está fugindo da
parte difícil. A parte difícil é essa.

### Sex 11/09 — 2h — Testes do núcleo
Teste antes de implementar o que falta. Alvo: com semente fixa, a mesma partida produz
sempre o mesmo box score, e a soma dos pontos do box score bate com o placar. Esse
segundo teste é o que pega bug de agregação.

### Dom 13/09 — 3h — Estratégias e motor
As três estratégias e o laço da partida. Ao terminar, o teste de troca de estratégia:
mudar a estratégia de um time altera o resultado sem tocar em nenhum arquivo do motor.

### Seg 14/09 — 1h — Revisão espaçada
Drills de git, sem projeto: `stash`, `rebase -i` para juntar dois commits, `cherry-pick`,
recuperar um commit "perdido" pelo reflog. Faça num repositório descartável.

### Ter 15/09 — 2h — Refatoração
`ruff` limpo. Type hints em toda função pública. Rode `mypy` e veja o que ele acha —
não precisa passar, precisa que você entenda cada reclamação. Elimine a duplicação que
apareceu entre as três estratégias.

### Qua 16/09 — 3h — Fechamento
- README final: o que o projeto faz, como rodar, e a seção de decisões de design —
  três a cinco decisões, cada uma com a alternativa que você descartou e o porquê.
- Histórico de commits legível. Se estiver sujo, limpe com rebase interativo.
- Push público.
- Relatório de fim de fase no `LOG.md` (template no anexo B). É ele que você cola ao
  abrir a conversa da Fase 1.

---

## O que não está nesta fase, e por quê

- **Algoritmos e complexidade.** É a Fase 1. Aqui, se você resolver em O(n²) e o código
  estiver claro, está aprovado.
- **Async, decorators, metaclasses.** Você não vai precisar disso para entrar em clube
  nenhum, e eles seduzem quem quer parecer avançado.
- **Docker, CI, deploy.** Fase 2 ou depois.
- **Frameworks web, pandas, numpy.** Fase 0 é Python puro de propósito. Biblioteca
  esconde a falta de fluência em vez de curá-la.

---

## Critério de aprovação da fase

Não é "terminei os quatorze blocos". É isto, e eu vou avaliar sem suavizar:

1. Você consegue escrever uma classe com dataclass, `__repr__` e type hints sem
   consultar sintaxe.
2. Você consegue explicar em voz alta por que usou composição em vez de herança em um
   ponto específico do seu código.
3. `pytest` roda, os testes passam, e pelo menos um deles falharia se você quebrasse a
   lógica de propósito.
4. O histórico de commits conta uma história.
5. O tempo dos exercícios do Bloco A caiu de forma perceptível entre 03/09 e 16/09.

Se três dos cinco não estiverem de pé em 16/09, estendemos a fase. Isso não é fracasso,
é informação — mas é informação que eu vou te dar sem embrulhar.

---

## Anexo A — Template do `LOG.md`

```
# LOG — Reativação Técnica

## Fase 0

### 2026-09-03 — Diagnóstico a frio (4h)
Bloco A: terminei X de 8 em 75 min. Travei em: ...
Consultas que precisei fazer: ...
Bloco B: ...
Bloco C: ...
Sensação vs. resultado: (onde eu achei que ia bem e não fui, e o contrário)

### 2026-09-04 — Correção (2h)
Reescrevi: ...
Aprendi: ...
Ainda não entendo: ...
```

Uma entrada por sessão. Três campos fixos em todas: **o que fiz**, **onde travei**,
**o que ainda não entendo**. O terceiro é o mais importante e é o que a maioria das
pessoas não escreve.

## Anexo B — Relatório de fim de fase

Ao fechar em 16/09, acrescente ao `LOG.md`:

- Os cinco critérios de aprovação, cada um com um veredito honesto e uma evidência
  (linha de código, commit, tempo cronometrado).
- Link do repositório público.
- Três conceitos que ainda estão frágeis. Eles entram na revisão espaçada da Fase 1.
- Horas efetivamente cumpridas vs. 30 planejadas. Se ficou muito abaixo, o problema é
  de agenda, não de conteúdo, e a Fase 1 precisa ser redimensionada.
