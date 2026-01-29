import string 

def counter_intelligence(encrypted_str):
    """
    encrypted message always signed off with kiss (x) 
    using the last letter see how it has shifted and decrypt the message
    """
   #     return encrypted_str.upper()

    upper_encrypted_str = encrypted_str.upper() 
    alphabet = list(string.ascii_uppercase)
    
    x_index = alphabet.index('X')       #standard x index is 23
    kiss = alphabet.index(upper_encrypted_str[-1])    #index of last letter of string - ? 
    shift = kiss - x_index              #difference
    
    decoded_string = ""

    for letter in upper_encrypted_str: 
        if letter in (" ", ".", ",", "(", ")", ":"):
            decoded_string += letter 
        else: 
            new_index = (alphabet.index(letter) - shift) % len(alphabet) #%len(alphabet) to loop back around the alphabet list when out of range
            updated_letter = alphabet[new_index]
            decoded_string += updated_letter
    print(decoded_string)
    return decoded_string

counter_intelligence("BCD Y")