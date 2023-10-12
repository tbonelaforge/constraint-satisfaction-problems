class GraphColoringCSP2:
    def __init__(self, nodes, edges, num_colors):
        self.nodes = nodes
        self.edges = edges
        self.num_colors = num_colors
        self.adjacency_lists = self.initialize_adjacency_lists(nodes, edges)
        self.domain_values = list(range(num_colors))
        self.assigned = {}
        self.taken_counts = self.initialize_taken_counts()
        self.untaken_options = self.initialize_untaken_options()

    def is_assignment_complete(self):
        for node in self.nodes:
            if node not in self.assigned:
                return False
        return True

    def select_unassigned_variable(self):
        # Assume assignment not complete

        min_options = None
        max_degree = None
        best_node = None
        for node in self.nodes:
            if node in self.assigned:
                continue
            these_options = self.count_options(node)
            this_degree = self.count_unassigned_constraints(node)
            if min_options is None or these_options < min_options:
                min_options = these_options
                max_degree = this_degree
                best_node = node
            elif these_options == min_options:
                if this_degree > max_degree:
                    max_degree = this_degree
                    best_node = node
        return best_node

    def order_domain_values(self, node):
        untaken_options = self.get_untaken_options(node)
        augmented_options = []
        for value in untaken_options:
            constraining_score = 0
            for neighbor in self.get_neighbors(node):
                if value in self.untaken_options[neighbor]:
                    constraining_score += 1
            augmented_options.append((constraining_score, value))
        augmented_options.sort() # least constraining values first!
        values = map(lambda ao: ao[1], augmented_options)
        return values

    def initialize_adjacency_lists(self, nodes, edges):
        adjacency_lists = { node: [] for node in nodes }
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            adjacency_lists[node1].append(node2)
            adjacency_lists[node2].append(node1)
        return adjacency_lists


    def initialize_taken_counts(self):
        taken_counts = dict()
        for node in self.nodes:
            taken_counts[node] = []
            for i in self.domain_values:
                taken_counts[node].append(0)
        return taken_counts


    def initialize_untaken_options(self):
        untaken_options = dict()
        for node in self.nodes:
            untaken_options[node] = set()
            for i in self.domain_values:
                untaken_options[node].add(i)
        return untaken_options


    def get_neighbors(self, node):
        return self.adjacency_lists[node] 


    def add_assignment(self, node, color):
        self.assigned[node] = color
        self.process_assignment(node, color, True)


    def remove_assignment(self, node):
        color = self.assigned[node]
        self.process_assignment(node, color, False)
        del self.assigned[node]


    def process_assignment(self, node, color, add=True):
        delta = 1 if add else -1
        self.taken_counts[node][color] += delta
        for neighbor in self.get_neighbors(node):
            self.taken_counts[neighbor][color] += delta
            if add: # case is ADD: handle possible taking away of neighbor options
                if color in self.untaken_options[neighbor]:
                    self.untaken_options[neighbor].remove(color)
            else: # case is REMOVE: check if this color can go BACK to an untaken option for this neighbor
                if self.taken_counts[neighbor][color] == 0: # this was the last constraint!
                    self.untaken_options[neighbor].add(color)


    def count_options(self, node):
        return len(self.untaken_options[node])


    def count_unassigned_constraints(self, node):
        unassigned_constraints = 0
        for neighbor in self.get_neighbors(node):
            if neighbor not in self.assigned:
                unassigned_constraints += 1
        return unassigned_constraints


    def get_untaken_options(self, node):
        untaken_options = []
        for i in self.domain_values:
            if i in self.untaken_options[node]:
                untaken_options.append(i)
        return untaken_options 

    