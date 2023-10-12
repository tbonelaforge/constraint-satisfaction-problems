class GraphColoringCSP:
    def __init__(self, nodes, edges, num_colors):
        self.nodes = nodes
        self.edges = edges
        self.num_colors = num_colors
        self.adjacency_lists = self.initialize_adjacency_lists(nodes, edges)
        self.domain_values = list(range(num_colors))

    def is_assignment_complete(self, assignment):
        for node in self.nodes:
            if node not in assignment:
                return False
        return True

    def select_unassigned_variable(self, assignment):
        # Assume assignment not complete

        for node in self.nodes:
            if node not in assignment:
                return node
        return None # should never get here

    def order_domain_values(self, var, assignment):
        return self.domain_values

    def is_consistent(self, var, val, assignment):
        for n in self.get_neighbors(var):
            if n in assignment:
                color = assignment[n]
                if color == val: # disallow adjacent nodes to have same color
                    return False
        return True

    def initialize_adjacency_lists(self, nodes, edges):
        adjacency_lists = { node: [] for node in nodes }
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            adjacency_lists[node1].append(node2)
            adjacency_lists[node2].append(node1)
        return adjacency_lists

    def get_neighbors(self, node):
        return self.adjacency_lists[node]                              

if __name__ == "__main__":
    print("Testing the construction of a new GraphColoringCSP instance...")
    nodes = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
    edges = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'), ('Q', 'NSW'), ('SA', 'NSW'), ('SA', 'V'), ('NSW', 'V')]
    csp = GraphColoringCSP(nodes, edges)
    print("After constructing the new csp, it has adjacency lists: ")
    print(csp.adjacency_lists)