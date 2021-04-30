import logging
from typing import List

import networkx as nx
import pyfiglet
import typer
from colorama import init as init_colorama
from tabulate import tabulate
from termcolor import colored

from .data_model import Task, TimeLog
from .graph import create_graph, load, save
from .parser import parse
from .tasks import list_tasks

# Global variables (I know, I know...)
app = typer.Typer()
graph: nx.DiGraph = None

# Configuration / Logging
init_colorama(autoreset=True)
logger = logging.getLogger(__file__)


def get_banner(color="green"):
    """JS Stick Letters
    https://github.com/pwaller/pyfiglet
    http://patorjk.com/software/taag/#p=testall&f=Acrobatic&t=WhatNext%20-%3E
    """
    # pylint: disable=anomalous-backslash-in-string
    banner = """
>>                ___          ___     ___
>> |  | |__|  /\   |     |\ | |__  \_/  |   ___\\
>> |/\| |  | /~~\  |     | \| |___ / \  |      /
>>
"""
    # Coloring https://pypi.org/project/colorama/
    return colored(
        "\n".join([b for b in banner.splitlines() if len(b.strip())]), color=color,
    )


# https://pypi.org/project/tabulate/
# table = [
#     ["Sun", 696000, 1989100000],
#     ["Earth", 6371, 5973.6],
#     ["Moon", 1737, 73.5],
#     ["Mars", 3390, 641.85],
# ]
# print(tabulate(table))

# header.__doc__ = get_banner()
# CRUD Task

# create_task
# update_task
#
# list_tasks
# view_task
# start -> adds a time


@app.command()
def show():
    # Taken from https://codegolf.stackexchange.com/questions/11693/ascii-visualize-a-graph#
    # https://stackoverflow.com/questions/834395/python-ascii-graph-drawing
    R = " ".join([",".join(e) for e in graph.edges()])

    # TODO more sophisticed sorting
    V = sorted(list(set(R) - {","}))
    T = [" "] * 40
    for e in R.split():
        x, y = sorted(map(V.index, e[::2]))
        typer.echo(" ".join(T[:x] + ["+" + "--" * (y - x - 1) + "->"] + T[y + 1 :]))
        T[x] = T[y] = "|"
        typer.echo(" ".join(T))
    typer.echo(colored(" ".join(V), color="green"))


@app.command("list")
def cli_list_tasks(
    sort_by: str = "importance",
    limit: int = 10,
    ascending=False,
    all_tasks: bool = True,
    search: str = None,
    tags: List[str] = None,
    urls: List[str] = None,
    users: List[str] = None,
):

    tasks = list_tasks(
        graph,
        sort_by=sort_by,
        limit=limit,
        ascending=ascending,
        only_leaves=not all_tasks,
        search=search,
        tags=tags,
        urls=urls,
        users=users,
    )
    typer.echo(tabulate([t.dict() for t in tasks]))


@app.command("task")
def next_task():
    global graph
    print("NXT")


@app.command()
def delete_all(
    force: bool = typer.Option(..., prompt="Are you sure you want to delete all tasks?")
):
    global graph
    if force:
        typer.echo("Deleting graph")
        graph = create_graph()
        save(graph)
    else:
        typer.echo("Aborted")


@app.command("add")
def add(new_task_or_tasks: str):
    global graph
    num_tasks = len(graph.nodes)
    graph = parse(graph, new_task_or_tasks)
    num_tasks2 = len(graph.nodes)
    typer.echo(f"Created {num_tasks2 - num_tasks} tasks")
    save(graph)


def main():
    global graph
    typer.echo(get_banner())

    try:
        graph = load()
    except Exception as e:
        logger.error(f"Graph Load Exception {e}: graph data might be corrupted")
        return

    app()


if __name__ == "__main__":
    main()
