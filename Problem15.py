# Lattice paths


grid_size = [20,20]

def count_paths(gridsize):

    if gridsize == [0,0]: return 1

    paths = 0

    if gridsize[0] > 0:
        paths += count_paths([gridsize[0]-1,gridsize[1]])

    if gridsize[1] > 0:
        paths += count_paths([gridsize[0],gridsize[1]-1])

    return paths


print(count_paths([4,4]))




def countRoutes(m,n):
    if n==0  or m==0:
        return 1
    else:
        return countRoutes(m, n - 1) + countRoutes(m - 1, n)

print(countRoutes(2,2))


cache = dict()

def countRoutes_memo(m,n,cache):


    if n == 0 or m == 0:
        return 1
    if (m,n) in cache:
        return cache[(m,n)]
    else:
        cache[(m, n)] = countRoutes_memo(m, n - 1, cache) +\
                        countRoutes_memo(m - 1, n, cache)
        return cache[(m,n)]

print(countRoutes_memo(20,20,cache))










