from graph_coloring_csp import GraphColoringCSP
from graph_coloring_csp2 import GraphColoringCSP2
from n_queens_csp import NQueensCSP
from n_queens2_csp import NQueens2CSP
from n_queens_assignment import NQueensAssignment

NUM_BACKTRACKS = 0

def backtracking_search(csp):
    global NUM_BACKTRACKS
    NUM_BACKTRACKS = 0
    search_result = backtracking_search_recursive({}, csp)
    return (search_result, NUM_BACKTRACKS)

def backtracking_search2(csp):
    global NUM_BACKTRACKS
    NUM_BACKTRACKS = 0
    initial_assignment = NQueensAssignment(csp.rows, csp.columns)
    return backtracking_search_recursive2(initial_assignment, csp)


def backtracking_search3(csp):
    global NUM_BACKTRACKS
    NUM_BACKTRACKS = 0
    search_result = backtracking_search_recursive3(csp)
    return (search_result, NUM_BACKTRACKS)


def backtracking_search_recursive3(csp):
    global NUM_BACKTRACKS
    if csp.is_assignment_complete():
        return csp.assigned

    var = csp.select_unassigned_variable()
    for val in csp.order_domain_values(var):
        csp.add_assignment(var, val)
        result = backtracking_search_recursive3(csp)
        if result is not None:
            return result
        NUM_BACKTRACKS += 1
        csp.remove_assignment(var)
    return None


def backtracking_search_recursive(assignment, csp):
    global NUM_BACKTRACKS
    if csp.is_assignment_complete(assignment):
        return assignment

    var = csp.select_unassigned_variable(assignment)
    for val in csp.order_domain_values(var, assignment):
        if csp.is_consistent(var, val, assignment):
            assignment[var] = val
            result = backtracking_search_recursive(assignment, csp)
            if result is not None:
                return result
            #print("I am having to backtrack!!!")
            #print(assignment)
            NUM_BACKTRACKS += 1
            del assignment[var]
    return None

def backtracking_search_recursive2(assignment, csp):
    global NUM_BACKTRACKS
    if csp.is_assignment_complete(assignment):
        return assignment

    var = csp.select_unassigned_variable(assignment)
    for val in csp.order_domain_values(var, assignment):
        if csp.is_consistent(var, val, assignment):
            assignment.add_assignment(var, val)
            result = backtracking_search_recursive2(assignment, csp)
            if result is not None:
                return result
            #print("I am having to backtrack!!!")
            #print(assignment.assigned)
            NUM_BACKTRACKS += 1
            assignment.remove_assignment(var)
    return None


if __name__ == "__main__":
    
    print("Testing backtracking search on graph of australia...")
    nodes = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
    edges = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'), ('Q', 'NSW'), ('SA', 'NSW'), ('SA', 'V'), ('NSW', 'V')]
    csp = GraphColoringCSP(nodes, edges, 3)
    
    result = backtracking_search(csp)
    print("The result is: ")
    print(result)


    print("Testing backtracking search on simple tree, which should be 2-colorable")
    nodes = ['A', 'C', 'B', 'D']
    edges = [('A', 'B'), ('B', 'D'), ('C', 'D')]
    csp = GraphColoringCSP(nodes, edges, 2)
    result = backtracking_search(csp)
    print("the result is: ")
    print(result)
    print("With NUM_BACKTRACKS: ")
    print(NUM_BACKTRACKS)


    # print("Testing backtracking search on N-queens problem, 4 X 4")
    # csp2 = NQueensCSP(4, 4)

    # result2 = backtracking_search(csp2)
    # print("The result is: ")
    # print(result2)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing the min remaining values optimization...")
    # csp3 = NQueens2CSP(4, 4)

    # result3 = backtracking_search2(csp3)
    # print("The result is: ")
    # print(result3.assigned)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing backtracking search on N-queens problem, 6 X 6")
    # csp2 = NQueensCSP(6, 6)

    # result2 = backtracking_search(csp2)
    # print("The result is: ")
    # print(result2)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing the min remaining values optimization...")
    # csp3 = NQueens2CSP(6, 6)

    # result3 = backtracking_search2(csp3)
    # print("The result is: ")
    # print(result3.assigned)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing backtracking search on N-queens problem, 7 X 7")
    # csp2 = NQueensCSP(7, 7)

    # result2 = backtracking_search(csp2)
    # print("The result is: ")
    # print(result2)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing the min remaining values optimization...")
    # csp3 = NQueens2CSP(7, 7)

    # result3 = backtracking_search2(csp3)
    # print("The result is: ")
    # print(result3.assigned)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing backtracking search on N-queens problem, 8 X 8")
    # csp2 = NQueensCSP(8, 8)

    # result2 = backtracking_search(csp2)
    # print("The result is: ")
    # print(result2)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    # print("Testing the min remaining values optimization...")
    # csp3 = NQueens2CSP(8, 8)

    # result3 = backtracking_search2(csp3)
    # print("The result is: ")
    # print(result3.assigned)
    # print("With %s backtracks" % (NUM_BACKTRACKS))

    print("Testing the new Graph Coloring CSP, with edges: ")
    nodes = ['A', 'B', 'C', 'D', 'E']
    edge_list = [['A', 'D'], ['B', 'E'], ['C', 'E'], ['D', 'E']]
    print(edge_list)
    csp2 = GraphColoringCSP2(nodes, edge_list, 2)
    (search_result, num_backtracks) = backtracking_search3(csp2)
    print("Got search_result, with num_backtracks: ")
    print(search_result)
    print(num_backtracks)

    print("Testing the new-new Graph Coloring CSP, with edges: ")
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    edge_list = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['D', 'E'], ['D', 'F'], ['E', 'F']]
    print(edge_list)
    csp2 = GraphColoringCSP2(nodes, edge_list, 3)
    (search_result, num_backtracks) = backtracking_search3(csp2)
    print("Got search_result, with num_backtracks: ")
    print(search_result)
    print(num_backtracks)

    print("Testing the new-new Graph Coloring CSP, on a 7-node graph, with edges: ")
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edge_list = [['B', 'D'], ['B', 'F'], ['B', 'G'], ['C', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'E'], ['F', 'G']]
    print(edge_list)
    csp2 = GraphColoringCSP2(nodes, edge_list, 3)
    (search_result, num_backtracks) = backtracking_search3(csp2)
    print("Got search_result, with num_backtracks: ")
    print(search_result)
    print(num_backtracks)

    print("Testing the new-new Graph Coloring CSP, on a 7-node graph, with edges: ")
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edge_list = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'E'], ['D', 'F'], ['D', 'G'], ['E', 'F'], ['E', 'G'], ['F', 'G']]
    print(edge_list)
    csp2 = GraphColoringCSP2(nodes, edge_list, 3)
    (search_result, num_backtracks) = backtracking_search3(csp2)
    print("Got search_result, with num_backtracks: ")
    print(search_result)
    print(num_backtracks)
    