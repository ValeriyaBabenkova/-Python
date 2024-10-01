class TaskModel:
    def __init__(self):
        self.tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

    def get_tasks(self):
        return self.tasks

    def add_task(self, name):
        task = {'name': name, 'status': 'в ожидании'}
        self.tasks.append(task)

    def complete_task(self, number_task):
        self.tasks[number_task]['status'] = 'выполнено'

    def delete_task(self, number_task):
        self.tasks.pop(number_task)


class View:
    @staticmethod
    def show_all_tasks(tasks):
        for number, task in enumerate(tasks, 1):
            print(f"{number}. {task['name']} : {task['status']}")

    @staticmethod
    def show_add_task():
        return input('Введите название задачи\n')

    @staticmethod
    def show_complete_task():
        return int(input('Введите номер задачи\n'))

    @staticmethod
    def show_delete_task():
        return int(input('Введите номер задачи. которую хотите удалить\n'))


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def add_task(self):
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)
        task_name = self.view.show_add_task()
        self.model.add_task(task_name)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)

    def complete_task(self):
        task_number = self.view.show_complete_task()
        task_number -= 1
        self.model.complete_task(task_number)

    def delete_task(self):
        task_number = self.view.show_delete_task()
        task_number -= 1
        self.model.delete_task(task_number)


model = TaskModel()
view = View()
contr = Controller(view, model)

while True:
    print('1 - Добавить задачу')
    print('2 - Выполнить задачу')
    print('3 - Посмотреть список задач')
    print('4 - Удалить задачу')
    print('5 - Выйти')

    choice = input('Что вы хотите сделать?\n')

    if choice == '1':
        contr.add_task()
    elif choice == '2':
        contr.complete_task()
    elif choice == '3':
        print('Посмотрите на ваши задачи')
        contr.show_tasks()
    elif choice == '4':
        contr.delete_task()
    elif choice == '5':
        pass