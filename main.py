from task_manager import TaskManager
from ai_services import create_simple_tasks

def print_menu():
    print("\n--- Gestor de tareas Inteligente")
    print("1. Añadir tarea")
    print("2. Añadir tarea compleja (con IA)")
    print("3. Listar tareas")
    print("4. Completar tareas")
    print("5. Eliminar tarea")
    print("6. Salir")




def main():
    
    manager = TaskManager()
    
    while True:
    
    
        try:
            
            print_menu()
            choice = int(input("Elige una de las opciones: "))
                    
            match choice:
                case 1:
                    description = input("Descripción de la tarea: ")
                    manager.add_task(description)

                case 2:
                    description = input("Descripción de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                           manager.add_task(subtask) 
                        else:
                            print(subtasks)
                            break
                    
                case 3:
                    manager.list_task()
    
                case 5:
                    id = int(input("Id de la tarea a completar: "))
                    manager.complete_task(id)
                    
                case 5:
                    id = int(input("Id de la tarea a eliminar "))
                    manager.delete_task(id)
    
                case 6:
                    print("Saliendo del programa")
                    break
                
                case _:
                    print("Opción no válida. Selecciona otra")
                    
        except ValueError:
            print("Opción no válida. Selecciona otra")


if __name__=="__main__":
    main()