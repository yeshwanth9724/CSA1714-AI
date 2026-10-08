from itertools import permutations
words = ["SEND", "MORE", "MONEY"]
letters = set("SENDMORY")
for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))
    if d["S"] == 0 or d["M"] == 0:
        continue
    def num(word):
        return int("".join(str(d[x]) for x in word))
    if num("SEND") + num("MORE") == num("MONEY"):
        print("Solution:", d)
        print(num("SEND"), "+", num("MORE"), "=", num("MONEY"))
        break
