with open('ping45.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Ersetze "Zeit" durch "time" und trenne die Zahl und "ms" mit einem Leerzeichen
        modified_line = line.replace("Zeit", "time").replace("ms", " ms")
        print(modified_line, end='')