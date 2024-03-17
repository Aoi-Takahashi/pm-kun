from typing import List
import flet as ft
from flet import (
    UserControl,
)


def create_view(path: str, component: List[UserControl]):
    return ft.View(
        path,
        component,
    )
