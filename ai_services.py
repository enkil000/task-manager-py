import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY")
)



def create_simple_tasks(task):
    if not client.api_key:
        return ["Error: La Api key de OpenAI no está configurada"]
    
    
    try:
        prompt=f"""Desglosa la siguiente tarea en una lista de subtareas simples y accionables.
        Tarea: {task}
        
        Formato de la respuesta:
        -Subtarea 1
        -Subtarea 2
        -Subtarea 3
        -etc..
        
        Responde solo con una lista de subtareas, una por linea, empezado cada linea con un -
        
        """
        
        params={
            "model":"gpt-5",
            "messages":[
                {"role":"system","content":"Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables"},
                {"role":"user","content":prompt}
            ],
            "max_completion_tokens":1500,
            "verbosity":"medium",
            "reasoning_effort":"minimal"
        }
        
        response= client.chat.completions.create(**params) # esos asteriscos son para desempaquetar la petición
        content= response.choices[0].message.content.strip()
        
        subtasks=[]
        
        for line in content.split("\n"):
            line=line.strip()
            if line and line.startswith("-"):
                subtask=line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: no se ha podido generar las subtareas"]
        
        
    except Exception as e:
       print(f"Error real de la API: {e}")
       return ["Error: no se ha podido establecer comunicación con OpenAI."] 
        