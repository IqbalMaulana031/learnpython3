from datetime import datetime
import random

def get_pemenang(participant):
    return random.choices(participant)[0]

now = datetime.now()

print(now.year, now.month, now.day)

participant = ['nanda', 'budi', 'yoga', 'ali']

print("pemenang undian adalah {}".format(get_pemenang(participant)))