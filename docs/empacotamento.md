# Anotações

## Documento dedicado ao registro de conteúdos de blocos de leituras dirigidas

### Empacotamento de projetos e pyproject.toml
Empacotar um projeto significa transformar todos os meus arquivos e códigos de um projeto em algo que pode ser distribuido e reutilizável, capaz de ser instalado, importado e executado em qualquer ambiente, não só apenas na sua máquina local.

Quando falamos sobre pacote, nos referimos especificamente à pasta que contém todo o código-fonte do seu projeto (e arquivos de suporte necessários) organizada e configurada para ser distribuída.
Dentro do seu repositório, existem arquivos de desenvolvimento que não entram no pacote final (como pasta de testes, arquivos de configuração do editor, scripts de automação ou o próprio arquivo de configuração .git). O pacote é apenas o subconjunto de código e arquivos que você empacota e disponibiliza para ser instalado em outros ambientes.

Antes para empacotar um projeto, era necessário criar um arquivo executável chamado setup.py. Hoje, tudo é feito a partir de um arquivo chamado pyproject.toml, que basicamente centraliza todas as configurações do projeto que está sendo desenvolvido.
Ele se divide em duas seções cruciais:
[build-system]: Diz às ferramentas como transformar seu código fonte em um pacote instalável.  
[project]: Contém os metadados do pacote (nome, versão, dependências diretas, versão do Python suportada, etc.).  

Para transformar o diretório de código em um pacote pronto para ser intalado, distribuóido e compartilhado, são usadas duas ferramentas:
Build-Backend: É a ferramenta que realmente executa o trabalho pesado. Ele organiza os arquivos na estrutura correta, realiza compilação/empacotamento e gera os arquivos finais de distribuição (sdist ou wheel) na pasta dist/ (são esses arquivos que se sobe para o PyPI ou compartilha com outros devs).
Build-Frontend: A CLI/Ferramenta que você executa (pip, build (python -m build), uv). Lê o pyproject.toml, cria um ambiente isolado temporário, instala o backend e chama as funções desse backend.

Existem dois formatos de distribuição, como mencionado anteriormente, que o backend gera na pasta dist/
Sdist (Significa Source Distribution): É apenas o código-fonte puro compactado em um .tar.gz. Quando você baixa apenas o SDist, o pip precisa compilar e gerar o Wheel localmente na sua máquina antes de conseguir instalar.
Se o autor da biblioteca não publicou um Wheel compatível com seu sistema operacional ou sua versão do Python, o pip recorre ao SDist como plano B.
Wheel (.whl): É o pacote pré-compilado, como se fosse o executável de instalação (tipo um .msi no Windows ou .dmg no Mac). O pip apenas baixa o arquivo, descompacta os arquivos na pasta do seu ambiente virtual (site-packages) e pronto. Instalação extremamente rápida e sem dependências de ferramentas externas (como compiladores C/C++ ou Rust).


### Layouts de código e como empacotar um projeto
Onde o seu pacote vive em relação à raiz do projeto.
Flat-Layout: A pasta do pacote fica na raiz do projeto. (project/pacote)
Source-Layout: A pasta do pacote fica dentro de uma subpasta dedicada. (project/src/pacote)

O source-layout existe para evitar que o próprio Python esconda erros humanos que possam ser escritos durante o desenvolvimento dos arquivos do projeto.
O exemplo mais comum é com o uso do pytest. Nesse caso, a estrutura flat-layout esconderia um erro de programação durante os testes.
Exemplo: estou escrevendo um pacote Python que lê dados em uma tabela no formato dados.json.
Imagine que esqueco de avisar o build-backend no meu pyproject.toml que o arquivo dados.json deve ser incluido na compilação do pacote. Logo, ele iria apenas empacotar os arquivos .py, ignorando o .json (fundamental para o código funcionar).
Se eu estiver usando flat-layout:

meu_projeto/

├── pyproject.toml

└── meu_pacote/

    ├── __init__.py

    ├── dados.json  

    └── main.py  

Você abre o terminal na pasta do projeto e roda o pytest.
O Python começa a executar o teste e encontra import meu_pacote.
Como você está rodando o comando da raiz, o Python lê a pasta meu_pacote/ direto do seu disco rígido por padrão.
O código roda, lê o dados.json que está ali no disco rígido e o teste retorna: APROVADO
O diagnóstico falso: Seu teste passou, então você assume que o pacote está perfeito.
No entanto, o problema surge quando alguém tenta usar o seu projeto em outra máquina.
Você gera o arquivo .whl (o pacote final) e faz o upload.
Quando um usuário instala seu pacote com pip install meu_pacote e tenta rodar o código:
O pip instalou o arquivo .whl na pasta de bibliotecas do ambiente do usuário.
O arquivo dados.json não está lá (porque você esqueceu de incluir no pyproject.toml no Passo 1).
O programa do usuário quebra com erro FileNotFoundError.

O source-layout evita isso pois na hora que o Python fosse ler o import meu_pacote, ele nao acharia esse modulo na raiz. Isso te obrigaria a rodar pip install -e . no seu ambiente virtual para conseguir testar. A instalação do pip iria gerar o pacote e deixar de fora o dados.json, visto que você não o adicionou no pyproject.toml. O seu pytest falharia no seu próprio computador, apontando o FileNotFoundError antes de você subir qualquer código para produção.


### Dependências de execução vs. desenvolvimento
Dependências de Execução (dependencies)

São os pacotes de que o seu código necessita para rodar na máquina do usuário final ou no servidor de produção. Sem eles, o código quebra com ImportError durante o uso normal da aplicação.

Exemplos: pandas, requests, fastapi, numpy.

Onde vivem no pyproject.toml:

Ini, TOML
[project]
name = "meu-pacote"
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]
Impacto: Quando alguém executa pip install meu-pacote, o pip lê essa lista e baixa todas essas dependências automaticamente.

Dependências de Desenvolvimento (dev-dependencies)

São as ferramentas necessárias apenas para quem está construindo, testando, formatando ou fazendo o build do projeto. O usuário final não precisa delas para executar a biblioteca.

Exemplos:

Testes: pytest, coverage

Formatação/Linting: ruff, black, mypy

Documentação: mkdocs, sphinx

Build/Publicação: build, twine

Onde vivem no pyproject.toml: A especificação moderna (PEP 735 / padrões de gerenciadores como uv ou hatch) usa grupos de dependências opcionais ou de desenvolvimento:

Ini, TOML
[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.3.0",
    "mypy>=1.8.0",
]
Impacto: Quando um usuário comum roda pip install meu-pacote, nenhuma das dependências de desenvolvimento é baixada. Elas só são instaladas se o desenvolvedor solicitar explicitamente (ex: pip install -e .[dev] ou via gerenciador de ambiente).