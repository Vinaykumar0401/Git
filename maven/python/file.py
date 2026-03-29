with open(r"C:\Users\DELL\Downloads\demo.txt", "r") as fobj:
    counter = 0
    for line in fobj:
        line = line.strip()
        for ch in line:
            if ch in "aeiouAEIOU":    
                counter += 1
    print("Total number of vowels:", counter)