def main(): 
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_total = count_words(text)
    letter_count = count_letter(text)
    report = to_report(letter_count, words_total)
    print(report)

def count_letter(text):
    result_dict = {}
    for letter in text:
        lowercase_letter = letter.lower()
        if lowercase_letter.isalpha():
            if lowercase_letter in result_dict:
                result_dict[lowercase_letter] += 1
            else:
                result_dict[lowercase_letter] = 1
    return result_dict

def to_report(dict_text, words_total):
    sorted = []
    for letter in dict_text:
        sorted.append({"letter": letter, "num": dict_text[letter]})
    sorted.sort(reverse=True, key=sort_on)
    report = f"Begin of Report\n{words_total} words were found in this text\n\n"
    for line in sorted:
        report += f"The letter '{line["letter"]}' is {line["num"]} in the document\n"
    report += "\nEnd of Report"
    return report

def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

main()