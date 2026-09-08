def ordena_tarefas(tarefas):
    # for c, tarefa in enumerate(tarefas): isso foi feito antes de um feedback do chat
    for c, tarefa in enumerate(tarefas, start=1):
        # print(c)
        # print(tarefa)
        print(f"{c} - {tarefa}")

tarefas = ["Estudar Python", "Treinar", "Ler"]
ordena_tarefas(tarefas)

# feito em 3min11s