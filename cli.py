commands = ["hello", ["good bye", "close", "exit", "bye", "esc", "q"], "add", "change", "phone", "show all"]
phone_book = {"Vasya": "0505436565", "Lesya" : "0674231111"}


def add_phone(cont):
    contact = cont.split(' ')
    number_add= f'Введите все данные для добавления номера'
    if len(contact) == 3:
        
        for phone in phone_book:
            
            if phone.casefold() == contact[1].casefold():
                print(f'Контакт {contact[1]} уже есть в книге с номером {phone_book.get(phone)}')
                return True
                
        phone_book[contact[1]] = contact[2]   
        number_add = f'ok'
        
    print(number_add)

        


def change(contact):
    chng_cont = contact.split(' ')
    number_chng= f'Введите все данные для изменения номера'
    if len(chng_cont) == 3:
        number_chng = f'Нет контакта {chng_cont[1]} в Вашем списке'
        for phone in phone_book:
            if phone.casefold() != chng_cont[1].casefold():
                continue
            else:
                phone_book[phone] = chng_cont[2]
                number_chng = f'Контакт {chng_cont[1]} изменен' 
            
    print(number_chng)

def phone(contact):
    c_number=contact.split(" ")
    number = 'Введите контакт, который вы ищите'
    if len(c_number) == 2:
        number = f'В ваших контактах отсутствует {c_number[1]}'
        for phone in phone_book:
            if c_number[1].casefold() == phone.casefold():
                number = f'{phone_book.get(phone)}'
    print(number)
    
    
def reply(command):
    bot=True
    operator=command.lower().split(" ")
    if command.lower() in commands[1]:
        print(answers[1])
        print(phone_book)
        bot = False
    elif operator[0] in commands or command.lower() in commands:
        try:
            index_comm = commands.index(command.lower())
        except ValueError:
            index_comm = commands.index(operator[0])

        try:
            answers[index_comm](command)
        except:
            print(answers[index_comm])
    else:
        print(f'Введите правильную команду :{commands[0],commands[2:]} или {commands[1]} для выхода')
    return bot

def show_all(x):
    for name, phone in phone_book.items():
        print(f'Name: {name}, phone number {phone}')



answers = ["How can I help you?", "Good bye!",add_phone, change, phone, show_all]


def main():
    working_bot= True
    while working_bot:
        print('->')
        command = input()
        working_bot = reply(command)
        
if __name__ == '__main__':
    main()


