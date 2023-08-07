def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


num = int(input())
inp_data = []

for i in range(num):
    inp_data.append(int(input()))

    a = inp_data[0]

for j in range(1, len(inp_data)):
    z = gcd(a, inp_data[j])
    a = z

print(a)
