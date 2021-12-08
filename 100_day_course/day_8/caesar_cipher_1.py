alphabets = [chr(c) for c in range(ord('a'), ord('z')+1)]

from art import logo

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text,shift,direction):
    cipher_text=''
    if direction== 'decode':
            shift = abs(shift)* -1
    for char in text:
        if char in alphabets:
            position=alphabets.index(char)
            x=len(alphabets)
            new_position=(position+shift) % x
            cipher_text += alphabets[new_position]
        else:
            cipher_text+=char
    print(cipher_text)
    print(f'the {direction}d text is {cipher_text}' )
    
#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

def main():
    while True:
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
        result=input('do you want to continue, type yes or no?\n')
        if result=='no':
            print('Goodbye!')
            break


main()