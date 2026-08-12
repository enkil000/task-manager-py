import json
import pytest
from task_manager import Task, TaskManager


@pytest.fixture
def temp_task_file(tmp_path):
    """Fixture que proporciona un archivo temporal para tareas."""
    task_file = tmp_path / "task.json"
    TaskManager.FILENAME = str(task_file)
    yield task_file
    # Limpieza automática por tmp_path


@pytest.fixture
def manager(temp_task_file):
    """Fixture que proporciona un TaskManager con archivo temporal."""
    return TaskManager()


class TestTask:
    """Tests para la clase Task."""

    def test_task_creation(self):
        task = Task(1, "Test task")
        assert task.id == 1
        assert task.description == "Test task"
        assert task.completed is False

    def test_task_creation_with_completed_true(self):
        task = Task(2, "Completed task", completed=True)
        assert task.id == 2
        assert task.description == "Completed task"
        assert task.completed is True

    def test_task_str_representation_incomplete(self):
        task = Task(1, "Buy groceries")
        assert str(task) == "[ ] #1: Buy groceries"

    def test_task_str_representation_complete(self):
        task = Task(3, "Review code", completed=True)
        assert str(task) == "[✓] #3: Review code"


class TestTaskManagerAddTask:
    """Tests para la funcionalidad de agregar tareas."""

    def test_add_task_single(self, manager, capsys):
        manager.add_task("Learn Python")
        assert len(manager._tasks) == 1
        assert manager._tasks[0].id == 1
        assert manager._tasks[0].description == "Learn Python"
        assert manager._tasks[0].completed is False
        assert manager._next_id == 2
        captured = capsys.readouterr()
        assert "Tarea añadida: Learn Python" in captured.out

    def test_add_task_multiple_increments_id(self, manager):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        assert len(manager._tasks) == 3
        assert manager._tasks[0].id == 1
        assert manager._tasks[1].id == 2
        assert manager._tasks[2].id == 3
        assert manager._next_id == 4

    def test_add_task_persists_to_file(self, manager, temp_task_file):
        manager.add_task("Save to file")
        with open(temp_task_file, "r") as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]["id"] == 1
        assert data[0]["description"] == "Save to file"
        assert data[0]["completed"] is False


class TestTaskManagerListTask:
    """Tests para la funcionalidad de listar tareas."""

    def test_list_task_empty(self, manager, capsys):
        manager.list_task()
        captured = capsys.readouterr()
        assert "No existen tareas" in captured.out

    def test_list_task_shows_all_tasks(self, manager, capsys):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.list_task()
        captured = capsys.readouterr()
        assert "[ ] #1: Task 1" in captured.out
        assert "[ ] #2: Task 2" in captured.out
        assert "[ ] #3: Task 3" in captured.out

    def test_list_task_shows_completed_status(self, manager, capsys):
        manager.add_task("Incomplete")
        manager.add_task("Complete this")
        manager.complete_task(2)
        manager.list_task()
        captured = capsys.readouterr()
        assert "[ ] #1: Incomplete" in captured.out
        assert "[✓] #2: Complete this" in captured.out


class TestTaskManagerCompleteTask:
    """Tests para la funcionalidad de completar tareas."""

    def test_complete_task_success(self, manager, capsys):
        manager.add_task("Task to complete")
        manager.complete_task(1)
        assert manager._tasks[0].completed is True
        captured = capsys.readouterr()
        assert "La tarea con id:1 se ha completado" in captured.out

    def test_complete_task_not_found(self, manager, capsys):
        manager.add_task("Existing task")
        manager.complete_task(999)
        captured = capsys.readouterr()
        assert "Tarea no encontrada 999" in captured.out

    def test_complete_task_persists_to_file(self, manager, temp_task_file):
        manager.add_task("Persist completion")
        manager.complete_task(1)
        with open(temp_task_file, "r") as f:
            data = json.load(f)
        assert data[0]["completed"] is True

    def test_complete_task_multiple(self, manager):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.complete_task(1)
        manager.complete_task(3)
        assert manager._tasks[0].completed is True
        assert manager._tasks[1].completed is False
        assert manager._tasks[2].completed is True


class TestTaskManagerDeleteTask:
    """Tests para la funcionalidad de eliminar tareas."""

    def test_delete_task_success(self, manager, capsys):
        manager.add_task("Task to delete")
        manager.delete_task(1)
        assert len(manager._tasks) == 0
        captured = capsys.readouterr()
        assert "La tarea con id:1 se ha eliminado" in captured.out

    def test_delete_task_not_found(self, manager, capsys):
        manager.add_task("Existing task")
        manager.delete_task(999)
        assert len(manager._tasks) == 1
        captured = capsys.readouterr()
        assert "Tarea no encontrada 999" in captured.out

    def test_delete_task_persists_to_file(self, manager, temp_task_file):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.delete_task(1)
        with open(temp_task_file, "r") as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]["id"] == 2

    def test_delete_task_multiple(self, manager):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.delete_task(2)
        assert len(manager._tasks) == 2
        assert manager._tasks[0].id == 1
        assert manager._tasks[1].id == 3


class TestTaskManagerLoadTasks:
    """Tests para la funcionalidad de cargar tareas."""

    def test_load_tasks_from_existing_file(self, temp_task_file, capsys):
        # Crear archivo con tareas preexistentes
        data = [
            {"id": 1, "description": "Write tests", "completed": False},
            {"id": 2, "description": "Review code", "completed": True},
            {"id": 3, "description": "Deploy", "completed": False},
        ]
        temp_task_file.write_text(json.dumps(data))

        manager = TaskManager()

        assert len(manager._tasks) == 3
        assert manager._tasks[0].id == 1
        assert manager._tasks[0].description == "Write tests"
        assert manager._tasks[0].completed is False
        assert manager._tasks[1].id == 2
        assert manager._tasks[1].completed is True
        assert manager._next_id == 4

    def test_load_tasks_empty_file(self, temp_task_file, capsys):
        temp_task_file.write_text(json.dumps([]))

        manager = TaskManager()

        assert manager._tasks == []
        assert manager._next_id == 1

    def test_load_tasks_missing_file(self, temp_task_file, capsys):
        # No crear el archivo, solo configurar la ruta
        manager = TaskManager()

        assert manager._tasks == []
        assert manager._next_id == 1
        captured = capsys.readouterr()
        assert "No se ha encontrado el fichero" in captured.out

    def test_load_tasks_sets_next_id_correctly(self, temp_task_file):
        data = [
            {"id": 5, "description": "Task", "completed": False},
            {"id": 10, "description": "Task", "completed": False},
        ]
        temp_task_file.write_text(json.dumps(data))

        manager = TaskManager()

        assert manager._next_id == 11  # Última ID + 1


class TestTaskManagerSaveTasks:
    """Tests para la funcionalidad de guardar tareas."""

    def test_save_tasks_creates_file(self, manager, temp_task_file):
        manager.add_task("Save test")
        assert temp_task_file.exists()

    def test_save_tasks_format_is_valid_json(self, manager, temp_task_file):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        
        with open(temp_task_file, "r") as f:
            data = json.load(f)  # Debe no lanzar excepción
        assert isinstance(data, list)

    def test_save_tasks_preserves_all_fields(self, manager, temp_task_file):
        manager.add_task("Test task")
        manager.complete_task(1)

        with open(temp_task_file, "r") as f:
            data = json.load(f)

        assert data[0]["id"] == 1
        assert data[0]["description"] == "Test task"
        assert data[0]["completed"] is True

    def test_save_tasks_multiple_entries(self, manager, temp_task_file):
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")

        with open(temp_task_file, "r") as f:
            data = json.load(f)

        assert len(data) == 3
        for i, item in enumerate(data, 1):
            assert item["id"] == i


class TestTaskManagerIntegration:
    """Tests de integración del flujo completo."""

    def test_complete_workflow(self, manager, temp_task_file, capsys):
        # Agregar tareas
        manager.add_task("Learn Python")
        manager.add_task("Build project")
        manager.add_task("Deploy")

        # Completar una
        manager.complete_task(2)

        # Listar
        manager.list_task()
        captured = capsys.readouterr()
        assert "[ ] #1: Learn Python" in captured.out
        assert "[✓] #2: Build project" in captured.out
        assert "[ ] #3: Deploy" in captured.out

        # Eliminar una
        manager.delete_task(1)

        # Verificar persistencia
        new_manager = TaskManager()
        assert len(new_manager._tasks) == 2
        assert new_manager._tasks[0].id == 2
        assert new_manager._tasks[0].completed is True
        assert new_manager._tasks[1].id == 3

    def test_persistence_across_instances(self, manager, temp_task_file):
        manager.add_task("Persist this")
        manager.add_task("And this too")
        manager.complete_task(1)

        # Crear nueva instancia
        new_manager = TaskManager()

        assert len(new_manager._tasks) == 2
        assert new_manager._tasks[0].completed is True
        assert new_manager._tasks[1].completed is False
