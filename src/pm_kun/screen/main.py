import flet as ft
from pm_kun.screen.chart import chart
from pm_kun.screen.home import home
from pm_kun.screen.pmk import pmk
from pm_kun.screen.task import task


def main(page: ft.Page):
    page.title = "プロマネ君"

    def route_change(route):
        page.views.clear()
        # Entory point("/")
        page.views.append(home(page))
        if page.route == "/todo":
            page.views.append(task(page))
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
