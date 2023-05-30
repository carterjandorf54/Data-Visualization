# Returns an input list list[0] and the squares list list[1]
def squares(start, finish):
    squares = [x ** 2 for x in range(start, finish)]
    inputs = [x for x in range(start, finish)]

    lists = [inputs, squares]

    # Return the input list and the squares list
    return lists