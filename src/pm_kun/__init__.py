import datetime
from typing import Optional
from pm_kun.pmgpt.main import generate_response
from pm_kun.screen.main import main as Screen
from pm_kun.task.todo import BaseTask
from pm_kun.type_definition import Priority, Status, ToDo
import uuid
import flet as ft


def main() -> None:
    print("This is Entory point for pm-kun.")
    is_process = False
    my_task = BaseTask()
    # question = input("質問を入力してください")
    # context = input("コンテキストを入力してください")
    # print(generate_response(user_input=question, user_context=context))
    Screen
    # while is_process:
    #     print("1.タスクの追加")
    #     print("2.タスクの削除")
    #     print("3.タスクの更新")
    #     print("4.終了")
    #     select = input("選択してください")
    #     if select == "1":
    #         task = input("タスクを入力してください")
    #         my_Todo: ToDo = {
    #             "id": str(uuid.uuid4()),
    #             "task": "",
    #             "status": Status.未着手,
    #             "period": datetime.date.today(),
    #             "priority": Priority.低,
    #         }
    #         my_Todo["id"] = str(uuid.uuid4())
    #         my_Todo["task"] = task
    #         my_task.add_task(my_Todo)
    #         print(f"TODOの数：{len(my_task.todo_list)}")
    #         print(my_task.todo_list)
    #     elif select == "2":
    #         task = input("削除するタスクを入力してください")
    #         for todo in my_task.todo_list:
    #             if task in todo["task"]:
    #                 id = todo["id"]
    #                 my_task.delete_task(id)
    #         print(my_task.todo_list)
    #     elif select == "3":
    #         cuurent_task = input("更新するタスクを入力してください")
    #         update_task = input("更新後のタスクを入力してください")
    #         for todo in my_task.todo_list:
    #             if cuurent_task in todo["task"]:
    #                 id = todo["id"]
    #                 my_task.update_task(id, task=update_task)
    #         print(my_task.todo_list)
    #     elif select == "4":
    #         break
