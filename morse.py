import tkinter as tk

# Morse code dictionary with both letters and digits
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Function to convert text to Morse code
def text_to_morse(text):
    return ' '.join(morse_code_dict.get(letter.upper(), '') for letter in text)

# Function to convert Morse code to text
def morse_to_text(code):
    reverse_dict = {value: key for key, value in morse_code_dict.items()}
    return ''.join(reverse_dict.get(letter, '') for letter in code.split())

# Function to determine and convert the input text
def convert_input():
    text = input_text.get()
    if set(text).issubset({'.', '-', ' ', '/'}):  # Morse code detection
        converted_text = morse_to_text(text)
    else:
        converted_text = text_to_morse(text)
    output_text.delete(1.0, "end")
    output_text.insert('end', converted_text)

# Setting up the Tkinter window
root = tk.Tk()
root.title("Morse Code Translator")

# Input text box with label
input_label = tk.Label(root, text="Enter Text or Morse Code:")
input_label.pack()
input_text = tk.Entry(root)
input_text.pack()

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_input)
convert_button.pack()

# Output text box with label
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Start the Tkinter event loop
root.mainloop()
