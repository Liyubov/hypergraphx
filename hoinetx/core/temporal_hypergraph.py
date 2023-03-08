import bisect
from hoinetx.core.attribute_handler import AttributeHandler


class TemporalHypergraph:
    def __init__(self, edges):
        self.__attr = AttributeHandler()
        self.edges = {}
        self._nodes = set()
        self.add_edges(edges)

    def add_edge(self, edge):
        if not isinstance(edge, tuple):
            raise TypeError('Edge must be a tuple')
        if len(edge) != 2:
            raise ValueError('Edge must be a tuple of length 2')
        t = edge[0]
        _edge = tuple(sorted(edge[1]))
        if not isinstance(_edge, tuple):
            raise TypeError('Edge must be a tuple')
        if len(_edge) < 2:
            raise ValueError('Edge must be a tuple of length 2 or more')
        if t < 0:
            raise ValueError('Time must be a positive integer')
        for node in _edge:
            self._nodes.add(node)
        if t not in self.edges:
            self.edges[t] = set([_edge])
        else:
            self.edges[t].add(_edge)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def add_node(self, node):
        self._nodes.add(node)

    def add_nodes(self, nodes):
        for node in nodes:
            self._nodes.add(node)

    def del_edge(self, edge):
        pass

    def del_edges(self, edges):
        pass

    def get_edges(self, time_window=None):
        edges = []
        if time_window is None:
            for t in sorted(self.edges):
                for edge in self.edges[t]:
                    edges.append((t, edge))
        elif isinstance(time_window, tuple) and len(time_window) == 2:
            for t in sorted(self.edges):
                if time_window[0] <= t <= time_window[1]:
                    for edge in self.edges[t]:
                        edges.append((t, edge))
        else:
            for edge in self.edges[time_window]:
                edges.append((time_window, edge))
        return edges

    def aggregate(self, time_window=None):
        from hoinetx.core.hypergraph import Hypergraph
        aggregated = {}
        if not isinstance(time_window, int):
            raise TypeError('Time window must be an integer')
        t = 0
        while t < max(self.edges):
            aggregated[t] = set()
            for edge in self.get_edges((t, t + time_window)):
                aggregated[t].add(edge[1])
            aggregated[t] = Hypergraph(aggregated[t])
            t += time_window
        return aggregated

    def __str__(self):
        for edge in self.edges:
            print(edge)
        return ''




