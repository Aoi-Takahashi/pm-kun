import flet as ft
from flet_core import UserControl
from typing import List


def create_view(path: str, component: List[UserControl]):
    return ft.View(
        path,
        component,
    )


class Todo(ft.UserControl):
    def __init__(self):
        self.title = ft.Text(
            "TODO一覧",
            size=30,
        )
        self.text = ""
        self.todos = ft.Column()
        self.input_todo = ft.TextField(hint_text="TODOを入力してください")
        self.back_button = ft.ElevatedButton(
            "メニューに戻る", on_click=lambda _: self.page.go("/")
        )
        self.input_todo = ft.TextField(hint_text="TODOを入力してください")
        self.add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=self.add_todo
        )

    def build(self):
        self.row_todo_input = ft.Row(
            controls=[self.input_todo, self.add_button], alignment="center"
        )

        self.column = ft.Column(
            spacing=20,
            controls=[
                self.title,
                self.row_todo_input,
                self.todos,
                self.back_button,
            ],
            horizontal_alignment="center",
            alignment="center",
        )
        self.row = ft.Row(
            controls=[self.column], alignment="center", vertical_alignment="center"
        )
        return ft.Row(
            controls=[
                ft.Checkbox(label=self.text),
                ft.IconButton(
                    icon=ft.icons.CREATE_OUTLINED,
                    tooltip="Edit To-Do",
                ),
                ft.IconButton(
                    ft.icons.DELETE_OUTLINE,
                    tooltip="Delete To-Do",
                ),
            ]
        )

    def add_todo(self, e):
        self.list_todo.controls.append(
            ft.Row(
                controls=[
                    ft.Checkbox(label=self.input_todo.value),
                    ft.IconButton(
                        icon=ft.icons.CREATE_OUTLINED,
                        tooltip="Edit To-Do",
                    ),
                    ft.IconButton(
                        ft.icons.DELETE_OUTLINE,
                        tooltip="Delete To-Do",
                    ),
                ]
            )
        )
        self.input_todo.value = ""
        self.input_todo.focus()
        self.page.update()
