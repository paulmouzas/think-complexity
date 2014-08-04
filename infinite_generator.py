import string
def infinite_generator():
    count = 0
    while True:
        count += 1
        for c in string.lowercase:
            yield c + str(count)
            
