def foo(n,a,b,c):
    for i in range(1,n+1):
        line = ""
        if i % a==0:
            line+="foo"
        if i % b==0:
            line+="bar"
        if i % c==0:
            line+="baz"
        if line!="":
            print(line)

foo(15, 2, 3, 5)
        