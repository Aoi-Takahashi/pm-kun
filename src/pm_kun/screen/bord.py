from typing import Union
import flet as ft
from flet import Draggable, DragTargetAcceptEvent
from pm_kun.screen.component.ticket import Ticket
from pm_kun.screen.util.create_view import create_view


def view_chart(page: ft.Page):
    todos_unselected = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )
    todos_high = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )
    todos_normal = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )
    todos_complete = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )

    def complete_ticket(parent_container: Union[ft.Column, ft.Row], control_id: str):
        def handler(e):
            src = None
            for control in parent_container.controls:
                if isinstance(control, Draggable) and control.content.id == control_id:
                    src = control
                    break

            if src:
                completed_task = Draggable(
                    group="task",
                    content=Ticket(
                        title=src.content.title,
                        id=src.content.id,
                        on_positive_button_click=complete_ticket(
                            todos_complete, src.content.id
                        ),
                        on_negative_button_click=delete_ticket(
                            todos_complete, src.content.id
                        ),
                        origin_container=todos_complete,
                    ),
                )
                todos_complete.controls.append(completed_task)
                todos_complete.update()

                parent_container.controls.remove(src)
                parent_container.update()

        return handler

    def delete_ticket(parent_container: Union[ft.Column, ft.Row], control_id: str):
        def handler(e):
            for control in parent_container.controls:
                if isinstance(control, Draggable) and control.content.id == control_id:
                    parent_container.controls.remove(control)
                    parent_container.update()
                    break

        return handler

    def drag_accept(
        target_container: ft.Column, from_container: str, e: DragTargetAcceptEvent
    ):
        src = page.get_control(e.src_id)
        if (
            hasattr(src.content, "origin_container")
            and src.content.origin_container is not None
        ):
            src.content.origin_container.controls.remove(src)
            src.content.origin_container.update()

        if from_container == "high":
            src.content.origin_container = todos_high
        elif from_container == "normal":
            src.content.origin_container = todos_normal
        elif from_container == "complete":
            src.content.origin_container = todos_complete
        else:
            src.content.origin_container = todos_unselected

        accept_task = Draggable(
            group="task",
            content=Ticket(
                title=src.content.title,
                id=src.content.id,
                on_positive_button_click=complete_ticket(
                    target_container, src.content.id
                ),
                on_negative_button_click=delete_ticket(
                    target_container, src.content.id
                ),
                origin_container=src.content.origin_container,
            ),
        )
        target_container.controls.append(accept_task)
        target_container.update()

    back_button = ft.ElevatedButton("メニューに戻る", on_click=lambda _: page.go("/"))

    for data in page.data:
        todos_unselected.controls.append(
            Draggable(
                data=f"{data['name']}|{data['id']}",
                group="task",
                content=Ticket(
                    title=data["name"],
                    id=data["id"],
                    on_positive_button_click=complete_ticket(
                        todos_unselected, data["id"]
                    ),
                    on_negative_button_click=delete_ticket(
                        todos_unselected, data["id"]
                    ),
                    origin_container=todos_unselected,
                ),
            )
        )

    area_unselected = ft.DragTarget(
        group="task",
        content=ft.Container(
            content=todos_unselected,
            width=250,
            height=600,
        ),
        on_accept=lambda e: drag_accept(todos_unselected, "none", e),
    )

    label_high = ft.Text("重要", size=20, text_align="center")
    priority_high = ft.DragTarget(
        group="task",
        content=ft.Container(
            content=todos_high,
            width=250,
            height=600,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=5,
        ),
        on_accept=lambda e: drag_accept(todos_high, "high", e),
    )
    area_high = ft.Column(
        controls=[label_high, priority_high],
        alignment="center",
    )

    label_normal = ft.Text("標準", size=20, text_align="center")
    priority_normal = ft.DragTarget(
        group="task",
        content=ft.Container(
            content=todos_normal,
            width=250,
            height=600,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=5,
        ),
        on_accept=lambda e: drag_accept(todos_normal, "normal", e),
    )
    area_normal = ft.Column(
        controls=[label_normal, priority_normal],
        alignment="center",
    )

    label_complete = ft.Text("完了", size=20, text_align="center")
    complete = ft.DragTarget(
        group="task",
        content=ft.Container(
            content=todos_complete,
            width=250,
            height=600,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=5,
        ),
        on_accept=lambda e: drag_accept(todos_complete, "complete", e),
    )
    area_complete = ft.Column(
        controls=[label_complete, complete],
        alignment="center",
    )

    display = ft.Row(
        controls=[area_unselected, area_high, area_normal, area_complete],
        alignment="center",
    )

    return create_view("/chart", [ft.Column(controls=[display, back_button])])
