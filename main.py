# 4
soz =  ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

a = sorted(soz, key=len, reverse=True)

print("1-eng uzun soz:",  a[0])
print("2- eng uzun soz:", a[1])


# 5
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

birinchi = ""
ikinchi = ""

for soz in words:
    if len(soz) > len(birinchi):
        ikinchi = birinchi
        birinchi = soz
    elif len(soz) > len(ikinchi):
        ikinchi = soz

print("1-chi eng uzun soz:", birinchi)
print("2-chi eng uzun soz:", ikinchi)

# 6
ism = input("Ismni kiriting: ")

if len(ism) <= 2:
    natija = ism
else:
    natija = ism[0] + "X" * (len(ism) - 2) + ism[-1]

print(natija)

# 7
a = ("a", "b", "c", "d")

natija = tuple((i, el) for i, el in enumerate(a))

print(natija)

8
a = ("apple", "banana", "ok")

natija = tuple(s[::-1] for s in a)

print(natija)
