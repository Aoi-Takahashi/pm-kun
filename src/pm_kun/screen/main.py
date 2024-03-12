import flet as ft
from pm_kun.screen.chart import chart
from pm_kun.screen.unit import create_view
from pm_kun.screen.home import view_home
from pm_kun.screen.pmk import pmk
from pm_kun.screen.task import Todo, view_task

"""
①各画面の実装をクラス化する
②TODO画面の実装を完成せさせる
③TODOの配列を他の画面に渡せるようにする
④TODOの内容をもとにガントチャートを作成する
⑤CSVファイルを読み込んでTODO一覧を作成する
⑥PMK画面の実装を完成させる
"""


def main(page: ft.Page):
    page.title = "プロマネ君"

    # Entory Point(Routing)
    def route_change(route):
        page.views.clear()
        page.views.append(view_home(page))
        if page.route == "/todo":
            page.views.append(view_task(page))
        if page.route == "/chart":
            page.views.append(chart(page))
        if page.route == "/pmk":
            page.views.append(pmk(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)

if __name__ == "__main__":
    ft.app(target=main)
