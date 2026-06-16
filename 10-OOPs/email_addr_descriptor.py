from collections import Counter

class EmailAddress:
    def __init__(self, name):
        self._key = name
    
    def __set__(self, instance, clean_str):

        if not isinstance(clean_str, str):
            raise TypeError("your phrase should be string")
        
        clean_str = clean_str.strip().lower()

        if EmailAddress.at_counter(clean_str) == False:
            raise ValueError("your phrase must contain exactly one @")
        
        if EmailAddress.before_at_after(clean_str) == None:
            raise ValueError("There must be at least one character before and after the @.")
    
        instance.__dict__[self._key] = clean_str
    
    def __get__(self, instance, owner):
        if instance is None:
            return None
        return instance.__dict__.get(self._key, None)
    
    @staticmethod
    def at_counter(str):
        str_cnt = Counter(str)
        return str_cnt["@"] == 1
    
    @staticmethod
    def before_at_after(str):
        if "@" not in str:
            return None
        
        lst = str.split("@")

        if "" in lst:
            return None
        
        return lst


class Utilisateur:
    client = EmailAddress("email")


u = Utilisateur()

try:
    u.client = "  Contact@Email.Com "
    print(u.client)

except Exception as e:
    print(e)

try:
    u.client = "contactemail.com"
    print(u.client)
except ValueError as e:
    print(e)

try:
    u.client = "abc@def@ghi"
    print(u.client)
except Exception as e:
    print(e)
