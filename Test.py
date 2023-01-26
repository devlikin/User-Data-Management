def call(a):
    a += input(":", )
    print(a)
    call(a)


a = ""
call(a)
