class RomanNumerals:
    def roman(self, n):

        rom = ""
        num = n % 10
        num10 = int((n % 100)/10)
        num100 = int(n%1000/100)
        num1000 =  int(n%10000/1000)

        #tysiące
        if num1000 == 1:
            rom += "M"
        elif num1000 == 2:
            rom += "MM"
        elif num1000 == 3:
            rom += "MMM"

        #setki
        if num100 == 1:
            rom += "C"
        elif num100 == 2:
            rom += "CC"
        elif num100 == 3:
            rom += "CCC"
        elif num100 == 4:
            rom += "CD"
        elif num100 == 5:
            rom += "D"
        elif num100 == 6:
            rom += "DC"
        elif num100 == 7:
            rom += "DCC"
        elif num100 == 8:
            rom += "DCCC"
        elif num100 == 9:
            rom += "CM"

        #dziesiątki
        if num10 == 1:
            rom += "X"
        elif num10 == 2:
            rom += "XX"
        elif num10 == 3:
            rom += "XXX"
        elif num10 == 4:
            rom += "XL"
        elif num10 == 5:
            rom += "L"
        elif num10 == 6:
            rom += "LX"
        elif num10 == 7:
            rom += "LXX"
        elif num10 == 8:
            rom += "LXXX"
        elif num10 == 9:
            rom += "XC"

        #jedności
        if num == 1:
            rom += "I"
        elif num == 2:
            rom += "II"
        elif num == 3:
            rom += "III"
        elif num == 4:
            rom += "IV"
        elif num == 5:
            rom += "V"
        elif num == 6:
            rom += "VI"
        elif num == 7:
            rom += "VII"
        elif num == 8:
            rom += "VIII"
        elif num == 9:
            rom += "IX"


        return rom