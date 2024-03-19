from typing import Union
import flet as ft
from flet import UserControl


class Ticket(UserControl):

    def __init__(
        self,
        title: str,
        id: str,
        on_positive_button_click=None,
        on_negative_button_click=None,
        origin_container: ft.Column = None,
    ):
        super().__init__()
        self.title = title
        self.id = id
        self.positive_button = "完了"
        self.negative_button = "削除"
        self.on_positive_button_click = on_positive_button_click
        self.on_negative_button_click = on_negative_button_click
        self.origin_container = origin_container

    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(self.title),
                        ),
                        ft.Row(
                            [
                                ft.TextButton(
                                    self.positive_button,
                                    on_click=self.on_positive_button_click,
                                ),
                                ft.TextButton(
                                    self.negative_button,
                                    on_click=self.on_negative_button_click,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=250,
                padding=10,
            )
        )
