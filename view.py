#1 меню
import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) <9:
            return int(choice)
        
#2 открыть файл

# функция для вывода сообщений
def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

#3 показать контакт
#функция выводит на печать контакты

def print_contact(pb: list[dict[str, str]], error: str):
    if pb:
        print('\n' + '=' * 71)
        for i, contact in enumerate(pb, 1):
            #print(contact)
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("comment"):<20}')
        print('=' * 71 + '\n')
    else:
        print_message(error)

#добавить контакт
def input_contact(massage: str, cancel: str) -> dict:
    contact = {}
    print(massage)
    for key, value in text.input_contact.items():
    #     contact[key] = input(value)
    # return contact
        data = input(value)
        if data:
            contact[key] = data
            #print(contact)
        else:
            print_message(text.cancel_input)
    return contact

#удалить контакт 


def input_index(message: str, pb: list, error: str):
    print_contact(pb, error)
    while True:
        index = input(message)
        if index.isdigit and 0 < int(index) < len(pb) + 1:
            return int(index)
        


def input_find_contact():
    message = input(text.find_contact_info)
    return message