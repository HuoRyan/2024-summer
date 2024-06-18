def sum1(N):
    sum_of_num = 0
    for i in range(1,N):
        if N % i == 0:
            sum_of_num += i
    return sum_of_num

def check(N):
    sum_final = sum1(N)
    if sum_final == N:
        print(sum_final)

def main():
    for i in range(1, 10001):
        check(i)

main()