"""Find and return a path between two nodes on a graph."""


class GraphNode:

    def __init__(self, node_id=None, value=None):
        self.id = node_id
        self.value = value
        self.adj = set()


class Graph:

    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node_id, value):
        if node_id is not None:
            if node_id not in self.nodes:
                n = GraphNode(node_id, value)
                self.nodes.update({node_id: n})
                return (node_id, value)
        return None

    def update_node_value(self, node_id, value):
        if node_id is not None:
            if node_id in self.nodes:
                self.nodes[node_id].value = value
                return (node_id, value)
        return None

    def add_edge(self, id1, id2):
        if id1 != id2:
            if id1 in self.nodes and id2 in self.nodes:
                self.nodes[id1].adj.add(id2)
                return (id1, id2)
        return None
    

    def find_path(self, source, dest):
        if source not in self.nodes or dest not in self.nodes:
            return None
        previous = {}
        q = Queue()
        q.enqueue(source)
        seen = {source}
        found = False
        while not q.is_empty() and not found:
            node_id = q.dequeue()
            for i in self.nodes[node_id].adj:
                if i not in seen:
                    seen.add(i)
                    q.enqueue(i)
                    previous.update({i: node_id})
                    if i == dest:
                        found = True
                        break
        path = []
        if found:
            n = dest
            while n != source:
                path.append(n)
                n = previous[n]
            path.append(n)
            path.reverse()

        return path


class QueueNode:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, item):
        n = QueueNode(item)
        if self.is_empty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
            
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            n = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return n.data

    def is_empty(self):
        return self.head == None        
        
            
def test():
    g = Graph()
    for i in range(7):
        g.add_node(i, i*10)
    
    edges = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (5, 6), (6, 3)]
    for t in edges:
        g.add_edge(t[0], t[1])

    print(g.find_path(0, 6))


if __name__ == '__main__':
    test()
