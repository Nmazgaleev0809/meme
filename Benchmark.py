def benchmark(iters):
    def actual_decorator(func):
        import time
        
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper
    return actual_decorator


@benchmark(iters=200)
def stock_list(listOfArt, listOfCat):
    ans = [int(i) for i in list(str(0)*len(listOfCat))]
    for i in listOfArt:
        i = i.split()
        if i[0][0] in listOfCat:
            ans[listOfCat.index(i[0][0])]+= int(i[1])
    ans_arr = []
    i = 0
    while i < len(listOfCat):
        ans_arr.append('('+listOfCat[i]+' : '+str(ans[i])+')')
        i+=1
    if len(listOfArt)==0 or len(listOfCat)==0:
        return ' '
    if ans.count(0)==len(ans):
        return ' '
    return ' - '.join(ans_arr)
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

stock_list(b, c)


