import flet as ft

from pm_kun.screen.unit import create_view


def pmk(page: ft.Page):
    title_text = ft.Text("ここにPMアドバイザーを追加する", size=30, text_align="center")
    back_button = ft.ElevatedButton("メニューに戻る", on_click=lambda _: page.go("/"))

    column = ft.Column(
        spacing=20,
        controls=[title_text, back_button],
        horizontal_alignment="center",
        alignment="center",
    )
    row = ft.Row(controls=[column], alignment="center", vertical_alignment="center")
    return create_view("/pmk", [row])
