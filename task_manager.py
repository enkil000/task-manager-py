class Task:
    
    def __init__(self, id, descripcion, completed=False):
        self.id=id
        self.descripcion= descripcion
        self.completed= completed
        
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.descripcion}"   
    
    
class TaskManager:
    def __init__(self):
        self._tasks=[]
        self._next_id=1
        
    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id +=1
        print(f"Tarea añadida: {description}")
    
    def list_task(self):
        if not self._tasks:
            print("No existen tareas")
        else:
            for task in self._tasks:
                print(task)
    
    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed=True
                print (f"La tarea con id:{id} se ha completado")
                return
        print(f"Tarea no encontrada {id}")


    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(id)
                print (f"La tarea con id:{id} se ha eliminado")
                return

        print(f"Tarea no encontrada {id}")
