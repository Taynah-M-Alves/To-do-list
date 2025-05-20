import datetime as datetime 

# Variaveis:

tarefas= []
data_criacao = datetime.date
tipos_status = ["em aberto", "em progresso", "finalizado","emaberto","emprogresso"]

class tarefa:

    def __init__(self, titulo, status="Em Aberto"):
        self.titulo = titulo
        self.status = status
        self.data_criacao = datetime.date.today()



    def mostrar_tarefa(self):
        global data_criacao
        print(f'''\n----------------{self.titulo}----------------
            
            Status: {self.status}
            Criação da tarefa:{data_criacao}''')
        
def criar_task():
        titulo= input(str("Digite o titulo da tarefa que deseja criar:")).capitalize()
        while True:
            print('''Status das tarefas:
                1. Em Aberto
                2. Em Progresso
                3. Finalizado''')
            status = input(str("\nDigite em qual status está sua tarefa:")).lower()
            if status in tipos_status:
                 break
            else:
                 print("Status inválido! tente novamente.")
        task = tarefa(titulo, status)
        tarefas.append(task)

print('''
    Ações disponíveis:
      1. Criar uma task.
      2. Visualizar as tasks
      3. Sair
''')
#Seria legal incluir a chance do usuário excluir alguma task  



while True:
    opcao= input(str("Digite a opção que deseja fazer:"))

    if opcao=="1":
        criar_task()
        print("task criada com sucesso!")

    if opcao == "2":
        for t in tarefas:
            t.mostrar_tarefa()
        
    if opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção invalida! Tente novamente.")