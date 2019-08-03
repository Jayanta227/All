#making febonacci series with generators
def feb():
    a=0;b=1;c=25
    while True:
        yield a;
        a,b=b,a+b
for f in feb():
    print(f)
    if f>1000:
        break