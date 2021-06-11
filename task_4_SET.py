rand_set = [123, 'fjal', 3.14, [1, 2, 3], (3, 2, 1), {"first_name": "Humphrey",
  "last_name": "Wilcox"}, True]
def revprint_set_rec(st, i=0):
    if len(st) != i:
        print(f"{st[len(st) - 1 - i]} ", end = '')
        revprint_set_rec(st, i+1)
    else:
        print()

print(rand_set)
revprint_set_rec(rand_set)

