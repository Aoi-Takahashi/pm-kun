import uuid
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    Row,
    TextField,
    UserControl,
    colors,
    icons,
)


class Task(UserControl):

    def __init__(self, task_name, task_delete, update_task_data):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.task_name = task_name
        self.task_delete = task_delete
        self.update_task_data = update_task_data

    def build(self):
        self.display_task = Checkbox(value=False, label=self.task_name)
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="編集",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="削除",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="編集完了",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update_task_data(self.id, self.display_task.label)
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)


class Todo(UserControl):
    def __init__(self):
        super().__init__()
        self._todos = []

    def build(self):
        self.new_task = TextField(hint_text="TODO内容を入力してください", expand=True)
        self.tasks = Column()

        return Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_delete, self.update_task_data)
        self.tasks.controls.append(task)
        self._todos.append({"id": task.id, "name": task.task_name})
        self.new_task.value = ""
        self.update()

    def update_task_data(self, task_id, new_name):
        for task in self._todos:
            if task["id"] == task_id:
                task["name"] = new_name
                break
        print(self._todos)

    def task_delete(self, task):
        self._todos = [t for t in self._todos if t["id"] != task.id]
        self.tasks.controls.remove(task)
        self.update()

    @property
    def todos(self):
        return self._todos
