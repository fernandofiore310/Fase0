# FASE 0 — REATIVAÇÃO

## O Sistema Desenvolvido - Simulador de Estacionamento

O sistema desenvolvido nesse projeto simula um estacionamento. Algumas das funções que ele realiza:

- Armazenamento de veículos estacionado,
- Diferentes tipos de veículos,
- Um sistema de cálculo de tarifa, diferente para cada tipo de cliente e seu tipo de veículo,
- Um relatório diário que resumo a atividade do estacionamento naquele dia

---

## Como usar o Sistema

### Pré-requisitos

- Python 3.10+
- Git

### Passos

**1. Clonar o Repositório:**

```bash
   git clone "https://github.com/fernandofiore310/Fase0.git"
   cd Fase0
```

**2. Criar e ativar o Ambiente Virtual**

No Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instalar dependências**

Este projeto gerencia dependências via `pyproject.toml`.

```bash
pip install .--group <dependency-groups>
```

**4. Executar projeto**

Na raiz do projeto, execute:

```bash
python src/projeto_estacionamento/main.py
```

**5. Testar o projeto**

Na raiz do projeto, execute:

```bash
pytest -v
```

---

## Decisões de Design

Nesta seção, trago alguns pontos e decisões que foram feitos ao longo do desenvolvimento desse projeto

### A Classe Mensalista herda da classe Veiculo, e não da classe Carro.

A classe Mensalista, na teoria, pode dirigir qualquer tipo de veículo, a questão é que ele só vai ser cobrado como um carro. Logo, a classe Mensalista foi criada herdando de veículo.
O atributo de franquia é criado nessa classe (já que é único desse tipo de Classe) e no método de calcular a tarifa, usar o cálculo de calcular a tarifa do Carro quando a franquia tiver acabado.
Para não repetir o cálculo em dois lugares, criei uma função "solta" chamada calcula_tarifa_carro(), que é usada tanto no método do Mensalista, quanto no do Carro.

### Tempo injetado manualmente

Para conseguir fazer os testes e ver se as tarifas estavam sendo corretamente calculadas, sem ter que esperar o tempo real de fato, preferi injetar o tempo manualmente nas funções de cálculo de tarifas do que usar o datetime por exemplo.
Assim evita que tenha que se esperar o tempo real.
Caso esse projeto fosse ser, futuramente, usado em uma aplicação real, acredito que vale a mudança.

### Conflito do tempo de permanência média e relatório diário

Ao testar a Classe Menaslista, é normal que se passe tempos altíssimos como parâmetro do seu método de calcular tarifa, de modo a testar se o Sistema passa a cobrá-lo após as 200 horas mensais. Isso acaba gerando um conflito, pois imagine que coloquei que o Mensalista ficou 210 horas no estacionamento, de modo a ver se o Sistema cobra corretamente essas 10 horas adicionais do plano do mensalista. Se caso, depois disso, eu pedir para o Sistema gerar o relatório diário, essas 210 horas que passei anteriormente, vão entrar no cálculo de permanência média do dia. Porém, como é algo óbvio de se notar, é impossível um dia ter 210 horas.
Logo, é apenas uma inconsistência que surgiu, que é meio inevitável.
