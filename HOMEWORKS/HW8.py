def show()->int:
    print("\n Выбери действие:\n"
          "1/ Отобразить весь справочник  \n"
          "2/  Найти абонента по имени\n"
          "3/  Найти абонента по номеру телефона \n"
          "4/  Добавить абонента в справочник\n"
          "5/  Сохранить справочник в текстовом формате\n"
          "6/  Выйти\n")
    choice = int(input("Введите номер команды"))
    return choice

def work_w_book(choice):

        if choice ==1:
           print(read('phonebook.txt'))
        elif choice == 2:
           print(find_by_name())
        elif choice == 3:
           print(find_by_name())
        elif choice == 4:
            print(add_new())
        else:
            print("Еще в работе)")

def read(filename):
    data =[]
    data1=('Фамилия','Имя','Отчество','Телефон','Описание')
    with open(filename,'r', encoding='utf-8') as fin:
        for line in fin:
            record=dict(zip(data1, line.strip().split()))
            data.append(record)
    return data



def find_by_name():
    df = open('phonebook.txt', encoding='utf-8')
    str = input('Введите фамилию или имя или телефон')
    lines = df.readlines()
    print(lines)
    count = 0
    for line in lines:
        if str in line:
           print(line, end='')
           count+=1
    if count==0:
             print("Контакт не найден")
    df.close()


def add_new():
    print("Введите 'Фамилия','Имя','Отчество','Телефон','Описание' контакта через пробел:")
    user_data = input()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
      data.write(user_data)
      data.write('\n')
    return data

work_w_book(show())
