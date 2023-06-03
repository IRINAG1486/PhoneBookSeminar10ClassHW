class PhoneBook:


    def __init__(self, path: str = 'phone.txt'):
        self.phone_book: list[dict[str, str]] = []
        self.path = path

   
    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            self.phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})
                

    
    def load(self):
        return self.phone_book

   
    def add(self, contact: dict[str, str]):
        self.phone_book.append(contact)
        return contact.get('name')

  
    def save(self):
        data = []
        for contact in self.phone_book:
            contact = ':'.join([value for value in contact.values()])
            data.append(contact)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    
    def dellcont(self, index: int):
        return self.phone_book.pop(index - 1).get('name')



    def find(self, pb: list[dict[str, str]], message: str, error: str):
        data: list[dict[str, str]] = []
        for contact in self.phone_book:
            for value in contact.values():
                if message.lower() in value.lower():
                    data.append(contact)
                    return data
                else:
                    error
    



  
    def change(self, info_contact, dict_contact: dict[str, str], error):
        for contact in self.phone_book:
            for value in contact.values():
                if info_contact.lower() in value.lower():
                    contact['name'] = dict_contact.get('name')
                    contact['phone'] = dict_contact.get('phone')
                    contact['comment'] = dict_contact.get('comment')
                else:
                    error
        return self.phone_book