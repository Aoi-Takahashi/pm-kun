from pm_kun.pmgpt.main import generate_response
import flet as ft
from pm_kun.screen.bord import view_chart
from pm_kun.screen.home import view_home
from pm_kun.screen.pmk import pmk
from pm_kun.screen.task import view_task

# TODO: PMK画面の実装を完成させる


def main(page: ft.Page) -> None:
    # question = input("質問を入力してください")
    # context = input("コンテキストを入力してください")
    # print(generate_response(user_input=question, user_context=context))
    page.title = "プロマネ君"
    page.window_width = 1050
    page.window_height = 800
    page.data = []

    def route_change(route) -> None:
        page.views.clear()
        page.views.append(view_home(page))
        if page.route == "/todo":
            page.views.append(view_task(page))
        if page.route == "/chart":
            page.views.append(view_chart(page))
        if page.route == "/pmk":
            page.views.append(pmk(page))
        page.update()

    def view_pop(view) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)

if __name__ == "__main__":
    ft.app(target=main)
