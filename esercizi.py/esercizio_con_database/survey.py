import string

class Survey:
    def __init__(self, attr = {}):
        self.__name = attr.get('name', None)
        self.__age = attr.get('age', None)
        self.__height = attr.get('height', None)
        self.__married = attr.get('married', None)
        self.__subjects = attr.get('subjects', [])

    # Getters - Readers
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_height(self):
        return self.__height
    
    def get_married(self):
        return self.__married
    
    def get_subjects(self):
        return self.__subjects
    
    # Setters - Writers
    def set_name(self, new_name):
        if self.__name_validation(new_name):
            self.__name = new_name
            return { 'successful': True }
        return { 'successful': False, 'error_message': 'Nome invalido: usare solo lettere a-z' }

    def set_age(self, new_age):
        if self.__age_validation(new_age):
            self.__age = int(new_age)
            return { 'successful': True }
        return { 'successful': False, 'error_message': 'Età invalida: usare solo numeri interi' }
    
    def set_height(self, new_height):
        if self.__height_validation(new_height):
            self.__height = float(new_height)
            return { 'successful': True }
        return { 'successful': False, 'error_message': 'Altezza invalida: usare numeri float' }
    
    def set_married(self, new_married):
        if self.__yes_no_validation(new_married):
            self.__married = new_married in ['si', 'sì']
            return { 'successful': True }
        return { 'successful': False, 'error_message': 'Risposta invalida: usare si/no' }
    
    def set_subjects(self, new_subject):
        if new_subject != '' and new_subject not in self.__subjects:
            self.__subjects.append(new_subject)
            return { 'successful': True }
        elif new_subject != '' and new_subject in self.__subjects:  
            return { 'successful': False, 'error_message': 'Materia già inserita' } 
        elif new_subject == '':
            return { 'successful': False, 'error_message': 'Materia invalida: non può esser vuoto' } 
        

    # Validation

    def __name_validation(self, name):
        for letter in name:
            if letter.isdigit() or letter in list(string.punctuation):
                return False
        return True
    
    def __age_validation(self, age):
        try:
            # print('Sto cercando di convertire l\'età')
            int(age)
            # print('Conversione avvenuta con successo')
            return True
        except:
            # print('Conversione fallita')
            return False
        
    def __height_validation(self, age):
        try:
            # print('Sto cercando di convertire l\'età')
            float(age)
            # print('Conversione avvenuta con successo')
            return True
        except:
            # print('Conversione fallita')
            return False

    def __yes_no_validation(self, answer):
        if answer in ['si', 'no', 'sì']:
            return True
        return False