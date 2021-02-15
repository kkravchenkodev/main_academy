def power_generator(num: int):
    def power_n(power: int):
        return num ** power

    return power_n


power_2 = power_generator(2)
power_3 = power_generator(3)
power_4 = power_generator(4)
power_5 = power_generator(5)
print('4^2 =', power_2(4))
print('4^3 =', power_3(4))
print('4^4 =', power_4(4))
print('4^5 =', power_5(4))
