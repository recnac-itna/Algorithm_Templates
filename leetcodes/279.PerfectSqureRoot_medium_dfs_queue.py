from collections import deque 
# [279] https://leetcode.com/problems/perfect-squares/
# given a positive integer n, find the least number of perfect square numbers
#convert to a grahp
#the shortest path from n to 0.
class Solution1:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = -1
        queue = deque([n])
        visited = {n}

        while queue:
            step += 1
            size = len(queue)  

            for _ in range(size):
                cur_node = queue.popleft()
                if cur_node == 0: 
                    return step  #terminating checking 

                #strech to collect next nodes
                i = 1
                while True:
                    next_node = cur_node - i**2
                    if next_node < 0: #next_node >=0 
                        break 
                    if next_node not in visited:
                        queue.append(next_node)
                        visited.add(next_node)
                    i += 1 
        #No failure case, because  1+1+..add up to any number.


#DFS from 0 to n 
class Solution2:
    def numSquares(self, n: int) -> int:
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        queue = deque([(0, 0)])
        visited = set()

        while queue:
            cur_value, step = queue.popleft()
            step += 1
            for num in nums:
                new_value = cur_value + num
                if new_value == n:
                    return step
                elif new_value > n:
                    break
                else:
                    if new_value not in visited:
                        visited.add(new_value)
                        queue.append((new_value, step))

# bidirectional BFS, faster than one-directional BFS
class Solution3:
    def numSquares2(self, n):
        front, back, pm = [0], [n], 1  # pm is "plus minus"
        depth = [0] + [None] * (n - 1) + [-1]  # depth[0] == 0, depth[n] == -1, depth[everythingElse] == None
        while front:
            newFront = []
            for v in front:
                i = 1
                while True:
                    w = v + pm * i * i  # generate a neighbor
                    if w < 0 or w > n:  # all neighbors have been generated
                        break
                    if depth[w] is None:  # w has not been discovered
                        depth[w] = depth[v] + pm  # mark it as discovered by assigning a depth to it
                        newFront.append(w)
                    elif (depth[w] < 0) != (depth[v] < 0):  # w has been discovered in the `back` tree, so we're done
                        return abs(depth[w] - depth[v])
                    i += 1
            front = newFront
            if len(front) > len(back):
                front, back, pm = back, front, -pm  # always expand the tree with fewer leaves
