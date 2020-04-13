# ReadFromTerminal
###### Python

## The program:
Your program must perform three different tasks in high precision.
- The first task is to count the vowels in a string. For our propose the letter ‘y’ will always be a
vowel.
- The second task is to print the Nth Perfect Power number. Perfect Power numbers are defined
in https://en.wikipedia.org/wiki/Perfect_power
- The last task is to print the Nth lazy caterer number. lazy caterer numbers are defined in
https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence
Input using the argparse library:
one string ('task') and another argument ('arg')

### Output:
The answer should be printed to the terminal

### Some Examples:
- Running from the terminal: python sample.py --task=vowels--arg=import_antigravity
	* Output: 7
- Running from the terminal: python sample.py --task=vowels--arg="You only killed the
 bride's father, you know. I didn't mean to. Didn't mean to? You put your sword right
 through his head. Oh dear... is he all right?"
 	* Output: 46
- Running from the terminal: python sample.py --task=perfect --arg=1
	* Output: 1
- Running from the terminal: python sample.py --task=perfect --arg=15
	* Output: 125
- Running from the terminal: python sample.py --task=lazy --arg=37
	* Output: 667
- Running from the terminal: python sample.py --task=lazy --arg=94
	* Output: 4372
