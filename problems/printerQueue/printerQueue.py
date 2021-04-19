def solution(N, M, docs):
    pass


if __name__ == "__main__":
    test_num = int(input())
    for _ in range(test_num):
        N, M = map(int, input().split(" "))
        docs = list(map(int, input().split(" ")))
        solution(N, M, docs)
