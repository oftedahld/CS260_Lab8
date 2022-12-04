#
#  Lab8_main.py
#
#  Created by Jim Bailey on 6/2/2020
#  Licensed under a Creative Commons Attribution 4.0 International License.
#
from DGraph import DGraph


def main():
    # define tree

    tree = DGraph()

    print("Testing non-weighted directed graph")

    # add nodes
    tree.addNode('A')
    tree.addNode('C')
    tree.addNode('T')
    tree.addNode('Z')
    tree.addNode('X')
    tree.addNode('K')
    tree.addNode('Q')
    tree.addNode('J')
    tree.addNode('M')
    tree.addNode('U')

    # add and list edges
    tree.addEdge('A', 'C')
    tree.addEdge('A', 'T')
    tree.addEdge('A', 'Z')
    tree.addEdge('X', 'C')
    tree.addEdge('C', 'X')
    tree.addEdge('C', 'K')
    tree.addEdge('T', 'Q')
    tree.addEdge('K', 'Q')
    tree.addEdge('Q', 'J')
    tree.addEdge('J', 'M')
    tree.addEdge('Z', 'X')
    tree.addEdge('U', 'M')
    tree.addEdge('K', 'X')

    print("The list of nodes")
    print(" expected A C T Z X K Q J M U")
    print(" actually " + tree.listNodes(), end = "\n\n")

    print("The graph edge list is:")
    print(tree.displayEdges(), end="\n\n")

    #uncomment this to display the adjacency matrix
    print("The adjacency or edge matrix is:")
    print(tree.displayMatrix(), end="\n")

    print("The breadth first traversal from A")
    print(" expected A: Z T C X Q K J M with U unreachable")
    print(" actually " + tree.breadthFirst('A'), end="\n\n")    

    print("The depth first traversal from A")
    print(" expected A: Z X C K Q J M T with U unreachable")
    print(" actually " + tree.depthFirst('A'), end="\n\n")

    # now show connectivity Table
    print("The graph connect table should be: ")
    print("A: Z T C X Q K J M ")
    print("C: K X Q J M")
    print("T: Q J M")
    print("Z: X C K Q J M")
    print("X: C K Q J M")
    print("K: X Q C J M ")
    print("Q: J M")
    print("J: M")
    print("M:")
    print("U: M " )

    #uncomment this line to test the connection table
    print("\nactually: ")
    print(tree.connectTable(), end="\n")
    
    #uncomment these line to test the minimum spanning tree
    print("The minimum spanning tree from Z ")
    print(" expected Z: Z-X X-C C-K K-Q Q-J J-M ")
    print(" actually " + tree.minTree('Z'), end = "\n\n")

    print("The minimum spanning tree from C ")
    print(" expected C: C-K K-X K-Q Q-J J-M ")

    print(" actually " + tree.minTree('C'), end = "\n\n")
    
if __name__ == '__main__':
    main()