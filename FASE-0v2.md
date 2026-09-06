# FASE 0 — REATIVAÇÃO (revisão 2, 06/09)

**Janela:** quinta 03/09 → quarta 16/09
**Estado:** diagnóstico e primeira correção concluídos. Este documento substitui a versão
de 30/08.

**Regra da fase:** zero código gerado por IA. Explicação, exercício, apontamento de erro
e leitura de documentação, sim. Solução, não.

---

## O que mudou, e por quê

A versão original partia de "base sólida, fluência perdida". O diagnóstico de 03/09
mostrou outra coisa: lacunas conceituais, não apenas de fluência. Três mudanças.

**1. A teoria virou bloco explícito.** A regra "ler só depois de travar" estava certa
para fluência — não saber `len` ou `sorted` se resolve travando e consultando. Mas
ninguém deduz sozinho a diferença entre variável de classe e de instância. Conceito
precisa de exposição antes da tentativa. Todo bloco de conteúdo novo passa a começar com
20 a 30 minutos de leitura dirigida, com perguntas definidas de antemão.

**2. O simulador de basquete saiu.** Ele pressupunha domínio de POO que o diagnóstico
mostrou não existir. Construir um artefato novo sobre base instável produziria um projeto
pela metade e nenhum aprendizado de design.

**3. O sistema de estacionamento virou o artefato da fase.** É o problema onde você
falhou no requisito central, e é onde o aprendizado está. Ele deixa de ser exercício e
passa a ser construído continuamente de 06/09 até 16/09, virando pacote instalável com
testes e README de decisões.

Isso reduz o valor de portfólio do artefato, e a troca é consciente: a Fase 0 existe para
reconstruir base, não para impressionar. A peça de portfólio é a Fase 2.

---

## O que já foi medido

**Consertado em uma sessão:** o modelo de iteração (percorrer palavras, não caracteres) e
o hábito de executar o código durante a escrita. Os dois eram os achados mais graves de
03/09 e não reapareceram em 04/09.

**Parcialmente consertado:** reimplementar à mão o que a biblioteca padrão já faz. O
vocabulário cresceu bastante, mas o reflexo antigo ainda aparece.

**Padrão novo, identificado em 04/09:** enunciado lido de forma incompleta. Requisitos
escritos e não implementados em três dos quatro exercícios. Não é incapacidade, é ausência
de conferência.

**Ainda não medido:** POO. O Bloco B de 03/09 falhou o requisito central e o código não
executava. É o foco do resto da fase.

**Tempo:** 03/09 — 75 min, 0 de 8 rodando. 04/09 — 90 min, 4 rodando. Primeiro ponto da
curva, e é bom.

---

## Hábitos permanentes

Valem em toda sessão até o fim da fase. Não são metas, são condições.

1. **Regra dos três minutos.** Nenhum trecho passa de três minutos sem ser executado.
2. **Conferência de enunciado.** Ao achar que terminou, releia o enunciado linha por linha
   e marque cada requisito. Só então considere pronto.
3. **Vinte minutos antes de perguntar** — para bug. Para conceito, pergunte logo.
4. **Log no mesmo dia**, com tempo por tarefa. Nunca na manhã seguinte.
5. **Commits descrevem intenção**, não arquivo.

---

## Semana 1 — restante

### Dom 06/09 — 3h — POO, parte 1

- 30 min: os três bugs de 04/09 (A1 linha 21, A2 linhas 19-24, A4 linha 32) e conferência
  de enunciado em A1, A4 e A6.
- 45 min: `yield` — 15 min de experimentação no terminal antes de tocar no A7.
- 10 min de pausa.
- 25 min de leitura dirigida, com três perguntas a responder: variável de classe versus de
  instância (tutorial oficial, cap. 9); o que uma `dataclass` gera; o que é `__repr__` e
  por que existe separado de `__str__`. Execute o B1.py antigo no pythontutor.com e observe
  a memória.
- 70 min: Bloco B do zero, com os primeiros 20 minutos em desenho escrito, sem código.

### Seg 07/09 — 1h — Revisão espaçada

Sem conteúdo novo. Refaça de memória, cronometrado, A1 e A6. Compare com os tempos de
04/09. Releia as suas respostas do Bloco C e corrija o que estiver errado — notadamente a
confusão entre descartar alteração não commitada e restaurar arquivo de um commit.

### Ter 08/09 — 2h — Drills

Vinte exercícios curtos, de 3 a 6 minutos, gerados pelo ChatGPT. Alvo único: eliminar a
reimplementação manual. Todos devem ser resolvíveis com a biblioteca padrão em poucas
linhas — `sorted` com `key`, `max`/`min` com `key`, `sum`, `Counter`, `defaultdict`, `zip`,
`enumerate`, desempacotamento, comprehensions com condição.

Regra do dia: se você escrever um laço com contador manual, parou errado.

### Qua 09/09 — 3h — Ambiente e empacotamento

25 min de leitura dirigida: layout `src/`, `pyproject.toml`, básico de `pytest`.

Depois, transformar o estacionamento em pacote: estrutura de diretórios, `pyproject.toml`
com dependências de execução e de desenvolvimento separadas, `pytest` rodando, `ruff`
limpo. Corrigir a regra do `.gitignore` que não casa com o nome real do seu venv.

Mínimo de seis testes, sendo um com `fixture` e um com `parametrize`.

---

## Semana 2 — o artefato

Sistema de cobrança de estacionamento, como pacote Python instalável.

**Requisitos de saída:**

- Tipos de veículo como tipos, não como string. Adicionar ônibus não pode exigir alteração
  no cálculo — e isso será verificado literalmente: você adiciona ônibus no fim e o diff
  precisa mostrar arquivo novo, não arquivo alterado.
- `dataclass` onde couber, `__repr__` útil em toda classe de domínio, type hints em toda
  função pública.
- Tempo injetado, não lido de dentro das classes. Sem isso não há como testar cobrança sem
  esperar horas passarem — mesma razão pela qual o simulador precisaria de aleatoriedade
  injetada.
- Testes cobrindo: primeira hora cheia, fração de hora, hora exata (a borda que quebrou em
  03/09), franquia do mensalista e o excedente.
- CLI mínimo.
- README com três a cinco decisões de design, cada uma com a alternativa descartada.

**Corte, se apertar:** derrube o CLI e o relatório por tipo. Não derrube os testes nem a
injeção de tempo.

### Qui 10/09 — 4h — Bloco nobre

30 min de leitura dirigida: `Protocol` versus `ABC`, composição versus herança. Depois,
fechar o desenho e implementar os tipos de veículo e o cálculo.

### Sex 11/09 — 2h — Testes

Escreva o teste antes da implementação que falta. Comece pela borda da hora exata.

### Dom 13/09 — 3h — Relatório e CLI

Agregação do dia e entrada por linha de comando.

### Seg 14/09 — 1h — Revisão espaçada

Drills de git em repositório descartável: `stash`, `rebase -i` para juntar commits,
`reflog`. Sem projeto.

### Ter 15/09 — 2h — Refatoração e o teste do ônibus

`ruff` limpo, type hints completos, `mypy` rodado e cada reclamação entendida. Então
adicione o tipo ônibus e confira o diff. Se aparecer alteração no cálculo, o desenho
falhou e você tem um dia para consertar.

### Qua 16/09 — 3h — Fechamento

README final, histórico de commits legível, push público, relatório de fim de fase.

---

## Critério de aprovação

Avaliado sem suavização em 16/09:

1. Escrever uma classe com `dataclass`, `__repr__` e type hints sem consultar sintaxe.
2. Explicar, sobre um ponto específico do seu código, por que composição e não herança.
3. O teste do ônibus passa sem alterar o cálculo.
4. `pytest` verde, e pelo menos um teste que falharia se a lógica fosse quebrada de
   propósito.
5. Tempo dos exercícios do Bloco A em queda mensurável entre 03/09 e 16/09.

Três dos cinco de pé é o mínimo. Abaixo disso a fase estende, e isso é informação, não
fracasso.

---

## Fora do escopo

Algoritmos e complexidade (Fase 1). Async, decorators, metaclasses. Docker, CI, deploy.
Pandas e numpy — Python puro de propósito, porque biblioteca esconde falta de fluência em
vez de curá-la.
