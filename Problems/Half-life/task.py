half_life = 0
number_atoms = int(input())
resulting_quantity = int(input())
while number_atoms > resulting_quantity:
    half_life += 12
    number_atoms /= 2
print(half_life)
