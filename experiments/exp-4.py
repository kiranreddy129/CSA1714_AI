from itertools import permutations

words = input("Enter words separated by +: ").split("+")
result = input("Enter result word: ")

letters = set("".join(words) + result)
letters = list(letters)

first = set(word[0] for word in words)
first.add(result[0])

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if any(d[x] == 0 for x in first):
        continue

    total = 0

    for word in words:
        number = 0
        for ch in word:
            number = number * 10 + d[ch]
        total += number

    result_number = 0
    for ch in result:
        result_number = result_number * 10 + d[ch]

    if total == result_number:
        print("\nSolution:")

        for ch in letters:
            print(ch, "=", d[ch])

        print()

        for word in words:
            number = 0
            for ch in word:
                number = number * 10 + d[ch]
            print(word, "=", number)

        print(result, "=", result_number)
        break
else:
    print("No solution")
