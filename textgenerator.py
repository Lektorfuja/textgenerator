import random
import string

def generate_random_string():
    letters = string.ascii_lowercase  # 26 letters of the English alphabet
    random_string = ''.join(random.choices(letters, k=100))
    return random_string

if __name__ == "__main__":
    result = generate_random_string()
    print(result)
