def sign_up():
    print("Bem vindo! Antes de utilizar o programa realize o cadastro: ")
    u = input("Digite seu nome de usuário: ")
    return u

username = sign_up()

print(f"{username.upper()} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?")

list_task = []

while True :
    
    op = int(input("Digite 1 para adicionar uma tarefa\nDigite 2 para remover uma tarefa\nDigite 3 para ver as tarefas\nDigite 0 para sair do programa ou alterar o usuário\n"))
    
    if op == 0 :
        op2 = int(input("Digite 1 para alterar o usuário do programa\nDigite 2 para sair do programa\nDigite qualquer outro número para permanecer no sistema\n"))
        if op2 == 1:
            username = sign_up()
            print(f"{username.upper()} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?")

        elif op2 == 2:
            break


    elif op == 1 :
        type_task = input("Digite o nome da tarefa: ")
        time_task = input("Digite o prazo da tarefa: ")
        prior_task = input("Digite o nível de prioridade da tarefa: ")
        task = {'nome' : type_task, 'gerencia' : username, 'horário' : time_task, 'prioridade': prior_task}
        list_task.append(task)

    elif op == 2 :
        remove = input("Digite o nome do item que deseja remover: ")

        for i in list_task :
            if remove == i['nome']:
                print("Tarefa encontrada! Removendo...")
                if username != i['gerencia']:
                    print("Você não é o gerente do projeto, não poderá remover essa tarefa")

                else:
                    list_task.remove(i)
                break

            else:
                print("Tarefa não encontrada! Não poderemos remover a tarefa")

    elif op == 3 :
        print(list_task)
