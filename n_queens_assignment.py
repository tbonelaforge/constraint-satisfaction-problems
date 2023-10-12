class NQueensAssignment:

    ATTACK_DIRECTIONS = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ]

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.attack_counts = [
            [0 for j in range(columns)] for i in range(rows)
        ]
        self.assigned = dict() # { c: r }

    def is_assigned(self, c):
        if c in self.assigned:
            return True
        return False

    def add_assignment(self, c, r):
        self.assigned[c] = r
        self.process_assignment(c, r, True)

    def remove_assignment(self, c):
        r = self.assigned[c]
        self.process_assignment(c, r, False)
        del self.assigned[c]
        

    def process_assignment(self, c, r, add=True):
        delta = 1 if add else -1
        self.attack_counts[r][c] += delta
        for direction in self.ATTACK_DIRECTIONS:
            pos = [r + direction[0], c + direction[1]]
            while self.is_in_bounds(pos):
                self.attack_counts[pos[0]][pos[1]] += delta
                pos[0] += direction[0]
                pos[1] += direction[1]

  
    def count_options_for_column(self, c):
        unattacked_rows = self.get_unattacked_rows_for_column(c)
        return len(unattacked_rows)


    def get_unattacked_rows_for_column(self, c):
        unattacked_rows = []
        for r in range(self.rows):
            if self.attack_counts[r][c] == 0:
                unattacked_rows.append(r)
        return unattacked_rows


    def is_in_bounds(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= self.rows or pos[1] >= self.columns:
            return False
        return True
    