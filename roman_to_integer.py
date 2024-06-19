class RomanToInteger:
    def __init__(self):
        #  sınıfın başlangıç durumunu ayarlar
        self.roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        self.invalid_combinations = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD"]

    def is_valid_roman(self, roman_numeral):
        valid_chars = set(self.roman_numeral.keys())  # geçerli roma rakamlarını tutar liste gibi ama daha hızlı
        for char in roman_numeral:
            if char not in valid_chars:
                return False
            break

        for invalid_comb in self.invalid_combinations:  # listedeki her ögeyi teker teker alir.
            if invalid_comb in roman_numeral:
                return False
        return True

    def roman_to_integer(self, user_input=None):
        user_input = user_input.upper()

        if not self.is_valid_roman(user_input):  # kullanıcın geçersiz girdiği rakamı kontrol eder
            return None

        total = 0
        last_value = 0
        for i in reversed(user_input):  # girilen roma rakamini ters cevirdi
            value = self.roman_numeral[i]
            if value < last_value:  # mevcut değer önceki değerden küçükse çıkar
                total -= value
            else:
                total += value
            last_value = value
        return total
