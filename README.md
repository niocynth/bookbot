# BookBot

BookBot is a Python program that analyzes the contents of a book and generates a report on word and character frequency.

## Features

- Counts the total number of words in a book.
- Counts the frequency of each character (case-insensitive, excluding spaces and newlines).
- Sorts and displays character counts in descending order.

## Usage

1. Place your book text files in the `books/` directory.
2. Run the program from the command line:

   ```sh
   python3 main.py books/frankenstein.txt
   ```

   Replace `books/frankenstein.txt` with the path to your desired book file.

## Output

The program prints a report showing:
- The path to the analyzed book.
- The total word count.
- The frequency of each character.

## File Structure

- `main.py`: Entry point; handles reading files and orchestrating analysis.
- `stats.py`: Functions for word and character counting.
- `report.py`: Generates and prints the analysis report.
- `books`: Directory containing book text files.

## Example

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 7352 total words
--------- Character Count -------
e: 4532
t: 3891
a: 3120
...
```

## License

This project is for educational purposes.
