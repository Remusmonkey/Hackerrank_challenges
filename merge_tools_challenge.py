def merge_the_tools(string, k):
    n = len(string)
    assert 1 <= n <= 10 ** 4, "The length of the string must be between 1 and 10^4."
    assert 1 <= k <= n, "k must be between 1 and the length of the string."
    assert n % k == 0, "The length of the string must be a multiple of k."
    step = k  # Since k is the size of each substring
    for i in range(0, n, step):
        substring = string[i:i + step]

        # Use an ordered set-like approach to remove duplicates efficiently
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)

        # Join the result list and print the unique substring
        print(''.join(result))