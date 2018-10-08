
def foo(s):
    return 10 / int(s) 
def bar(s):
    return foo(s)*2

def main(s):
    try:
        bar(s)
    except Exception as e:
        print('Error: ', e)
    finally:
        print('finally...')

main(0)
