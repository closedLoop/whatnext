import datetime
import json
import logging
import os

import networkx as nx
from networkx.readwrite.gml import read_gml, write_gml

from ..data_model import Task

logger = logging.getLogger(__file__)

fields_to_encode = ["due", "tags", "urls", "users", "notes", "time_logs"]


def default(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return {"_isoformat": obj.isoformat()}
    return super().default(obj)


def object_hook(obj):
    _isoformat = obj.get("_isoformat")
    if _isoformat is not None:
        return datetime.datetime.fromisoformat(_isoformat)
    return obj


def format_filename(fname: str = None) -> str:
    root_path = os.environ.get("HOME", "~")
    if fname is None:
        fname = os.path.join(root_path, ".whatnext.gml")
    return fname


def load_from_file(fname: str = None) -> nx.DiGraph:
    task_graph = read_gml(format_filename(fname))

    for node_id in task_graph.nodes:
        if task_graph.nodes[node_id].get("kind", "task"):
            for field in fields_to_encode:
                value = task_graph.nodes[node_id].get(field, None)
                if value is not None:
                    task_graph.nodes[node_id][field] = json.loads(
                        value, object_hook=object_hook
                    )

    return task_graph


def save_to_file(graph, fname: str = None):
    g = graph.copy(as_view=False)  # copy data

    for node_id in g.nodes:
        if g.nodes[node_id].get("kind", "task"):
            for field in fields_to_encode:
                if field in g.nodes[node_id]:
                    value = g.nodes[node_id][field]
                    if isinstance(value, list) and len(value) == 0:
                        del g.nodes[node_id][field]
                    elif value is None:
                        del g.nodes[node_id][field]
                    else:
                        g.nodes[node_id][field] = json.dumps(value, default=default)

    return write_gml(g, format_filename(fname))
