import re

class Cipher:


    def __init__(self, alphabet):
	    if alphabet == None or alphabet == '' or isinstance(alphabet,str) == False:
		    self.alphabet = 'abcdefghijklmnopqrstuvxwyz'
	    else:
		    self.alphabet = alphabet
		    
	    self.alpha_m = len(self.alphabet)
	    
	
	#Function to encrypt a single letter
    def encryption(self, letter, key1, key2):
        if self.is_coprime(key1, self.alpha_m) == False:
            raise ValueError('Key1 and size of alphabet must be coprimes!')
            
        if isinstance(letter,str) == True:
            if len(letter) > 1:
                raise Exception('Size of the string \'letter\' must be 1!')
                
            indexsearch = re.search(letter,self.alphabet)
            if indexsearch == None:
                raise Exception('Character not found in the alphabet!')
                
            letter = indexsearch.start()
        
        elif isinstance(letter,int) == False:
            raise ValueError('The value for letter must be an str or an int!!!')
            
        if isinstance(key1,int) == False or isinstance(key2,int) == False:
            raise ValueError('The value for key1 or key2 must be an int!!!')
            
        enc = (key1 * letter + key2) % self.alpha_m 
        return self.alphabet[enc]


    #Function to decrypt a single letter
    def decryption(self, letter, key1, key2):
        if self.is_coprime(key1, self.alpha_m) == False:
            raise ValueError('Key1 and size of alphabet must be coprimes!')
            
        if isinstance(letter,str) == True:
            if len(letter) > 1:
                raise Exception('Size of the string \'letter\' must be 1!')
                
            indexsearch = re.search(letter,self.alphabet)
            if indexsearch == None:
                raise Exception('Character not found in the alphabet!')
                
            letter = indexsearch.start()
            
        for x in self.alphabet:
            check_mmi = (key1 * self.alphabet.index(x)) % self.alpha_m 
            if check_mmi == 1:
                dec = self.alphabet.index(x) * (letter - key2) % self.alpha_m 
                
        return self.alphabet[dec]
        
    #Function to process full text
    #type: 1 - encryption, 2 - decryption
    def full_text(self, text, key1, key2, type):
        if isinstance(text, str) == False:
            raise ValueError('The text provided must be a string!')
            
        if isinstance(type, int) == False:
            raise ValueError('The \'type\' parameter must be an integer!')
            
        enc = ''
            
        for letter in text:
            if letter == ' ':
                enc = enc + letter
            else:
                if type == 1:
                    enc = enc + self.encryption(letter, key1, key2)
                elif type == 2:
                    enc = enc + self.decryption(letter, key1, key2)
                else:
                    raise ValueError('Value on \'type\' parameter invalid!')
                
        return enc
        
    
    
    def gcd(self, p,q):
    # Create the gcd of two positive integers.
        while q != 0:
            p, q = q, p%q
        return p
        
    def is_coprime(self, x, y):
        return self.gcd(x, y) == 1
    

