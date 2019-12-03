import random


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add the vertex into the path
            :param vertex: the vertex ready to be added
            :return: return nothing
            """
            self.vertices.append(vertex)

        def remove_vertex(self):
            """
            Pop the vertex in the path
            :return: return nothing
            """
            if self.is_empty():
                return None
            self.vertices.pop()

        def last_vertex(self):
            """
            Get the last vertex in the path
            :return: return the last vertex in the path
            """
            if self.is_empty():
                return None
            return self.vertices[-1]

        def is_empty(self):
            """
            Check whether the path is empty or not
            :return: return boolean
            """
            return len(self.vertices) == 0

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            Add edge into the vertex
            :param destination: Add the vertex to the self
            :return: return none
            """
            new_edge = Graph.Edge(self, destination)
            self.edges.append(new_edge)

        def degree(self):
            """
            Get the degree of the vertex
            :return: The length of the vertex
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            Get the edge that goes to a specified destination node
            :param destination: The edge to be checked in the edges list
            :return: return the edge if it exists in the edges list
            """
            for edge in self.edges:
                if edge.destination == destination:
                    return edge
            return None

        def get_edges(self):
            """
            Get the list of the edge
            :return: The list of edge
            """
            return self.edges

        def set_fake(self):
            """
            Set the Vertex to fake
            :return: return nothing
            """
            self.fake = True

        def visit(self):
            """
            Set the vertex to be visited
            :return: return nothing
            """
            self.visited = True

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        """
        Get the vertex of the ID
        :param ID: The ID of list of vertex
        :return: return the edges list of ID
        """
        return self.adj_list.get(ID)

    def construct_graph(self):
        """
        Construct the graph, add the vertex and edges into the graph
        :return: return the constructed graph
        """
        if self.filename is None:
            if self.size <= 0:
                raise GraphError
            if self.connectedness < 0 or self.connectedness > 1:
                raise GraphError

            edges = self.generate_edges()

            for edge in edges:
                source = edge[0]
                des = edge[1]
                if source not in self.adj_list:
                    self.adj_list[source] = Graph.Vertex(source)
                if des not in self.adj_list:
                    self.adj_list[des] = Graph.Vertex(des)
                self.get_vertex(source).add_edge(des)

        if self.filename is not None:
            try:
                file = open(self.filename, "r")
            except FileNotFoundError:
                raise GraphError

            for line in file:
                vertex_list = line.split()
                source = int(vertex_list[0])
                des = int(vertex_list[1])
                if source not in self.adj_list:
                    self.adj_list[source] = Graph.Vertex(source)
                if des not in self.adj_list:
                    self.adj_list[des] = Graph.Vertex(des)
                self.get_vertex(source).add_edge(des)

    def BFS(self, start, target):
        """
        BFS searching method
        :param start: The start vertex in the graph
        :param target: The target vertex in the graph
        :return: return the path created to represent the route
        """
        path_list = []  # Store the returned adjacent
        ini_vertex = self.get_vertex(start)  # The vertex of start
        ini_path = self.Path([])  # The path to record

        if ini_vertex is None:
            return ini_path

        ini_vertex.visit()  # Set the ini_vertex as visited
        ini_path.add_vertex(start)  # 加入vertex 1
        path_list.append(ini_path)  # 将path 1 加入list

        while len(path_list) != 0:
            path = path_list.pop(0) # Created in the Path class
            cur_vertex = self.get_vertex(path.last_vertex())
            if cur_vertex.get_edge(target):  # If destination == destination 说明找到了
                new_id = cur_vertex.get_edge(target).destination
                path.add_vertex(new_id)                 # All!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                self.get_vertex(new_id).visit()
                return path
                break
            else:
                edge_list = cur_vertex.get_edges()
                for edge in edge_list:
                    new_path = path.vertices[:]
                    new_path = self.Path(new_path)
                    new_path.add_vertex(edge.destination)
                    path_list.append(new_path)
        return self.Path([])

    def DFS(self, start, target, path=Path()):
        """
        DFS search method
        :param start: The start vertex
        :param target: The target vertex
        :param path: The path ready to be returned
        :return: return the path of the DFS searched route
        """
        start_vertex = self.get_vertex(start)  # vertex 1
        path.add_vertex(start)
        start_vertex.visit()  # 1 被读过了
        edge_list = start_vertex.get_edges()  # source destination stuff

        if path.last_vertex() == target:
            return path

        for edge in edge_list:
            if not self.get_vertex(edge.destination).visited:
                self.DFS(edge.destination, target, path)
                if path.last_vertex() == target:
                    return path
        path.remove_vertex()

def fake_emails(graph, mark_fake=False):
    """
    The function to tease out the fake emails
    :param graph: The graph to
    :param mark_fake: The identification of fake flag
    :return: return the checked email graph
    """
    for ver in graph.adj_list:
        if not ver.visited:
            check_fake_emails(ver)

    def check_fake_emails(start, emails=list()):
        ver_id = graph.get_vertex(start)
        if ver_id:
            if ver_id.degree == 0:
                emails.append(ver_id)
                return check_fake_emails(ver_id, emails)

    pass


def main():
    # filename = "test.txt"
    # stu = Graph(filename=filename)
    # stu = Graph(filename= "test2.txt")
    #print(stu.get_vertex(1))
    #print(stu.get_vertex(1).get_edge(2).destination)
    #print(stu.get_vertex(1).get_edges())
    # path = stu.DFS(1, 9)
    # print(path)
    stu = Graph(20, 0.1)

    fake = Graph.fake_emails(stu, True)



if __name__ == '__main__':
    main()