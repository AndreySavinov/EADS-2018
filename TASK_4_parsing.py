file = open('input.txt')
data = file.read()
file.close()


data = data.split(sep='\n')


L = int(data[0])


words = data[1].split(sep=' ')
n = len(words)


arr = [len(words[i]) for i in range(n)]



Max_length = 1e10
def new_marg(a, n, L):
    line = [[0 for i in range(n + 1)] for i in range(n + 1)] 
    cost = [0 for i in range(n + 1)]
    num_str = [0 for i in range(n + 1)]
    for i in range(1, n + 1): 
        res = L - a[i - 1]
        line[i][i] = res*res
        for j in range(i + 1, n + 1): 
            res = res - a[j - 1] - 1
            if res<0:
                line[i][j] = Max_length
            else:
                line[i][j] = res*res 
    for j in range(1, n + 1): 
        cost[j] = Max_length 
        for i in range(1, j + 1): 
            if ((cost[i - 1] + line[i][j])<cost[j]): 
                cost[j] = cost[i-1] + line[i][j]
                num_str[j] = num_str[i-1]+1
    return num_str[-1], cost[-1]



x, y = new_marg(arr, len(words), L) 
print(y, x)





out = str(y)+'\n'+str(x)
output = open('output.txt', 'w')
output.write(str(out))
output.close()