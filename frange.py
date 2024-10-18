# Written by siembra1978
def frangef(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step