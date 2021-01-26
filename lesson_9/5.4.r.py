import math
from json import load


def days_in_year(planet):
    with open('planet_data', 'r') as data:
        planet_data = load(data)
    orbital_radius = planet_data['orbital_radius'][planet] * 1000000
    orbital_speed = planet_data['orbital_speed'][planet]
    planet_year = 2 * math.pi * orbital_radius / orbital_speed / (60 * 60 * 24)
    print(f"The {int(planet_year)} days in a year on {planet}")
    return int(planet_year)


def the_bigger_year():
    planet1 = input("Planet 1: ")
    planet2 = input("Planet 2: ")
    planet_days1 = days_in_year(planet1)
    planet_days2 = days_in_year(planet2)
    the_biggest_year = planet1 if planet_days1 > planet_days2 else planet2
    return f"The {the_biggest_year} year is bigger"


if __name__ == '__main__':
    print(the_bigger_year())
