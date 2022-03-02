'''
    VARS:
        STRING
        INT
        FLOAT
        BOOL
        -- LIST
        -- TUPLE
        -- DICT
        -- SET
'''

from cmath import pi


name = "Jon Doe"
age = 20
heigth = 1.80
ishuman = True

print("IMPRIMINDO AS VARIAVEIS")
print(name)
print(age)
print(heigth)
print(ishuman)

print("IMPRIMINDO OS TIPOS DAS VARIAVEIS")
print(type(name))
print(type(age))
print(type(heigth))
print(type(ishuman))

print("IMPRIMINDO TEXTO CONCATENADOS COM VARIAVEIS")
# print("Função STR() sever para converter números para texto")
print("Meu nome é " + name + ", tenho " + str(age) + " anos e " + str(heigth) + " de altura.")
print("Meu nome é", name, ", tenho", age, "anos e", heigth, "de altura.")
print(f"Meu nome é {name}, tenho {age} anos e {heigth} de altura.")

# MULTIPLE VARIABLES
name, age, heigth, ishuman = "Leo Lemos", "30", "1.83", True
print("MULTIPLE VARIABLES")
print("Meu nome é " + name + ", tenho " + str(age) + " anos e " + str(heigth) + " de altura.")
print("Meu nome é", name, ", tenho", age, "anos e", heigth, "de altura.")
print(f"Meu nome é {name}, tenho {age} anos e {heigth} de altura.")

# MULTIPLE ASSINGMENT
leo = pedro = maria = 30
print(leo, pedro, maria)

# LENGTH
# UPPERCASE
# LOWERCASE
# TITLECASE
# START WITH
# END WITH
# CONTAINS
# REPLACE
# FIND