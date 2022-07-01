# # Class


# class Employee:
#     '''Employee Class'''

#     def __init__(self, eno, ename, esal) -> None:
#         '''Constructor'''
#         self.emp_id = eno
#         self.emp_name = ename
#         self.emp_sal = esal
#     # Instance Method

#     def info(self):
#         '''returns the Employee details'''
#         print("*" * 20)
#         print("Employee Id:", self.emp_id)
#         print("Employee Name: ", self.emp_name)
#         print("Employee Salary: ", self.emp_sal)
#         print("*" * 20)

# # Object


# e1 = Employee(1001, "John", 25000)
# e2 = Employee(1002, "Jake", 54009)
# e3 = Employee(1003, "Sara", 45000)

# # Calling the Class-methods

# e1.info()
# print()
# e2.info()
# print()
# e3.info()

# class self_Test:
#     '''verifying id is same for self(default_Variable) and 
#     object_Variable(reference variable)
#     '''
#     def __init__(self) -> None:
#         print(id(self))

# s = self_Test()
# s2 = self_Test()
# print(id(s))
# print(id(s2))

# # read()
# with open("abc.txt",'r') as f:
#     f.read()
#     print(f.closed())
# print("Is File Closed?", f.closed())

# # read(n)
# with open("abc.txt", 'r') as f:
#     f.read(3)
#     print(f.closed())
# print("Is File Closed?", f.closed())

# # readline()
# with open('abc.txt', 'r') as f:
#     f.readline()
#     print(f.closed())
# print("Is File Closed?", f.closed())

# # readlines()
# with open('abc.txt', 'r') as f:
#     f.readlines()
#     print(f.closed())
# print("Is File Closed?", f.closed())

# # write()
# with open('abc.txt', 'w') as f1:
#     f1.write("John\n")
#     f1.write("24\n")
#     f1.write("M\n")
#     print("Written Successfully")
# print("Is File Closed?", f1.closed())

# # writelines()
# with open('abc.txt', 'w') as f2:
#     l1 = ["John Doe\n", "24\n", "M\n", "35000\n"]
#     f2.writelines(l1)
#     print("written success")
#     print()
#     print("Details")
#     for x in f2:
#         print(x)
# print("Is File Closed?", f2.closed())
