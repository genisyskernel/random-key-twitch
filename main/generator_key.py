from random import randint, choice
import string

chars_upper = string.ascii_uppercase
chars_lower = string.ascii_lowercase
chars_letters = string.ascii_letters
chars_numbers = string.digits
key0 = "live"
key1 = randint(000000000, 999999999)
key_main = chars_letters + chars_numbers
key2 = "".join(choice(key_main) for _ in range(30))

#print(f"{chars_lower} | {chars_upper} | {chars_letters} | {chars_numbers}")
print(f"{key0}_{key1}_{key2}")

"""
live_237506076_QJ2c4bm59bwito3B5vM2wOUJFmm0uS
live_486865329_b18I1GSIyMHvwkeYKxhUMVUvlATYDr

live_123456789_abcdefghijklmnopqrsu0123456789
live_9[09]_30[aA09]
"""