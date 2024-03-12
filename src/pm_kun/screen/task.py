import flet as ft
from flet_core import Control, UserControl

from pm_kun.screen.unit import Todo, create_view


def view_task(page: ft.Page):
    todo = Todo()
    back_button = ft.ElevatedButton("メニューに戻る", on_click=lambda _: page.go("/"))
    display = ft.Column(controls=[todo.build(), back_button])

    return create_view("/todo", [display])
