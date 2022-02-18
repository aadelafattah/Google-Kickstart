def h_index(n, citations):
    ans = []
    max = 1
    for i in range(n):
        ans.append()(citations[i])
    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        citations = map(int, input().split()) # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
