alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      if shift_amount > 26:
        shift_amount = shift_amount % 26
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

status = True

while status:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  continue_cipher = input("Type 'yes' if you want to cipher again. \n Otherwise, type 'no' to end the program.")
  if continue_cipher.lower() == 'no':
    status = False
    print("The program has ended.")