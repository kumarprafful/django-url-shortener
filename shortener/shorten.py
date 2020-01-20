import random, string

def get_short_id():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = URLs.objects.get(pk=short_id)
        except:
            return short_id