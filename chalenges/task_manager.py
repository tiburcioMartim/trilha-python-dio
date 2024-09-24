# task_manager
'''    Dicas para Expansão
        1 - Salvar Tarefas em um Arquivo: Você pode adicionar funcionalidades para salvar e carregar tarefas de um arquivo (por exemplo, um arquivo de texto).
        2 - Prioridade das Tarefas: Adicione uma opção para definir prioridades para as tarefas.
        3 - Data de Conclusão: Permita que o usuário defina uma data de conclusão para cada tarefa.
'''

def menu_display():
    print('\nTask Manager')
    print('1. add task')
    print('2. list task')
    print('3. remove task')
    print('4. exit')

def add_task(tasks):
    task = input('Type a new task: ')
    tasks.append(task)
    print(f'Task {task} add with sucess!')

def list_task(tasks):
    if not tasks:
        print('\nNo tasks registered\n')
    else:
        print('\ntasks:')
        for i, task in enumerate(tasks, start=1):
            print(f'  {i}. {task}\n')
        # print()

def remove_task(tasks):
    list_task(tasks)
    
    if tasks:
        index = int(input('Type the task number at wish to remove: ')) - 1
        if 0 <= index < len(tasks):
            task_removed = tasks.pop(index)
            print(f'Task {task_removed} removed with sucess!')
        else:
            print('Invalid number.')

def main():
    tasks = []
    while True:
        menu_display()
        option = input('Choise a option: ')
        
        if option == '1':
            add_task(tasks)
        elif option == '2':
            list_task(tasks)
        elif option == '3':
            remove_task(tasks)
        elif option == '4':
            print("Program exit. Thank's for to use.")
            break
        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()