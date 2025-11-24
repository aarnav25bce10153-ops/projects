# projects
# Digit-Origin Mapping Tool

Welcome to the Digit-Origin Mapping Tool! This simple Python project helps you see how each digit is formed from counting numbers and lets you trace any digit back to its original number.

## What This Project Does

When you enter an upper limit, the program expands every number from 1 up to your chosen index. It then builds a list linking every digit to the number it came from. You can even ask which number a specific digit belongs to by providing its index in the list—perfect for exploring how numbers break down into digits!

## Key Features

- Interactive prompts to guide you through using the tool.
- Displays a digit list from numbers 1 to your input, removing the last digit as a demonstration twist.
- Lets you pick a position and instantly tells you which number created that digit.
- Includes basic error handling if you pick an invalid index.

## Tech Stack

- Python 3 (no extra libraries required)
- VS Code

## Getting Started

1. *Clone this repository:*  
   bash
   git clone https://github.com/yourusername/digit-origin-mapping-tool.git
   cd digit-origin-mapping-tool
   
2. *Run the tool:*  
   bash
   python digit_origin_mapper.py
   
   Use python3 if your system defaults to Python 2.

## Using the Program

- First, enter a positive number when prompted. The program will build and display the digit list.
- Next, enter an index to discover the number that produced the digit at that spot 
- If you enter a number that isn’t in range for the digits list, the script gently lets you know it’s invalid.

## Testing

Try running the tool several times with different numbers and indexes.  
Examples:
- Enter 34 as your number to see digits from 1 to 34.
- Try an index near the end or beyond the digit list to see how validation works.
