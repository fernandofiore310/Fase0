## Diferencas entre modos de alterar/reverter commits

### Descartar alteracao nao commitada
Para descartar uma alteracao nao comitada, se usa o comando git restore file (vi esse comando quando dou git status e tenho algo que ainda nao foi enviado para o repositorio). Nesse caso, eh possivel voltar para a versao pre mudancas nao commitadas, caso voce ache que tenha cometido um erro.
Se usar apenas git restore file, voce restaura o arquivo unstaged. Caso use a flag --staged, voce consegue restaurar a file que estava staged.

### Desfazer commit preservando o historico
Aqui eh quando voce fez um commit, mas quer desconsiderar as mudancas dele daqui para a frente no seu repositorio. Nesse caso, ao inves de apagar o commit, o git olha o que foi feito no commit, e faz um novo commit, com o inverso do que foi feito no anterior, assim, voltando para o estado inicial.
Para fazer isso, usei o comando:
git revert HASH

### Apagar commit do historico
Aqui, acredito que se usa o git reset. Nao sei muito bem como ele faz algo, mas imagino que ele apenas apague o commit e volte a "linha do tempo" para o commit anterior. Imagino que esse comando pode gerar problemas quando esta se trabalhando em grupo, e especialmente, quando se usa mais de uma branch. Pois caso uma branch tenha sido originada a partir do commit que pode ter sido apagado em outra branch, imagino que possa dar um problemao danado.

### Restaurar arquivo a partir de um commit específico
Nesse caso, voce apenas da um "salto" na timeline dos commits e captura uma versao de um arquivo de um commit antigo e restaura ele na "timeline" atual.
Basicamente voce da um load numa versao de um commit antigo no arquivo atual.
Para fazer isso, usa-se:

```git checkout hash do commit -- caminho```