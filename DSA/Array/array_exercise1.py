from tarfile import _Bz2ReadableFileobj


exp = [2200,2350,2600,2130,2190]
print(exp[1]-exp[0])
print(exp[0]+exp[1]+exp[2])
for i in range(len(exp)):
    if exp[i] == 2000:
        print(True)
        break
    else:
        rprint(False)
exp.append(1980)
print(exp)
exp[3] = exp[3] - 200
