#iteration
string = "Francis"
it = iter(string)
#next(it)
#print(next(it))
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)


