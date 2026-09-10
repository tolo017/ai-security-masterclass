with open("prompts.txt", "r") as file:

    for line in file:
        prompt = line.strip()
        print(prompt)
