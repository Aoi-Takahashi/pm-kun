import flet as ft
from pm_kun.screen.component.todo import Todo
from pm_kun.screen.util.create_view import create_view


def view_task(page: ft.Page):
    def navigate_home(e):
        for todo in todo_component.todos:
            page.data.append(todo)
        page.go("/")
        page.update()

    todo_component = Todo()
    back_button = ft.ElevatedButton("メニューに戻る", on_click=navigate_home)
    display = ft.Column(
        controls=[todo_component, back_button],
    )

    return create_view("/todo", [display])
