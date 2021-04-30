"""CRUD operations on data_model.Tasks

"""
import datetime
import logging
import re
from typing import List, Optional, Any, Dict

import networkx as nx

from .data_model import Task, TimeLog
from .graph import sort_nodes
import json

logger = logging.getLogger(__file__)


def create_task(graph: nx.DiGraph, task: Task) -> int:
    if task.task_id < 0:
        task.task_id = len(graph.nodes)

    task_spec = task.dict(exclude_defaults=True, exclude_none=True, exclude_unset=True)

    graph.add_node(task.task_id, kind="task", **task_spec)
    return task.task_id


def delete_task(graph: nx.DiGraph, task_id: int) -> int:
    raise NotImplementedError()


def update_task(
    graph: nx.DiGraph,
    task_id: int,
    user_id: str = None,
    name: str = None,
    completed: bool = None,
    importance: float = None,
    due: datetime.datetime = None,
) -> Task:
    """sets properties in a given task id by all values in kwargs
    if None, will remove property
    """
    raise NotImplementedError()


def complete_task(
    graph: nx.DiGraph, task_id: int, end_time: datetime.datetime = None,
):
    """sets the end_time to the last time_log (creates one if missing)
    and sets completed flag to True
    """
    raise NotImplementedError()


def add_tag(graph: nx.DiGraph, task_id: int, tag: str):
    raise NotImplementedError()


def remove_tag(graph: nx.DiGraph, task_id: int, tag: str):
    raise NotImplementedError()


def add_url(graph: nx.DiGraph, task_id: int, url: str):
    raise NotImplementedError()


def remove_url(graph: nx.DiGraph, task_id: int, url: str):
    raise NotImplementedError()


def add_user(graph: nx.DiGraph, task_id: int, user: str):
    raise NotImplementedError()


def remove_user(graph: nx.DiGraph, task_id: int, user: str):
    raise NotImplementedError()


def add_note(graph: nx.DiGraph, task_id: int, note: str):
    raise NotImplementedError()


def update_note(graph: nx.DiGraph, task_id: int, node_id: int, note: str):
    raise NotImplementedError()


def remove_note(graph: nx.DiGraph, task_id: int, node_id: int):
    raise NotImplementedError()


# Multiple Task
def list_tasks(
    graph: nx.DiGraph,
    sort_by: str = "importance",
    limit: int = 10,
    ascending=False,
    only_leaves=False,
    search: str = None,
    tags: Optional[List[str]] = None,
    urls: Optional[List[str]] = None,
    users: Optional[List[str]] = None,
):
    # can sort by 'importance','name','due'

    node_ids: List[int] = sort_nodes(
        graph,
        sort_by=sort_by,
        limit=limit,
        ascending=ascending,
        only_leaves=only_leaves,
    )

    # Regexp
    if search is not None and len(search):
        pattern = re.compile(search)
        node_ids = [
            node_id
            for node_id in node_ids
            if pattern(graph.nodes[node_id].get("name", ""))
        ]

    if tags is not None and len(tags):
        tags = set(tags)
        node_ids = [
            node_id
            for node_id in node_ids
            if len(set(graph.nodes[node_id].get("tags", [])).intersection(tags))
        ]

    if urls is not None and len(urls):
        urls = set(urls)
        node_ids = [
            node_id
            for node_id in node_ids
            if len(set(graph.nodes[node_id].get("urls", [])).intersection(urls))
        ]

    if users is not None and len(users):
        users = set(users)
        node_ids = [
            node_id
            for node_id in node_ids
            if len(set(graph.nodes[node_id].get("users", [])).intersection(users))
        ]
    print([graph.nodes[node_id] for node_id in node_ids])
    return [Task(**graph.nodes[node_id]) for node_id in node_ids]
