import pandas as pd
import os

if os.path.exists("users.csv"):
    users = pd.read_csv("users.csv")
    users_list = users[['username', 'password']].to_dict('records')
else:
    users = pd.DataFrame(columns=['username', 'password'])
    users_list = []


project_list = []
username = ""
list_task = []

def Greetings():
    global username
    global data_task

    g = input("Olá, deseja fazer o cadastro de usuário ou realizar log in?\n").strip().lower()

    if g in ["log in", "login"]:
        username = log_in()
        if not username:
            Greetings()

    elif g in ["cadastro", "registro"]:
        username = sign_up()

    else:
        print("Opção não válida, digite novamente!")
        Greetings()

    if not os.path.exists(f"u{username}.csv"):
        data_task = pd.DataFrame(columns=['Name', 'Time', 'Maneger', 'Priority', 'Type'])
        data_task.to_csv(f"u{username}.csv", index=False)
    else:
        data_task = pd.read_csv(f"u{username}.csv")

def sign_up():
    print("Bem vindo! Antes de utilizar o programa realize o cadastro: ")
    u = input("Digite seu nome de usuário: ").strip()
    p = input("Digite sua senha: ").strip()

    global users, users_list

    if u in users['username'].values:
        print("Cadastro não pode ser realizado, nome de usuário já foi registrado")
        return Greetings()  

    new_user = pd.DataFrame({'username': [u], 'password': [p]})
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv("users.csv", index=False)
    users_list.append({'username': u, 'password': p})
    print("Cadastro realizado com sucesso!")
    return u

def log_in():
    print("Bem vindo de volta! Antes de utilizar o programa realize o log in: ")
    ul = input("Digite o nome de usuário: ").strip()
    pl = input("Digite sua senha: ").strip()

    global users_list

    # Verifica se o usuário e a senha estão corretos
    for user in users_list:
        if user["username"].strip().lower() == ul.lower() and user["password"].strip() == pl:
            print("Login realizado com sucesso!")
            return ul  # Retorna o nome de usuário se o login for bem-sucedido

    # Se não encontrar o usuário ou a senha estiver incorreta
    print("Usuário ou senha incorretos.")
    return None

def task_creation(T_task, TI_task, P_task):
    global username
    global data_task
    global users_list

    new_task = pd.DataFrame({'Name': [T_task], 'Time': [TI_task], 'Maneger': [username], 'Priority': [P_task], 'Type': "Task"})
    data_task = pd.concat([data_task, new_task], ignore_index=True)
    data_task.to_csv(f"u{username}.csv", index=False)
    print("Tarefa Criada com Sucesso!\n")

def add_to_pj(C, N_pj, T_pj, P_pj):
    global users_list, data_task, username, project_list
    pjd = dict()
    cont = []
    pjd['project_name'] = N_pj
    pjd['Manager'] = username
    u = ""
    nun = 1
    for i in range(C):
        while True:
            u = input("Digite o nome do usuário a ser adicionado: ")
            pts = 0
            for j in users_list:
                if u.lower() == j["username"].strip().lower():
                    cont.append(u)
                    nun = nun + 1
                    pts = 1
                    break

            if pts == 1:
                break

            else:
                print("Usuário não encontrado, tente novamente")

        addu_new_pj = pd.DataFrame({'Name': [N_pj], 'Time': [T_pj], 'Maneger': [username], 'Priority': [P_pj], 'Type': "Project"})
        temp_data_task = pd.read_csv(f"u{u}.csv")
        temp_data_task = pd.concat([temp_data_task, addu_new_pj], ignore_index= True)
        temp_data_task.to_csv(f"u{u}.csv", index= False)
    pjd['Helpers'] = cont
    project_list.append(pjd)


def project_creation(N_pj, T_pj, P_pj):
    global username
    global data_task

    new_pj = pd.DataFrame({'Name': [N_pj], 'Time': [T_pj], 'Maneger': [username], 'Priority': [P_pj], 'Type': "Project"})
    data_task = pd.concat([data_task, new_pj], ignore_index= True)
    data_task.to_csv(f"u{username}.csv", index= False)

    colaborators = int(input("Digite quantos colaboradores deseja adicionar so projeto: "))

    add_to_pj(colaborators, N_pj, T_pj, P_pj)

    print("Projeto adicionado com sucesso!")

def remove_PJ_OU(user, remove):
    temp_data_task = pd.read_csv(f"u{user}.csv")
    temp_data_task = data_task[data_task['Name'] != remove]
    temp_data_task.to_csv(f"u{user}.csv")

Greetings()

if username:
    print(f"------------------ \n{username.upper()} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?\n------------------ ")

while True:
    op = int(input("------------------\nDigite 1 para adicionar uma tarefa\nDigite 2 para adicionar um projeto (tarefa com colaboradores)\nDigite 3 para Remover uma tarefa\nDigite 4 para ver as tarefas\nDigite 0 para sair do programa ou alterar o usuário\n------------------\n"))

    if op == 0:
        op2 = int(input("Digite 1 para alterar o usuário do programa\nDigite 2 para sair do programa\nDigite qualquer outro número para permanecer no sistema\n"))
        if op2 == 1:
            Greetings()
            print(f"{username.upper()} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?")
        elif op2 == 2:
            break

    elif op == 1:
        name_task = input("Digite o nome da tarefa: ")
        time_task = input("Digite o prazo da tarefa: ")
        prior_task = input("Digite o nível de prioridade da tarefa: ")
        task_creation(name_task, time_task, prior_task)

    elif op == 2:
        name_project = input("Digite o nome do projeto: ")
        time_project = input("Digite o prazo do projeto: ")
        prior_project = input("Digite o nível de prioridade do projeto: ")
        project_creation(name_project, time_project, prior_project)
        

    elif op == 3:

        while True:
            opr = input("Deseja remover uma tarefa ou um projeto? ")

            if opr.lower() == "tarefa":
                remove = input("Digite o nome da tarefa que deseja remover: ")
                if remove in data_task['Name'].values and "Task" in data_task['Type'].values:
                    print("Tarefa encontrada! Removendo...")
                    data_task = data_task[data_task['Name'] != remove]  # Remove a tarefa
                    data_task.to_csv(f"u{username}.csv", index=False)
                    break

                else:
                    print("Tarefa não encontrada! Não poderemos remover a tarefa")
                    break

            elif opr.lower() == "projeto":
                remove = input("Digite o nome do projeto que deseja remover: ")
                for i in project_list:
                    if i['project_name'].strip() == remove.strip() and i['Manager'] == username:
                        print("Projeto encontrado! Removendo...")
                        data_task = data_task[data_task['Name'] != remove]
                        data_task.to_csv(f"u{username}.csv", index=False)
                        print(i['Helpers'][0])
                        for j in i['Helpers']:
                            dumblist = []
                            for k in users_list:
                                dumblist.append(k['username'])
                            if j in dumblist:
                                remove_PJ_OU(j, remove)
                        print("Projeto removido com sucesso!")

                    else:
                        print("Projeto não encontrado! Não poderemos remover o projeto")
                
                break
          
    elif op == 4:
        print(data_task)