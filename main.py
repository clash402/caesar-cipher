from art import logo

# PROPERTIES
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# METHODS
def code(text, shift, direction):
  message = ""

  for char in text:
    if char in alphabet:
      if direction == "encode":
        pos = alphabet.index(char) + shift
      elif direction == "decode":
        pos = alphabet.index(char) - shift
      message += alphabet[pos]
    else:
      message += char

  return f"\nThe {direction}d text is: {message}"


# MAIN
print(logo)

app_is_in_progress = True

while app_is_in_progress:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()

  if direction == "encode" or direction == "decode":
    pass
  else:
    print(f"ERROR: {direction} is not a command.")
    continue

  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: ")) % 25
  result = code(text, shift, direction)

  print(result)

  user_answer = input("Run again? (y/n) ").lower()
  
  if user_answer != "y":
    print("Goodbye")
    app_is_in_progress = False
