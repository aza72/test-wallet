import json
from typing import List,Dict


class Wallet:
    
    def __init__(self,file ):
        self.file = file
        
#Открытие текстового файла используемого в качестве бд
    def open_file(self)->Dict[int, Dict[str,str]]:
       with open(self.file) as json_file:
           try:
               data = json.load(json_file)
               return data
           except:
               data = {}
               return data 
#Запись данных в файл в формате Json         
    def record_file(self,data:Dict[int, Dict[str,str]])->None:
        with open(self.file, 'w') as outfile:
            try:
                json.dump(data, outfile,ensure_ascii=False)
                print('Запись успешно сохранена')
            except:
                print('ОШИБКА!!! Что то пошло не так')
#Удаление записи            
    def delete_record(self, file:Dict[int, Dict[str,str]], id_delete:int)->None:
        with open(self.file, 'w') as outfile:
            try:
                del file[id_delete]
                json.dump(file, outfile,ensure_ascii=False)
                print('Запись успешно удалена')
            
            except:
                print('ОШИБКА!!! Что то пошло не так')
#Создание записи для изменения test+
    def editing_record(self,file:Dict[int, Dict[str,str]], id_editing:int, add:Dict[str,str])->Dict[int, Dict[str,str]]:
        value:Dict[str,str] = file[id_editing][0]
        
        if add['category']:
            value['category']=add['category']
            
        if add['date']:
            value['date']=add['date']
            
        if add['summ']:
            value['summ']=add['summ']

        if add['description']:
            value['description']=add['description']    

        file[id_editing][0] = value

        return file
        
        
#создание записи для сохранения test+
        

    def create_operation(self, data:Dict[int, Dict[str,str]], category:str,date:str,summ:str,description:str)->Dict[int, Dict[str,str]]:
        if len(data)==0:
            key = 1
        else:
            key = int(list(data)[-1])+1
            
        dct = {}
        dct[key] = []
        dct[key].append({
        'category':category,    
        'date': date,
        'summ': summ,
        'description': description
        })

        data.update(dct)
        return data

#Поиск записей test+
    def search_record(self, data:Dict[int, Dict[str,str]], category:str, date:str, summ:str)->List[int]:
        result:List[int] =[]
        
        for index in data:
            for x in data[index]:
                if x['category']==category or x['date']==date or x['summ']==summ:
                    result.append(index)
        if len(result)==0:
            print('Ничего не найдено')
        print(result)
        return result

#Функция отображения баланса               
    def show_balance(self,data)->None:
        result_income:List[int] =[]
        result_expenses:List[int] =[]
        for index in data:
            for x in data[index]:
                if x['category']=='расходы':
                    result_expenses.append(int(x['summ']))
                elif x['category']=='доходы':
                 result_income.append(int(x['summ']))

        balance:int = sum(result_income)-sum(result_expenses)         
        print('Ваш баланс составляет ',balance,'\n',
              'Доходы ',sum(result_income),'\n',
              'Расходы ',sum(result_expenses),'\n',)

#Отображение записей
    def show_record(self, data:Dict[int, Dict[str,str]], index_change:List[str])->None:

        for index in index_change:
            for x in data[index]:
                print('ID: ',index,'\n',
                      'Категория: ',x['category'],'\n',
                      'Дата: ',x['date'],'\n',
                      'Сумма операции: ',x['summ'],'\n',
                      'Описание: ',x['description'],'\n',
                      '__________________________________','\n')
             
         
#Ввод информации для поиска записи

    def input_record(self)->Dict[str,str]:
        record:Dict[str,str]= {}
        
        print('Введите категорию записи','\n',
              '1. Доходы','\n',
              '2. Расходы','\n')
        cat:str = input()
        if cat=='1':
            category = 'доходы'
        elif cat=='2':
            category = 'расходы'
        else:
            category = ''
            
            
        print('Введите дату в формате dd.mm.yyyy ','\n')
        date:str = input()
        print('Введите сумму операции ','\n')
        summ:str = input()
        print('Описание ','\n')
        description:str = input()
        
        record = {'category':category,'date':date,'summ':summ,'description':description}
        
        return record
    

path:str = 'data.txt'
data = Wallet(path)
file:Dict[int, Dict[str,str]]= data.open_file()

while True:
    print('Учет личных доходов и расходов','\n',
          '1. Узнать баланс','\n',
          '2. Добавить новую запись','\n',
          '3. Поиск по записям (удаление,редактирование)','\n',
          '4. Выход','\n',)
    case = input('Введите номер действия которое необходимо выполнить ')

    if case =='1':
        data.show_balance(file)
        
    elif case =='2':
        add:Dict[str,str] = data.input_record()
        if add==False:
            continue
        create = data.create_operation(file,add['category'],add['date'],add['summ'],add['description'])
        data.record_file(create)

    elif case =='3':
        print('Введите данные для поиска','\n',)
        add:Dict[str,str] = data.input_record()
        if add==False:
            continue
        index_change:List[int] = data.search_record(file,add['category'],add['date'],add['summ'])
        data.show_record(file,index_change)
        print('Введите действие','\n',
              '1. Удалить запись','\n',
              '2. Редактировать запись','\n',
              '3. Выйти','\n')
        choice = input()
        if choice == '1':
            print('Введите ID записи для удаления','\n')
            id_delete = input()
            data.delete_record(file,id_delete)

        elif choice =='2':
            print('Введите ID записи для редактирования','\n')
            id_editing = input()
            print('Заполните поля которые вы хотите отредактировать в противном случае пропустите их','\n')
            add:Dict[str,str] = data.input_record()
            save:Dict[int, Dict[str,str]] = data.editing_record(file,id_editing,add)
            data.record_file(save)

        elif choice =='3':
            continue
            
        else:
            print('Ошибка ввода')
            continue

        
    elif case =='4':
        break
    else:
        print('Ошибка ввода')

    


    
