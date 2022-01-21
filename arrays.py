import os


def hourglassSum(arr):
    coluna_final = len(arr) - 2
    linha_final = len(arr[0]) - 2
    maior_soma = 0
    for linha in range(linha_final):
        for col in range(coluna_final):
            somaX = arr[linha][col] + arr[linha][col + 1] + arr[linha][col + 2]
            somaX = somaX + arr[linha + 1][col + 1]
            somaX = somaX + arr[linha + 2][col] + arr[linha + 2][col + 1] + arr[linha + 2][col + 2]
            if somaX > maior_soma:
                maior_soma = somaX

            return maior_soma


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

