## Diferencas entre modos de alterar/reverter commits

### Descartar alteracao nao commitada
Isso acontece quando voce ainda nao realizou o commit de um arquivo, por exemplo, (nao sei se ele deve estar como staged change, acredito que sim) e voce quer que ele volte para a versao original dele.
Fiz isso com o exercicio A7.py, onde usei o comando:
git checkout 005f1dbfccbc0f1008badb4ae1094091c9556a8f -- C:\Users\ferna\dev\reativacao\Fase0\diagnostico\BlocoA\A7.py
Quando fiz isso, eh como se ele tivesse voltado para a fase onde o meu arquivo estava, antes das minhas alteracoes.

### Desfazer commit preservando o historico
Aqui eh quando voce fez um commit, mas quer desconsiderar as mudancas dele daqui para a frente no seu repositorio. Nesse caso, ao inves de apagar o commit, o git olha o que foi feito no commit, e faz um novo commit, com o inverso do que foi feito no anterior, assim, voltando para o estado inicial.
Para fazer isso, usei o comando:
git revert HASH

### Apagar commit do historico
Aqui, acredito que se usa o git reset. Nao sei muito bem como ele faz algo, mas imagino que ele apenas apague o commit e volte a "linha do tempo" para o commit anterior. Imagino que esse comando pode gerar problemas quando esta se trabalhando em grupo, e especialmente, quando se usa mais de uma branch. Pois caso uma branch tenha sido originada a partir do commit que pode ter sido apagado em outra branch, imagino que possa dar um problemao danado.