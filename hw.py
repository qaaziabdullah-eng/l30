#integer to roman number
class convert:
    def fun1(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        rom = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                rom += syb[i]
                num -= val[i]
            i += 1
        return rom
print(convert().fun1(80))