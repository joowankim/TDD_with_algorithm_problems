class PrinterQueue:
    def __init__(self, q):
        self.q = q
        self.priorities = sorted(q, reverse=True)

    def get(self, target):
        idx = 0
        cnt = 0
        while True:
            if idx == target:
                if self.__is_popable(idx):
                    return cnt + 1
                else:
                    self.q.append(self.q[idx])
                    target = len(self.q) - 1
            if not self.__is_popable(idx):
                self.q.append(self.q[idx])
            else:
                cnt += 1
            idx += 1

    def __is_popable(self, index):
        if self.q[index] == self.priorities[0]:
            del self.priorities[0]
            return True
        return False


def solution(N, M, docs):
    pq = PrinterQueue(docs)
    return pq.get(M)


if __name__ == "__main__":
    test_num = int(input())
    for _ in range(test_num):
        N, M = map(int, input().split(" "))
        docs = list(map(int, input().split(" ")))
        print(solution(N, M, docs))
