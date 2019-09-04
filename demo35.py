l1 = list("QWERTYUIOOUYTREWERUPIUYTWERTYUI")
print(l1)

counts = {}
print(type(counts))
for l in l1:
    counts.setdefault(l, 0)
    counts[l] = counts[l] + 1


for key, count in counts.items():
    print("[%s] count=%d" % (key, count))
for key, count in counts.items():
    print("[%s] count=%d" % (key, count))