o = list(map(int, input().split()))
n = list(o)
n[o.index(min(o))] = max(o)
n[o.index(max(o))] = min(o)

print(' '.join(map(str,n)))
