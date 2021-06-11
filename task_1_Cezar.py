class Cezar:
    alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    def __init__(self, words, lang='eng'):
        self.words = words.lower()
        self.lang = lang

    def change_lang(self):
        if self.lang == 'eng':
            self.lang = 'rus'
        else:
            self.lang = 'eng'
    
    def encrypt(self, step=7):
        encrypt_word = ''
        if self.lang == 'eng':
            tmp_alph = self.alphabet_eng
        else:
            tmp_alph = self.alphabet_rus
        for i in self.words:
            if i in tmp_alph:
                encrypt_word += tmp_alph[(tmp_alph.find(i) + step) % len(tmp_alph)]
            else:
                encrypt_word += i
        return encrypt_word

    def decrypt(self, step=7):
        decrypt_word = ''
        if self.lang == 'eng':
            tmp_alph = self.alphabet_eng
        else:
            tmp_alph = self.alphabet_rus
        for i in self.words:
            if i in tmp_alph:
                decrypt_word += tmp_alph[(tmp_alph.find(i) - step) % len(tmp_alph)]
            else:
                decrypt_word += i
        return decrypt_word
    

word = Cezar('Krokozyablik poshol domoi!')
print(word.encrypt())
crword = Cezar(word.encrypt())
print(crword.decrypt())

