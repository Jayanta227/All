import prob
num_test=100
def test(a_style=1,s=0):
    if a_style==1:
        for x in range(num_test):
            q=prob.q_making()
            a=prob.a_making1()
            count=0
            for y in q:
                if q[y]==a[y]:
                    count+=1
            s=s+count
        return s/num_test




    if a_style==2:
        for x in range(num_test):
            q=prob.q_making()
            a=prob.a_making2()
            count=0
            for y in q:
                if q[y]==a[y]:
                    count+=1
            s=s+count
        return s/num_test



    if a_style==3:
        for x in range(num_test):
            q=prob.q_making()
            a=prob.a_making3()
            count=0
            for y in q:
                if q[y]==a[y]:
                    count+=1
            s=s+count
        return s/num_test


print(test(1))
print(test(2))
print(test(3))
