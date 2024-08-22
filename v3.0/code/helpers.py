def load_replacements(file_path='replacements.txt'):
    replacements = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '|' in line:
                    find, replace = line.strip().split('|', 1)
                    replacements[find] = replace
                    replacements[replace] = find  # إضافة الاستبدال العكسي تلقائيًا
    except FileNotFoundError:
        print(f"File {file_path} not found. No replacements loaded.")
    return replacements

def convert_code(code, replacements):
    # احتفظ بسجل للتحويلات لمنع التكرار
    previous_codes = set()

    while code not in previous_codes:
        previous_codes.add(code)
        prev_code = code
        for find_word, replace_word in replacements.items():
            code = code.replace(find_word, replace_word)
        if code == prev_code:
            break  # توقف التكرار إذا لم يكن هناك أي تغيير
    return code
