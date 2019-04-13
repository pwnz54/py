o = list(map(int, input().split()))
n = list(o)
n[o.index(min(o))] = max(o)
n[o.index(max(o))] = min(o)

print(' '.join(map(str,n)))

#####################################
a = [int(s) for s in input().split()]

# обратите внимание на множественное присваивание:
# справа от "=" стоит список из двух элементов,
# а слева -- две переменные,
# поэтому так делать можно
k, C = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))
##############################################
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
#################################################
