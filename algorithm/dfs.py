# Deep-first search is traversing or searching tree or graph data structures, including graph-like solution space.
# it starts at the root node and explores as far as possible along each branch before backtracking.
#
# Time:  O(V+E)
# Space: O(V)


# recursion version
def dfs_recursively(node, visited: set):
    visited.add(node)
    '''
    process current node logic here
    '''
    for next_node in node.get_successors():
        if next_node not in visited:
            dfs_recursively(next_node, visited)


# iteration version, uncommon
def dfs_iteratively(root):
    stack, visited = [root], set()
    while stack:
        node = stack.pop()
        visited.add(node)
        '''
        process current node logic here
        '''
        for next_node in node.get_successors():
            if next_node not in visited:
                stack.append(next_node)
