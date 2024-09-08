
def delete_html_tags(html_file, result_file='cleaned.txt'):

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    cleaned_content = ""
    inside_tag = False

    for char in html_content:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_content += char

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_content)

    print(f"Текст очищений і записаний у файл: {result_file}")

    print("\nОчищений текст:")
    print(cleaned_content)

html_file = input("Введіть ім'я HTML-файлу, який потрібно очистити: ")
result_file = input(
    "Введіть ім'я файлу, куди зберегти очищений текст (за замовчуванням cleaned.txt): ") or 'cleaned.txt'

delete_html_tags(html_file, result_file)