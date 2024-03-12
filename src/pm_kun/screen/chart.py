import flet as ft
from pm_kun.screen.unit import create_view


def chart(page: ft.Page):
    title_text = ft.Text(
        "ここにタスクのチャート化したTODOを表示する", size=30, text_align="center"
    )
    back_button = ft.ElevatedButton("メニューに戻る", on_click=lambda _: page.go("/"))

    display = ft.Column(
        spacing=20,
        controls=[title_text, back_button],
        horizontal_alignment="center",
        alignment="center",
    )
    row = ft.Row(controls=[display], alignment="center", vertical_alignment="center")
    return create_view("/chart", [row])
