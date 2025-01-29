print("Bem vindo! Antes de utilizar o programa realize o cadastro: ")
username = input("Digite seu nome de usuário: ")


print(f"{username} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?")

list_task = []

while True :
    
    op = int(input("Digite 1 para adicionar uma tarefa\nDigite 2 para remover uma tarefa\nDigite 3 para ver as tarefas\nDigite 0 para sair do programa\n"))
    
    if op == 0 :
        break

    elif op == 1 :
        type_task = input("Digite o nome/tipo da tarefa: ")
        time_task = input("Digite o horário da tarefa: ")
        prior_task = input("Digite o nível de prioridade da tarefa: ")
        task = {'tipo/nome' : type_task, 'horário' : time_task, 'prioridade': prior_task}
        list_task.append(task)

    elif op == 2 :
        remove = input("Digite o nome do item que deseja remover: ")
        for i in list_task :
            if remove == i['tipo/nome']:
                print("Tarefa encontrada! Removendo...")
                list_task.remove(i)
                break

            else:
                print("Tarefa não encontrada! Não poderemos remover a tarefa")

    elif op == 3 :
        print(list_task)
