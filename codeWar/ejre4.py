def sum_array(arr):
    if not arr or len(arr) <=2:
        return 0
    return sum(sorted(arr)[1:-1])

#print(sum_array(None))

def combine_names(firstname, lastname):
    return f"{firstname} {lastname}"

#print(combine_names('Paco', 'Salsa'))

def to_binary(n):
    return int(bin(n)[2:])

#print(to_binary(5))

def print_array(arr):
    return ','.join(map(str, arr))

array1 = ["hello", "this", "is", "an", "array!"]
array2 = ["a", "b", "c", "d", "e!"]
data = array1+array2
print(print_array([4]))