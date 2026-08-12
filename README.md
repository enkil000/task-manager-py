# 📋 Gestor de Tareas Inteligente

Un gestor de tareas moderno potenciado por IA que te ayuda a organizar y desglosar tareas complejas en subtareas simples y accionables. Construido con Python y OpenAI API.

## ✨ Características

- **Gestión básica de tareas**: Crear, listar, marcar como completadas y eliminar tareas
- **Desglose inteligente con IA**: Utiliza GPT para fragmentar tareas complejas en subtareas simples
- **Persistencia de datos**: Almacenamiento en JSON para mantener tus tareas entre sesiones
- **Interfaz de menú interactivo**: Acceso fácil a todas las funcionalidades mediante CLI
- **Sistema de IDs automático**: Gestión automática de identificadores únicos para tareas
- **Suite de tests completa**: 28 tests con 97% de cobertura de código

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Cuenta de OpenAI con acceso a la API
- Variable de entorno `OPENAI_API_KEY` configurada

### Instalación

1. **Clonar o descargar el proyecto**
```bash
cd aplicacion-tareas
```

2. **Crear un entorno virtual**
```bash
python -m venv .venv
```

3. **Activar el entorno virtual**
```bash
# En Windows
.venv\Scripts\activate

# En macOS/Linux
source .venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Configurar las variables de entorno**
Crea un archivo `.env` en la raíz del proyecto:
```env
OPENAI_API_KEY=tu_clave_api_openai_aqui
```

### Uso

**Iniciar la aplicación**
```bash
python main.py
```

Se abrirá un menú interactivo con las siguientes opciones:

```
--- Gestor de tareas Inteligente
1. Añadir tarea
2. Añadir tarea compleja (con IA)
3. Listar tareas
4. Completar tareas
5. Eliminar tarea
6. Salir
```

#### Ejemplos de Uso

**Opción 1: Añadir tarea simple**
```
Elige una de las opciones: 1
Descripción de la tarea: Comprar leche
✓ Tarea añadida: Comprar leche
```

**Opción 2: Añadir tarea compleja con IA**
```
Elige una de las opciones: 2
Descripción de la tarea compleja: Preparar una presentación de ventas
✓ Tarea añadida: Investigar datos de ventas
✓ Tarea añadida: Crear estructura de diapositivas
✓ Tarea añadida: Diseñar gráficos y visualizaciones
✓ Tarea añadida: Redactar contenido
✓ Tarea añadida: Revisar y ajustar
```

**Opción 3: Listar tareas**
```
Elige una de las opciones: 3
[✓] #1: Comprar leche
[ ] #2: Investigar datos de ventas
[ ] #3: Crear estructura de diapositivas
```

**Opción 4: Completar tarea**
```
Elige una de las opciones: 4
Id de la tarea a completar: 2
✓ La tarea con id:2 se ha completado
```

**Opción 5: Eliminar tarea**
```
Elige una de las opciones: 5
Id de la tarea a eliminar: 3
✓ La tarea con id:3 se ha eliminado
```

## 📁 Estructura del Proyecto

```
aplicacion-tareas/
├── main.py                 # Punto de entrada - Interfaz CLI
├── task_manager.py         # Lógica principal de gestión de tareas
├── ai_services.py          # Integración con OpenAI API
├── task.json              # Base de datos JSON (generado automáticamente)
├── test_task_manager.py   # Suite de tests completa
├── requirements.txt       # Dependencias del proyecto
├── .env                   # Variables de entorno (no incluido en repo)
└── README.md              # Este archivo
```

## 🔧 Componentes Principales

### `main.py`
- Punto de entrada de la aplicación
- Implementa la interfaz de menú interactivo
- Gestiona la interacción del usuario

### `task_manager.py`
**Clase `Task`**
- Representa una tarea individual
- Propiedades: `id`, `description`, `completed`
- Método `__str__()` para representación visual con checkmark (✓)

**Clase `TaskManager`**
- Gestiona la colección de tareas
- Métodos:
  - `add_task(description)`: Añade una nueva tarea
  - `list_task()`: Muestra todas las tareas
  - `complete_task(id)`: Marca una tarea como completada
  - `delete_task(id)`: Elimina una tarea
  - `save_tasks()`: Persiste tareas en JSON
  - `load_taks()`: Carga tareas desde JSON

### `ai_services.py`
- Función `create_simple_tasks(task)`: Utiliza GPT para desglosar tareas
- Envía prompts estructurados a OpenAI
- Procesa respuestas y extrae subtareas
- Manejo robusto de errores

## 🧪 Testing

El proyecto incluye una suite completa de 28 tests con cobertura del 97%.

### Ejecutar los tests
```bash
# Ejecutar todos los tests
.venv\Scripts\python -m pytest test_task_manager.py -v

# Con reporte de cobertura
.venv\Scripts\python -m pytest test_task_manager.py --cov=task_manager --cov-report=term-missing
```

### Áreas de prueba
- **TestTask**: Creación y representación de tareas (4 tests)
- **TestTaskManagerAddTask**: Agregación de tareas (3 tests)
- **TestTaskManagerListTask**: Listado de tareas (3 tests)
- **TestTaskManagerCompleteTask**: Completar tareas (4 tests)
- **TestTaskManagerDeleteTask**: Eliminar tareas (4 tests)
- **TestTaskManagerLoadTasks**: Carga desde JSON (4 tests)
- **TestTaskManagerSaveTasks**: Guardado en JSON (4 tests)
- **TestTaskManagerIntegration**: Flujo completo (2 tests)

## 📦 Dependencias

| Paquete | Versión | Propósito |
|---------|---------|----------|
| openai | 3.0.0 | Cliente de API de OpenAI |
| python-dotenv | 1.2.2 | Gestión de variables de entorno |
| requests | 2.34.2 | Peticiones HTTP |
| pydantic | 2.13.4 | Validación de datos |

**Nota**: El proyecto también instala dependencias secundarias requeridas por los paquetes principales.

## ⚙️ Configuración Avanzada

### Variables de Entorno

Create un archivo `.env` en la raíz del proyecto:

```env
# OpenAI API
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

# Opcional - Configuración de modelo
# OPENAI_MODEL=gpt-3.5-turbo
```

### Configuración del Modelo IA

En `ai_services.py`, puedes ajustar los parámetros:

```python
params={
    "model":"gpt-3.5-turbo",  # Cambia el modelo aquí
    "max_completion_tokens":1500,  # Limita la salida
    "reasoning_effort":"minimal"
}
```

## ⚠️ Limitaciones Conocidas

1. **API Key requerida**: Necesitas una cuenta pagada de OpenAI
2. **Bug en delete_task**: Print dentro del loop que se ejecuta siempre (línea 76-77)
3. **Modelo gpt-5 no disponible**: Cambiar a `gpt-3.5-turbo` o `gpt-4`
4. **Sin validación de entrada**: No valida descripciones vacías
5. **IDs no se resetean**: Continúan incrementándose incluso tras eliminar tareas

## 🔄 Flujo de Trabajo

```
┌─────────────────────────────────────────────────┐
│       Inicio de la Aplicación                   │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│  Cargar tareas desde task.json                  │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│   Mostrar menú interactivo                      │
└────────────┬────────────────────────────────────┘
             │
      ┌──────┴──────┬──────────┬──────────┐
      │             │          │          │
      ▼             ▼          ▼          ▼
   Añadir      Añadir con    Listar   Completar
   Tarea        IA           Tareas   Tarea
      │             │          │          │
      └──────┬──────┴──────────┴──────────┘
             │
             ▼
      ┌─────────────────────┐
      │  Guardar en JSON    │
      └─────────────────────┘
             │
             ▼
      ┌─────────────────────┐
      │  ¿Salir? ──NO──────►│
      │      ┌──SÍ──┐       │
      └──────┴──────┴───────┘
             │
             ▼
          FIN
```

## 🚀 Mejoras Futuras

- [ ] Base de datos en lugar de JSON (SQLite/PostgreSQL)
- [ ] Interfaz gráfica (Tkinter/PyQt)
- [ ] Categorías y etiquetas para tareas
- [ ] Fechas límite y recordatorios
- [ ] Prioridades de tareas
- [ ] Sincronización en la nube
- [ ] API REST para acceso remoto
- [ ] Soporte para colaboración en equipo
- [ ] Análisis de productividad
- [ ] Integración con calendarios

## 📝 Notas de Desarrollo

- Utiliza pytest para testing
- Fixtures temporales para aislamiento de tests
- Captura de salida estándar con capsys
- Cobertura de código del 97%

## 🐛 Reportar Bugs

Si encuentras un bug, por favor:
1. Describe el comportamiento esperado
2. Describe el comportamiento actual
3. Incluye pasos para reproducir
4. Menciona la versión de Python y SO

## 📄 Licencia

Este proyecto es parte del programa de educación en desarrollo de software.

## 👨‍💻 Autor

Proyecto desarrollado como práctica en Spec-Driven Development (SDD) y pruebas unitarias.

---

**¿Necesitas ayuda?** Revisa los ejemplos de uso o ejecuta los tests para ver cómo funciona cada componente.
