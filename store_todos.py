class Todo_list:
    def __init__(self):
        self.todos = []

    def create_todo(self, todo):
        self.todos.append(todo)
        return self.todos
    
    # def del_todo(self, todo_del):
    #     self.todos.remove(todo_del)
    #     return self.todos
    
    # delete by using index
    def del_todo(self, todo_del):
        if todo_del in self.todos:
            index_tobe = self.todos.index(todo_del)
            self.todos.pop(index_tobe)
        return self.todos        
    
    def __repr__(self):
        return str(self.todos)

if __name__=='__main__':
    my_list = Todo_list()
    To_do_one = my_list.create_todo('Praise God')
    To_do_two = my_list.create_todo('Worship Him')
    To_do_three = my_list.create_todo('Enjoy His Presence')
    To_do_four = my_list.create_todo('Do somethings')
    delete_one = my_list.del_todo('Do somethings')
    print(delete_one)

