count = 0

with open("prompts.txt", "r") as file:
    
    for line in file:
        count += 1
        
        prompt = line.strip()
        
        if prompt == "":
            continue
            
print(f"Total lines: {count}")
