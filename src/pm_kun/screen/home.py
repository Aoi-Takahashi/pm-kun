import flet as ft


def home(page: ft.Page):
    page.title = "プロマネ君"

    # Event
    def navigate_todo(e):
        page.go("/todo")
        page.update()

    def navigate_chart(e):
        page.go("/chart")
        page.update()

    def navigate_pmk(e):
        page.go("/pmk")
        page.update()

    # Widgets
    todo_button = ft.FilledButton(text="タスク一覧", on_click=navigate_todo)
    chart_button = ft.FilledButton(text="ガントチャート", on_click=navigate_chart)
    pmk_button = ft.FilledButton(text="PMアドバイザー", on_click=navigate_pmk)
    title_text = ft.Text("プロマネ君", size=30, text_align="center")

    # Layout
    row = ft.Row(
        spacing=30,
        controls=[todo_button, chart_button, pmk_button],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    column = ft.Column(
        spacing=20,
        controls=[title_text, row],
        horizontal_alignment="center",
        alignment="center",
    )
    page.add(column)

    return ft.View(
        "/",
        [column],
    )
