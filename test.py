import unittest
from wallet import Wallet



class TestWallet(unittest.TestCase):


    def test_editing_record(self):

        dct = {}
        dct[1] = []
        dct[1].append({
        'category':"доходы",    
        'date': '21.12.2020',
        'summ': '132',
        'description': '123123'
        })

        id_editing = 1

        add = {'category':"расходы", 'date': '21.14.2020','summ': '1234','description': 'test'}
        
        result = {}
        result[1] = []
        result[1].append({
        'category':"расходы",    
        'date': '21.14.2020',
        'summ': '1234',
        'description': 'test'
        })
        
        self.assertEqual(Wallet.editing_record(self,dct,id_editing, add), result)
        
    def test_create_operation(self):
        data = {}
        category = 'расходы'
        date = '21.14.2020'
        summ = '1234'
        description = 'test'
        result = {}
        result[1] = []
        result[1].append({
        'category':"расходы",    
        'date': '21.14.2020',
        'summ': '1234',
        'description': 'test'
        })
        self.assertEqual(Wallet.create_operation(self,data,category,date,summ,description ), result)

        category = 'расходы'
        date = '21.14.2020'
        summ = '1234'
        description = 'test'
        
        data = {}
        data[1] = []
        data[1].append({
        'category':"расходы",    
        'date': '12.11.2023',
        'summ': '22',
        'description': 'начальные данные'
        })
        
        result = {}
        result[1] = []
        result[1].append({
        'category':"расходы",    
        'date': '12.11.2023',
        'summ': '22',
        'description': 'начальные данные'
        })

        
        app = {}
        app[2] = []
        app[2].append({
        'category':"расходы",    
        'date': '21.14.2020',
        'summ': '1234',
        'description': 'test'
        })

        result.update(app)
        
        self.assertEqual(Wallet.create_operation(self,data,category,date,summ,description ), result)

    def test_search_record(self):
        data = {}
        data[1] = []
        data[1].append({
        'category':"расходы",    
        'date': '12.11.2023',
        'summ': '22',
        'description': 'начальные данные'
        })

        
        app = {}
        app[2] = []
        app[2].append({
        'category':"доходы",    
        'date': '21.14.2020',
        'summ': '1234',
        'description': 'test'
        })

        data.update(app)

        
        category="расходы"    
        date=''
        summ= ''
        
        result = [1]

        self.assertEqual(Wallet.search_record(self,data,category,date,summ ), result)
        summ = '1234'
        category=''
        result = [2]
        self.assertEqual(Wallet.search_record(self,data,category,date,summ ), result)
        

        
if __name__ == "__main__":
  unittest.main()












  
