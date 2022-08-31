def verify(matrix):
    for i in range(len(matrix)-1):
        sm = list(map(sum, zip(matrix[i], matrix[i+1])))
        for j in range(1, len(sm)):
            if sm[j] == 2 or sm[j] == sm[j-1] == 1:
                return False
    else:
        return True


m = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

print(verify(m))
