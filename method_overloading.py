def conc(dtype, *args):
    
    if dtype == 'int':
        answer = 0
 
    if dtype == 'str':
        answer = ''

    for x in args:
        answer = answer + x
 
    print(answer)
 
conc('int', 5, 6)
conc('str', 'Hello ', 'world')
