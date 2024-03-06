from datetime import date
from typing import List, Optional
from pm_kun.type_definition import Priority, Status, ToDo


def main() -> None:
    print("""ここではpm-kunのTODOリストの作成と管理を行います。""")
    return None


class BaseTask:
    """
    タスクを管理するクラス。
    このクラスはタスクの追加、削除、更新、検索を行う
    """

    def __init__(self) -> None:
        self.todo_list: List[ToDo] = []
        pass

    def add_task(self, task: ToDo) -> None:
        """
        タスクを追加するメソッド
        Args:
            todo:ToDo 追加するタスク
        """
        self.todo_list.append(task)
        return None

    def delete_task(self, id: str) -> None:
        """
        タスクを削除するメソッド
        Args:
        """
        for todo in self.todo_list:
            if todo["id"] == id:
                self.todo_list.remove(todo)
                break
        return None

    def update_task(
        self,
        id: str,
        task: Optional[str] = None,
        status: Optional[Status] = None,
        period: Optional[date] = None,
        priority: Optional[Priority] = None,
    ) -> None:
        """
        タスクを更新するメソッド
        Args:
        """
        for todo in self.todo_list:
            if todo["id"] == id:
                if task is not None:
                    todo["task"] = task
                if status is not None:
                    todo["status"] = status
                if period is not None:
                    todo["period"] = period
                if priority is not None:
                    todo["priority"] = priority
                break
        return None

    def search_task(self, id: str) -> None:
        """
        タスクを検索するメソッド
        Args:
        """
        for task in self.todo_list:
            if task["id"] == id:
                return task
