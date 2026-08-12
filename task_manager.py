
import json

class Task:
    
    def __init__(self, id, description, completed=False):
        self.id=id
        self.description= description
        self.completed= completed
        
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"   
    
    
class TaskManager:
    
    FILENAME="task.json"
    
    def __init__(self):
        self._tasks=[]
        self._next_id=1
        self.load_taks()
        
    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id +=1
        self.save_tasks()
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
                self.save_tasks()
                return
        print(f"Tarea no encontrada {id}")


    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print (f"La tarea con id:{id} se ha eliminado")
                self.save_tasks()
                return
            print(f"Tarea no encontrada {id}")
            
    def load_taks(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks=[Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id= self._tasks[-1].id +1
                else:
                    self._next_id=1
        
        except FileNotFoundError:
            print("No se ha encontrado el fichero")
            
    
    def save_tasks(self):
        try:
            with open(self.FILENAME, "w") as file:
                json.dump([{"id":task.id, "description":task.description, "completed":task.completed} for task in self._tasks], file, indent=4)
        except FileNotFoundError:
                    print("No se ha encontrado el fichero")
            

