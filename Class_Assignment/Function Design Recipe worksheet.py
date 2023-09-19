# This function takes in a word (string) and a value (integer).
# It returns the word repeated 'value' times as a string.
def KaKaRp(word: str, value: int) -> str:
    return word * value

# This function calculates the number of cents from a floating-point 'change' value.
# It rounds the 'change' to the nearest dollar and calculates the remaining cents.
# The result is returned as an integer.
def number_of_cents(change: float) -> int:
    # Round the dollar part of the change to the nearest integer.
    dollars = round(change)
    # Calculate the cents by subtracting the dollars and converting the fraction to cents (multiply by 100).
    cents = (change - dollars) * 100
    return int(cents)

# This function calculates the tax amount based on a given 'bill' and 'rate'.
# It returns the calculated tax as a float.
def calculate_tax(bill: float, rate: float) -> float:
    return bill * rate

# Example usage of the functions:

# Print the result of KaKaRp function, which repeats the word "Marcia" 3 times.
print(KaKaRp("Marcia ", 3))

# Print the result of number_of_cents function, which calculates the cents from 1.25 dollars.
print(number_of_cents(1.25))

# Print the result of calculate_tax function, which calculates the tax on a $100 bill at a 13% rate.
print(calculate_tax(100, 0.13))
