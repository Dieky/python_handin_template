import string
class TextContainer():
    def __init__(self,text=[]):
        self.text = text
    
    def __str__(self):
        return '{text} '.format(self.text)

    def count_words(self):
        counter = 0
        for word in self.text:
            counter += 1
        print(counter)
    
    def count_chars(self):
        counter = 0
        for word in self.text:
            for char in word:
                counter += 1           
        print(counter)
        
    def count_ascii(self):
        counter = 0
        for word in self.text:
            for char in word:
                if char in string.ascii_letters:
                    counter += 1           
        print(counter)