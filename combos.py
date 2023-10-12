from graph_coloring_csp import GraphColoringCSP
from graph_coloring_csp2 import GraphColoringCSP2
from backtracking_search import backtracking_search, backtracking_search3

def combos(elements, k):
    n = len(elements)
    if k == 0:
        return [[]]
    results = []
    for i in range(n - k + 1):
        sub_results = combos(elements[i + 1:], k - 1)
        for sub_result in sub_results:
            result = [elements[i]]
            result.extend(sub_result)
            results.append(result)
    return results

def test_all_graphs(nodes, CLS=GraphColoringCSP, fn=backtracking_search):
    print("For the following nodes: ")
    print(nodes)
    print("We have edge possibilities: ")
    edge_possibilities = combos(nodes, 2)
    print(edge_possibilities)

    for j in range(len(edge_possibilities)):
        these_edges = combos(edge_possibilities, j + 1)
        for edge_list in these_edges:
            for i in range(len(nodes)):
                csp = CLS(nodes, edge_list, i + 1)
                (search_result, num_backtracks) = fn(csp)
                
                if search_result is not None: # found the chromatic number (i + 1)
                    if num_backtracks > 0: # This is a "problem case" which causes backtracks to occur
                        print("For the edge_list: ")
                        print(edge_list)
                        print("The chromatic number is %s, with %s backtracks:" % (i + 1, num_backtracks))
                        print(search_result)
                        
                    break


if __name__ == "__main__":
    # print("Testing 6 choose 3")

    # elements = [0, 1, 2, 3, 4, 5]
    # results = combos(elements, 3)
    # print("Got results: ")
    # print(results)

    # print("For the following nodes: ")
    # print("Testing original algorithm...")
    # nodes = ['A', 'B', 'C', 'D']
    # test_all_graphs(nodes)
    # print()
    
    # nodes = ['A', 'B', 'C', 'D', 'E']
    # test_all_graphs(nodes)

    print("Now testing minimum remaining values improvement on all 5-node graphs...")
    nodes = ['A', 'B', 'C', 'D', 'E']
    test_all_graphs(nodes, GraphColoringCSP2, backtracking_search3)

    print("Now testing a 6 node graph...")
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    test_all_graphs(nodes, GraphColoringCSP2, backtracking_search3)

    print("Now testing a 7 node graph...")
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    test_all_graphs(nodes, GraphColoringCSP2, backtracking_search3)






                