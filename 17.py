x = 0

x += len('thousand')
x += len('hundred') * 900
x += len('and') * 891
x += len('ninety') * 100
x += len('eighty') * 100
x += len('seventy') * 100
x += len('sixty') * 100
x += len('fifty') * 100
x += len('forty') * 100
x += len('thirty') * 100
x += len('twenty') * 100
x += len('nineteen') * 10
x += len('eighteen') * 10
x += len('seventeen') * 10
x += len('sixteen') * 10
x += len('fifteen') * 10
x += len('fourteen') * 10
x += len('thirteen') * 10
x += len('twelve') * 10
x += len('eleven') * 10
x += len('ten') * 10
x += len('nine') * 90 + len('nine') * 100
x += len('eight') * 90 + len('eight') * 100
x += len('seven') * 90 + len('seven') * 100
x += len('six') * 90 + len('six') * 100
x += len('five') * 90 + len('five') * 100
x += len('four') * 90 + len('four') * 100
x += len('three') * 90 + len('three') * 100
x += len('two') * 90 + len('two') * 100
x += len('one') * 90 + len('one') * 100 + len('one')

print x