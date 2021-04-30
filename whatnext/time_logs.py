"""CRUD operations on data_model.TimeLog

"""
import datetime
import logging

import networkx as nx

from .data_model import TimeLog

logger = logging.getLogger(__file__)


def create_timelog(graph: nx.DiGraph, task_id: int, time_log: TimeLog) -> int:
    raise NotImplementedError()


def delete_timelog(graph: nx.DiGraph, task_id: int, time_log_id: int) -> int:
    raise NotImplementedError()


def update_timelog_note(
    graph: nx.DiGraph, task_id: int, time_log_id: int, note: str
) -> int:
    raise NotImplementedError()


def start_timelog(
    graph: nx.DiGraph,
    task_id: int,
    time_log_id: int = None,
    start_time: datetime.datetime = None,
) -> datetime.datetime:
    raise NotImplementedError()


def end_timelog(
    graph: nx.DiGraph,
    task_id: int,
    time_log_id: int = None,
    end_time: datetime.datetime = None,
) -> datetime.datetime:
    raise NotImplementedError()

