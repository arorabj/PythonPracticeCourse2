
def fibonacciSeries(n):
    """

    :param n:
    :return: nth Fibonacci numbers
    """
    if 0<=n<=1 :
        return n

    n_minus1, n_minus2 =  1, 0
    result = None

    for f in range (n-1):
        result = n_minus2+n_minus1
        n_minus2=n_minus1
        n_minus1=result
    return result

for i in range(36):
    print(i, fibonacciSeries(i))


li =["a","cb",'abc bs',"abc","adjf dk", "dsa dsd ddd"]
for item in li :
    if len(item) >> 2:
        print(item)

a=(2,3,4)

a=a[2]
print (a)