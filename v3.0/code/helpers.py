def load_replacements(file_path='replacements.txt'):
    replacements = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if ' | ' in line:
                    find, replace = line.strip().split(' | ', 1)
                    replacements[find] = replace
                    replacements[replace] = find  
    except FileNotFoundError:
        print(f"File {file_path} not found. No replacements loaded.")
    return replacements

def convert_code(code, replacements):
   
    replaced_words = set()

    for find_word, replace_word in replacements.items():
      
        if find_word not in replaced_words:
            if find_word in code:
                code = code.replace(find_word, replace_word)
                replaced_words.add(find_word)
                replaced_words.add(replace_word)
                
    return code
