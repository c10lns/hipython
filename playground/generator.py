# 生成式
a = [x * x for x in range(1, 10) if x % 2 == 0]
print(a)

b = [x if x % 2 == 0 else -x for x in range(1, 10)]
print(b)

c, d, e = True, False, False
print(not d and c or e)


# 打印扑克
puke = list(str(x) for x in range(2, 11))
puke.extend(('J', 'Q', 'K', 'A'))
puke = list(x + y for x in ['♠', '♥', '♣', '♦'] for y in puke)
puke.extend(('Joker', 'joker'))
print(puke)
