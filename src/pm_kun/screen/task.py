import flet as ft


def task(page: ft.Page):
    page.title = "プロマネ君"

    # Widgets
    title_text = ft.Text("ここにTODO管理機能を追加", size=30, text_align="center")
    back_button = ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/"))

    # Layout
    column = ft.Column(
        spacing=20,
        controls=[title_text, back_button],
        horizontal_alignment="center",
        alignment="center",
    )
    page.add(column)

    return ft.View(
        "/todo",
        [column],
    )
