## Grafo de Branches

### Comando usado
git log --graph --oneline --all --decorate

--graph: Desenha a árvore usando caracteres de texto (ASCII art).

--oneline: Compacta o hash e a mensagem de commit em uma única linha.

--all: Exibe todas as branches (por padrão, exibe apenas a branch atual).

--decorate: Mostra onde os ponteiros das branches (main, HEAD, remotos) estão apontando no grafo.

### Analise do Esquema ate o momento
Entendi que cada * no grafo representa um commit. No entanto nao estou conseguindo entender muito bem as linhas que foram desenhadas. Existem, pelo que vejo, 5 linhas diferentes, uma amarela, uma azulm, uma vermelha, uma roxa e uma verde. Nao entendi o que cada uma delas significa. Alem disso, tambem nao entendi por que umas mudam de direcao e outras, como a vermelha, seguem retas.