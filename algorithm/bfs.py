# Breadth-first search is traversing or searching tree or graph data structures, including graph-like solution space.
# it explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
#
# Time:  O(V+E)     V: vertex, E: edges
# Space: O(V)
from collections import deque


# iteration version, using deque
def bfs_iteratively_by_queue(self, start, target=None):
    queue, visited = deque([start]), {start}

    while queue:
        node = queue.popleft()
        visited.add(node) #add [root] twice
        '''
        process current node logic here
        '''
        self.process_logic(node)

        # target is optional
        if node == target:
            '''
            reach the goal and break out
            '''
            self.process_target_logic(target)
            break
        for next_node in node.get_successors():
            if next_node not in visited:
                queue.append(next_node)

# alternative iteration version from leetcode, use deque
# [Explore - LeetCode](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1372/)

def bfs_iteratively_by_queue_2(self, start, target=None):
    #step as a log to monitor and record the process.
    step = -1
    queue, visited = deque([start]), {start}


    while queue:
        #Use step as an explicit reminder.
        step += 1
        size = len(queue)

        for _ in range(size):
            #get the current node and remove it from queue
            cur_node = queue.popleft()         
            # target is optional
            if cur_node == target:
                '''
                reach the goal and terminate
                '''
                self.process_target_logic(target)
                return 
        #strech to collect cur_node's successors
        for next_node in cur_node.get_successors():
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)

    return -1 #Failure 


# iteration version, using list, pythonic-style
# conciser but more memory, mainly used when you want to collect the whole list
def bfs_iteratively_by_list(self, start, target=None):
    node_list, visited = [start], {start}

    # append while traversing
    for node in node_list:
        visited.add(node)
        '''
        process current node logic here
        '''
        self.process_logic(node)

        # target is optional
        if node == target:
            '''
            reach the goal and break out
            '''
            self.process_target_logic(target)
            break
        for next_node in node.get_successors():
            if next_node not in visited:
                node_list += node

    # basically the node_list is useful here
    return node_list


# recursion version, uncommon
def bfs_recursively(self, queue: deque, visited: set, target=None):
    if not queue:
        return

    node = queue.popleft()
    visited.add(node)
    '''
    process current node logic here
    '''
    self.process_logic(node)

    # target is optional
    if node == target:
        '''
        reach the goal and break out
        '''
        self.process_target_logic(target)
        return
    for next_node in node.get_successors():
        if next_node not in visited:
            queue.append(next_node)
    self.bfs_recursively(queue, visited)
