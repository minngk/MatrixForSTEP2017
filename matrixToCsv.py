import numpy, sys, time, csv

if (len(sys.argv) != 2):
    print "usage: python %s N" % sys.argv[0]
    quit()

f = open('output.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
cnt = int(sys.argv[1])
csvlist = []
for n in xrange(1,cnt+1):
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C
    # Initialize the matrices to some values.
    for i in xrange(n):
        for j in xrange(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                c[j, k] += a[j, i] * b[i, k]


    end = time.time()
    csvlist.append("%.6f" % (end - begin))

writer.writerow(csvlist)
f.close();
