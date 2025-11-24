# projects 
# Digit-Origin Mapping Tool
  Welcome to the Digit-Origin Mapping Tool! This simple Python project helps you see how each digit forms from counting numbers and lets you trace any digit back to its original     number. 

## What This Project Does 
  When you enter an upper limit, the program expands every number from 1 up to your chosen index. It then builds a list that links every digit to the number it came from. You can       even ask which number a specific digit belongs to by providing its index in the list. This feature is perfect for exploring how numbers break down into digits! 

## Key Features 
 - Interactive prompts guide you through using the tool. - Displays a digit list from numbers 1 to your input, removing the last digit for demonstration.
 - Lets you pick a position and instantly tells you which number created that digit.
 - Includes basic error handling for invalid index choices. 

## Tech Stack 
  - Python 3 (no extra libraries required) 
  - VS Code


## Getting Started 
1. Clone this repository: bash git clone https://github.com/yourusername/digit-origin-mapping-tool.git cd digit-origin-mapping-tool
2. Run the tool: bash python digit_origin_mapper.py Use python3 if your system defaults to Python 2.

   
## Using the Program 
- First, enter a positive number when prompted. The program will build and display the digit list.
- Next, enter an index to find out the number that produced the digit at that spot.
- If you enter a number that isn’t in range for the digit list, the script will let you know it’s invalid.

  
## Testing 
Try running the tool several times with different numbers and indexes. 
Examples: 
- Enter 34 as your number to see digits from 1 to 34. 
- Try an index near the end or beyond the digit list to see how validation works.

## Output Digit list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 2, 0, 2, 1, 2, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 3, 0, 3, 1, 3, 2, 3, 3, 3] 
Enter index for whose original number you want to be printed: 33
Number: 21
