Description
A Python program that parses a file containing information about language "locales" and "charmaps" and generates output based on command-line options. Inspired by Unix's locale command.

Usage
python locale.py [option] [argument_file]

option: One of the following:

-a: Lists all available locale filenames.
-m: Lists all available charmap filenames.
-l [language]: Displays the total number of locales and charmaps for the specified language.
-v: Displays the author's name, surname, student ID, and date of completion.
argument_file: A text file containing comma-separated entries in the format:
type,language,filename

type: Either locale or charmap
language: Any string with letters, digits, underscores, or dots.
filename: Any string with letters, digits, underscores, or dots.
Examples
List all locales: python locale.py -a argument_file

Output: Available locales: en_AU fr_BE en_US

List all charmaps: python locale.py -m argument_file

Output: Available charmaps: EN GBK

Get locale and charmap count for a language: python locale.py -l English argument_file

Output: Language English: Total number of locales: 2 Total number of charmaps: 1

Error Handling
Prints an error if the argument file is missing, not readable, or the syntax is incorrect.
If no locales or charmaps are found, it prints: No locales available or No charmaps available
