for a in range(1, 34):
    for b in range(a, 34):
        for c in range(b, 34):
            for d in range(c, 34):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and c != d and a != c and b != d and a != d and b != c:
                    print(a, b, c, d, a ** 3 + b ** 3)
