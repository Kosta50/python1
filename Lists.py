# l=[1,2,"hi"]
# print(l)
# print(l[0])
# l[0]=50
# print(l)
# l.append(100)
# print(l)
# l.append(60)
# print(len(l))
# l.remove('hi')
# print(l)
# if('hi' in l):
#     print("\"Hi\" is in the list")
# else:
#     print("\"Hi\" is not in the list")
l=[50,120,100,60,70]
biggest=l[0]
for n in range(len(l)):
    if(biggest<l[n]):
        biggest=l[n]
print(biggest)
# for n in range(len(l)):
#     # print(n)
#     print(l[n])
s="banana"
# print(s[0])
for n in range(len(s)):
    print(s[n])

