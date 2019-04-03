# refer to https://time.geekbang.org/course/detail/130-42710


MAX_LEVEL = 10


# param such as current path, result, visited set
def recursion(level, *params):
    # recursion terminator
    if level > MAX_LEVEL:
        '''
        terminator logic here
        '''
        return

    '''
    process logic in current level, such as update state (params)
    '''

    # drill down
    recursion(level + 1, params)

    '''
    reverse the current level status if needed, such as revert the params (opposite operation of upper code block) 
    '''


# interval merge
# definition: interval = [start, end]
def add_interval(new_interval, intervals):
    if intervals and intervals[-1][1] >= new_interval[0]:
        if intervals[-1][1] < new_interval[1]:
            intervals[-1][1] = new_interval[1]
    else:
        intervals.append(new_interval)


