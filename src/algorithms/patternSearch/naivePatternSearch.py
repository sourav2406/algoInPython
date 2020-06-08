#python3 programe for naive pattern search algorithm

def search(text, pat):
    N = len(text)
    M = len(pat)

    for i in range(N - M + 1):
        j = 0
        while j < M:
            if text[i + j] != pat[j]:
                break
            j += 1

        if j == M:
            print("Pattern found at index ", i)

#Driver code
if __name__ == "__main__":
    text = "AAABCAAABCAAAABC"
    pat = "AAABC"

    search(text, pat)

        