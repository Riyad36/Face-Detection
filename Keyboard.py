listA = ['q','w','e','r','t','y','u','i','o','p']
listB = ['a','s','d','f','g','h','j','k','l',';']
listC = ['z','x','c','v','b','n','m',',','.','/']

pos = input()
value = input()

if pos == 'L':
    for i in range(0,len(value)):
        for j in range(0,9):

            if value[i] == listA[j]:
                value.replace(value[i], listA[j + 1])
            elif value[i] == listB[j]:
                value.replace(value[i], listB[j + 1])
            elif value[i] == listC[j]:
                value.replace(value[i], listC[j + 1])

elif pos == 'R':
    for i in range(0, len(value)):
        for j in range(0, 9):

            if value[i] == listA[j]:
                value.replace(value[i],listA[j+1])
            elif value[i] == listB[j]:
                value.replace(value[i],listB[j+1])
            elif value[i] == listC[j]:
                value.replace(value[i],listC[j+1])

print(value)
