"""Chapter 4: Question 2.

Check if there is a path between two nodes in a directed graph.
Modified to return the path itself if one was found.
"""

from src.utils.queue import Queue


def find_path(graph_obj, source_id, dest_id):
    """Uses a BFS algorithm to find a path: source_id --> dest_id.

    Args:
        graph_obj: An instance object of class DirectedGraph.
        source_id: Id of the source node.
        dest_id: Id of the destination node.
    Returns:
        If a path was found, returns a list of node ids.
        Otherwise, returns an empty list.
    Raises:
        IndexError: If source or destination ids do not exist in the graph.
    """
    if source_id not in graph_obj.nodes or dest_id not in graph_obj.nodes:
        raise IndexError('Node id does not exist in the graph.')

    if source_id == dest_id:
        return [source_id]
    
    previous = {}
    q = Queue()
    q.enqueue(source_id)
    visited = {source_id}
    found = False
    while not q.is_empty() and not found:
        node_id = q.dequeue()
        for adj_id in graph_obj.get_adj_node_ids(node_id):
            if adj_id not in visited:
                visited.add(adj_id)
                q.enqueue(adj_id)
                previous.update({adj_id: node_id})
                if adj_id == dest_id:
                    found = True
                    break
    path = []
    if found:
        current_id = dest_id
        while current_id != source_id:
            path.append(current_id)
            current_id = previous[current_id]
        path.append(current_id)
        path.reverse()

    return path

