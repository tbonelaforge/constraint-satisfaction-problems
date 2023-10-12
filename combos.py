from graph_coloring_csp import GraphColoringCSP
from graph_coloring_csp2 import GraphColoringCSP2
from backtracking_search import backtracking_search, backtracking_search3

def combos(elements, k):
    # print("INside combos, got called with elements: ")
    # print(elements)
    n = len(elements)
    if k == 0:
        return [[]]
    results = []
    for i in range(n - k + 1):
        # print("Considering i = %s" % (i))
        sub_results = combos(elements[i + 1:], k - 1)
        # print("got sub_results: ")
        # print(sub_results)
        for sub_result in sub_results:
            result = [elements[i]]
            result.extend(sub_result)
            results.append(result)
    return results

def test_all_graphs(nodes, CLS=GraphColoringCSP, fn=backtracking_search):
    print("For the following nodes: ")
    print(nodes)
    # nodes = ['A', 'B', 'C', 'D']
    print("We have edge possibilities: ")
    edge_possibilities = combos(nodes, 2)
    print(edge_possibilities)

    for j in range(len(edge_possibilities)):
        these_edges = combos(edge_possibilities, j + 1)
        # print("These edges: ")
        # print(these_edges)
        for edge_list in these_edges:
            # print("Constructing a graph with edge list: ")
            # print(edge_list)
            
            for i in range(len(nodes)):
                #print("Trying to color with %s colors: " % (i + 1))
                csp = CLS(nodes, edge_list, i + 1)
                (search_result, num_backtracks) = fn(csp)
                
                if search_result is not None:
                    # print("the chromatic number is %s, with result: " % (i + 1))
                    # print(search_result)
                    # print("With NUM_BACKTRACKS - ")
                    # print(num_backtracks)
                    if num_backtracks > 0:
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






                