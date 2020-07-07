def parent(i):
    return int(i/2)

def left(i):
    return 2 * i

def right(i):
    return left(i) + 1

def max(A,i,sz):
    l = left(i)
    r = right(i)
    largest = None
    if l <= sz and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= sz and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp 
        max(A,largest,sz)

def heapsort(A):
    size = len(A)
    middle = int(size/2)
    for i in xrange(middle,0,-1):
        max(A,i,size - 1)

    m = size - 1
    for i in xrange(m,-1,-1): 
        temp = A[0]
        A[0] = A[i]
        A[i] = temp 
        m = m-1 
        max(A,0,m)




A = [16,4,10,14,8,7,9,3,2,4,1]

print ("Unsorted: ", A)
heapsort(A)
print ("Heap Sorted: ", A)