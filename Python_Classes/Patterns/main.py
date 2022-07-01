# pattern - 1
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print("* " * n)


# Pattern - 2
'''
1  1  1  1  1  
2  2  2  2  2  
3  3  3  3  3  
4  4  4  4  4  
5  5  5  5  5
'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, " ", end="")
    print()


# pattern - 3
'''
1  2  3  4  5  
1  2  3  4  5  
1  2  3  4  5  
1  2  3  4  5  
1  2  3  4  5
'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, " ", end="")
    print()


# pattern - 4
'''
A  A  A  A  A  
B  B  B  B  B  
C  C  C  C  C  
D  D  D  D  D  
E  E  E  E  E 
'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(chr(64 + i), " ", end="")  # char(64) = 'A'
    print()

# pattern - 5

'''
A  B  C  D  E  
A  B  C  D  E  
A  B  C  D  E  
A  B  C  D  E  
A  B  C  D  E
'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(chr(64 + j), " ", end="")
    print()


# pattern - 6
'''
5  5  5  5  5  
4  4  4  4  4  
3  3  3  3  3  
2  2  2  2  2  
1  1  1  1  1
'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print((n + 1 - i), " ", end="")
    print()
