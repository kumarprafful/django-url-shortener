import random, string
from shortener.models import URLs

def get_short_id():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    i = 0
    while i <= 1000:
        # short_id = ''.join(random.choice(char) for x in range(length))
        short_id = 'C54Wc8'
        try:
            temp = URLs.objects.get(pk=short_id)
            i += 1
            print(i)
        except Exception as e:
            print(e)
            return short_id