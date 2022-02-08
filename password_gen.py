import random


def generate_password():
    chars = "~AaB1bCc2Dd!3@Ee4FfG5gHh6#$I7iJj8Kk%9LlMmNnOo&*PpQqRrS0sTtUuVv_WwXxYyZz"
    gen_pass = ""
    for i in range(0, 3):
        for j in range(0, 5):
            gen_pass += chars[random.randint(0, len(chars) - 1)]
        gen_pass += "-"
    gen_pass = gen_pass[0:17]
    return gen_pass


print(generate_password())