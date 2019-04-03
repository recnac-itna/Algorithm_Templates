# two pointers scenario, famous application such as binary search, quick sort and sliding window.

'''
Classification:
1. old & new state: old, new = new, cur_result
2. slow & fast pointer: slow-> fast->->
3. left & right boundary or index: left-> <-right
4. p1 & p2 from two sequences: p1-> p2->
5. start & end sliding window boundary: start-> end->
'''


# old & new state: old, new = new, cur_result
def old_new_state(self, seq):
    # initialize state
    old, new = None, None
    for element in seq:
        '''
        process current element with help of old state
        '''
        cur_result = self.process(element, old)
        old, new = new, cur_result


# slow & fast pointer: slow-> fast->->
def slow_fast_pointer(self, seq):
    # initialize slow pointer
    slow = seq[0]   # or slow = 0
    # fast-runner grows each iteration
    for fast in range(seq):     # or range(len(seq))
        '''
        slow-runner grows with some restrict
        '''
        if self.slow_checker(slow):
            slow = slow.next    # or slow += 1


# left & right boundary or index: left-> <-right
def left_right_index(self, seq):
    left, right = 0, len(seq) - 1
    while left < right:
        '''
        left index moves when satisfy the condition
        '''
        if self.left_condition(left):
            left += 1

        '''
        right index move when satisfy the condition
        '''
        if self.right_condition(right):
            right -= 1

        '''
        process logic before or after pointers movement
        '''
        self.process_logic()


# p1 & p2 from two sequences: p1-> p2->
def pointers_from_two_seq(self, seq1, seq2):
    # init pointers
    p1, p2 = 0, 0       # or seq1[0], seq2[0]

    # or other condition
    while p1 < len(seq1) and p2 < len(seq2):
        '''
        p1 index moves when satisfy the condition
        '''
        if self.p1_condition(p1):
            p1 += 1

        '''
        p2 index move when satisfy the condition
        '''
        if self.p2_condition(p2):
            p2 += 1

        '''
        process logic before or after pointers movement
        '''
        self.process_logic()


# start & end sliding window boundary: start-> end->
# more details templates in sliding windows, here is just about two-pointers part
def start_end_sliding_window(self, seq):
    start, end = 0, 0

    while end < len(seq):
        end += 1

        '''
        start grows with some restrict
        '''
        if self.start_checker(start):
            start += 1


