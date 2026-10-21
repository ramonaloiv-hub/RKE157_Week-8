from fight import calculate_hit
from read_from_file import read_data


hero=read_data(r"data\heroes.txt")
villain=read_data(r"data\villains.txt")

hero_weapons=read_data(r"data\weapons.txt")
villain_weapons=read_data(r"data\weapons.txt")


hero_hit=calculate_hit(hero,hero_weapons)
villain_hit=calculate_hit(villain,villain_weapons)

print(f"{hero} uses {hero_weapons} and hits with power {hero_hit}.")
print(f"{villain} uses {villain_weapons} and hits with power {villain_hit}.")

if hero_hit>villain_hit:
    print(f"{hero} saves the day!")
elif villain_hit>hero_hit:
    print(f"{villain} and the Dark Side wins!")
else:
    print("It's a tie!")
