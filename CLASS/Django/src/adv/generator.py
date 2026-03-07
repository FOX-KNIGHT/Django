def square_iter(n):
    if str(n).isdigit():
        res=n**0.5
        if str(res).isdigit():
            yield True
    else:
        yield False


print([next(square_iter(9))])