def opening_list(iterable: list):
    for i in iterable:
        if not isinstance(i, list):
            yield i
        else:
            yield from opening_list(i)
