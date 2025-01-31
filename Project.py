import pandas as pd
import os

if os.path.exists("users.csv"):
    users = pd.read_csv("users.csv")
else:
    users = pd.DataFrame(columns=['username', 'password'])

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

    
    if not os.path.exists(f"u{username}.csv"):

        data_task = pd.DataFrame(columns=['Name', 'Time', 'Maneger', 'Priority'])
        data_task.to_csv(f"u{username}.csv", index=False)
    else:
        data_task = pd.read_csv(f"u{username}.csv")

def sign_up():
    print("Bem vindo! Antes de utilizar o programa realize o cadastro: ")
    u = input("Digite seu nome de usuário: ").strip()
    p = input("Digite sua senha: ").strip()

    global users

    
    if u in users['username'].values:
        print("Cadastro não pode ser realizado, nome de usuário já foi registrado")
        return Greetings()  

    new_user = pd.DataFrame({'username': [u], 'password': [p]})
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv("users.csv", index=False)
    print("Cadastro realizado com sucesso!")
    return u

def log_in():
    print("Bem vindo de volta! Antes de utilizar o programa realize o log in: ")
    ul = input("Digite o nome de usuário: ").strip()
    pl = input("Digite sua senha: ").strip()

    global users

    user = users[(users['username'] == ul) & (users['password'] == pl)]

    if not user.empty:
        print("Login realizado com sucesso!")
        return ul
    else:
        print("Usuário ou senha incorretos.")
        return None

def task_creation(T_task, TI_task, P_task):
    global username
    global data_task

    new_task = pd.DataFrame({'Name': [T_task], 'Time': [TI_task], 'Maneger': [username], 'Priority': [P_task]})
    data_task = pd.concat([data_task, new_task], ignore_index=True)
    data_task.to_csv(f"u{username}.csv", index=False)
    print("Tarefa Criada com Sucesso!\n")

Greetings()

if username:
    print(f"------------------ \n{username.upper()} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?\n------------------ ")

while True:
    op = int(input("------------------\nDigite 1 para adicionar uma tarefa\nDigite 2 para remover uma tarefa\nDigite 3 para ver as tarefas\nDigite 0 para sair do programa ou alterar o usuário\n------------------\n"))

    if op == 0:
        op2 = int(input("Digite 1 para alterar o usuário do programa\nDigite 2 para sair do programa\nDigite qualquer outro número para permanecer no sistema\n"))
        if op2 == 1:
            Greetings()
            print(f"{username.upper()} BOAS VINDAS AO SEU GERENCIADOR DE TAREFAS! O QUE DESEJA REALIZAR?")
        elif op2 == 2:
            break

    elif op == 1:
        type_task = input("Digite o nome da tarefa: ")
        time_task = input("Digite o prazo da tarefa: ")
        prior_task = input("Digite o nível de prioridade da tarefa: ")
        task_creation(type_task, time_task, prior_task)

    elif op == 2:
        remove = input("Digite o nome do item que deseja remover: ")
        if remove in data_task['Name'].values:
            print("Tarefa encontrada! Removendo...")
            data_task = data_task[data_task['Name'] != remove]  # Remove a tarefa
            data_task.to_csv(f"u{username}.csv", index=False)
        else:
            print("Tarefa não encontrada! Não poderemos remover a tarefa")

    elif op == 3:
        print(data_task)
