"""spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)"""

"""def add_three_or_eight(num):
    if num < 10:
        result = num + 3
    else:
        result = num + 8
    return result
    
print(add_three_or_eight(8))"""


# TODO: Edit the function to return the correct bill for different
# values of num_gallons
"""def get_water_bill(num_gallons):
    if num_gallons > 1:
        bill = 5 * (num_gallons / 1000)
    if num_gallons <= 8000:
        bill = 5 * (num_gallons / 1000)
    elif num_gallons <=22000:
        bill = 6 * (num_gallons / 1000)
    elif num_gallons <= 30000:
        bill = 7 * (num_gallons / 1000)
    elif num_gallons > 30000:
        bill = 10 * (num_gallons / 1000)
    return bill

print(get_water_bill(20000))"""

# Phone bill calculation

def get_phone_bill(gb):
    over_quota = (gb - 15.)
    over_quota = over_quota * 100
    if gb <= 15.:
        bill = 100
    elif gb:    
        bill = 100 + over_quota

    return bill
print(get_phone_bill(16.8))