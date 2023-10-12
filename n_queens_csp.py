class NQueensCSP:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def is_assignment_complete(self, assignment):
        for c in range(self.columns):
            if c not in assignment:
                return False
        return True

    def select_unassigned_variable(self, assignment):
        # assume assignment is not complete
        
        for c in range(self.columns):
            if c not in assignment:
                return c
        return None

    def order_domain_values(self, var, assignment):
        return list(range(self.rows))

    def is_consistent(self, var, val, assignment):
        for (col, row) in assignment.items():
            if self.can_attack((row, col), (val, var)):
                return False
        return True

    def can_attack(self, pos1, pos2):

        if pos1[0] == pos2[0]: # same row
            return True
        if pos1[1] == pos2[1]: #same column
            return True
        if pos2[1] - pos1[1] == pos2[0] - pos1[0]: # diagonal down
            return True
        if pos2[1] - pos1[1] == pos1[0] - pos2[0]: # diagonal up
            return True