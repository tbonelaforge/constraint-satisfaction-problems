class NQueens2CSP:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns


    def is_assignment_complete(self, assignment):
        for c in range(self.columns):
            if not assignment.is_assigned(c):
                return False
        return True


    def select_unassigned_variable(self, assignment):
        # User min remaining values, to pick the next var to assign to
        min_options = None
        minimizing_var = None
        for var in range(self.columns):
            if assignment.is_assigned(var):
                continue
            these_options = assignment.count_options_for_column(var)
            if min_options is None or these_options < min_options:
                min_options = these_options
                minimizing_var = var
        return minimizing_var


    def order_domain_values(self, var, assignment):
        return assignment.get_unattacked_rows_for_column(var)


    def is_consistent(self, var, val, assignment):
        return True # Should have moved the checking above

    