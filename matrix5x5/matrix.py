A = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

B = [
    [26,27,28,29,30],
    [31,32,33,34,35],
    [36,37,38,39,40],
    [41,42,43,44,45],
    [46,47,48,49,50]
]

result = []

for i in range(5):
    line = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        line.append(total)
    result.append(line)

print("Hasil perkalian matriks: ")
for row in result:
    print(row)
