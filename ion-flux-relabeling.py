h = 3
q = [7, 3, 5, 1]

def binarySearch(height_squared, converter):
    tree_nodes = []
    for i in range(1, height_squared):
        tree_nodes.append(i)
        
    root = tree_nodes[-1]
    if root <= converter:
        print(-1)
        return -1
    
    while len(tree_nodes) > 2:
        
        if converter == tree_nodes[-1]:
            print(f"nodes left: {tree_nodes}, converter: {converter}, root: {root}")
            return root
        
        root = tree_nodes[-1]
        partition = round((len(tree_nodes)-1)*0.5)
        
        print(f"particion: {tree_nodes[partition]}")
        
        if tree_nodes[partition] > converter:
            tree_nodes = tree_nodes[0:partition]
            print(f"nodes left: {tree_nodes}, converter: {converter}, root: {root}")
        else:
            tree_nodes = tree_nodes[partition:len(tree_nodes)-1]
            print(f"nodes left: {tree_nodes}, converter: {converter}, root: {root}")
    return root



def solution(h, q):
    p = []
    height_squared = 2**h
    for converter in q:
        p.append(binarySearch(height_squared, converter))
    return p

print(solution(h, q))