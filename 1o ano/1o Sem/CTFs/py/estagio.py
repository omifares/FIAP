import os
def generate_secret_agent():

    with open("wordlist.txt", "r") as file:
        words = file.readlines()

    words = [word.strip() for word in words]

    indices = [0, 2, 10, 2, 3, 14, 19]
    letters = [words[i][0] if id % 2 == 0 else words[i][-1] for id, i in enumerate(indices)]

    secret_agent = "".join(letters)
    
    return secret_agent

secret_agent = generate_secret_agent()
curl_command = f"curl -A \"{secret_agent}\" http://161.35.250.58/secreto"

os.system(curl_command)
