def extract_title(markdown):    
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("#"):
            if line[1:2] == " ":
                return  line[1:].strip()
            
    raise Exception("No title found")