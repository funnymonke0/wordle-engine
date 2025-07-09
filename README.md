🧠 WordleEngine
WordleEngine is a Python-based solver for the popular word game Wordle. It narrows down possible solutions based on user-provided feedback (colors: green, yellow, black) and selects optimal guesses based on frequency analysis.

📂 Features
Loads and manages Wordle answer and valid word lists.

Simulates user feedback based on guesses (g = green, y = yellow, b = black).

Suggests optimal guesses by evaluating letter frequencies across positions.

Interactive command-line input loop for manual play or automated trials.

📄 Requirements
Python 3.x

Two word list files:

answer.txt – List of possible Wordle answers (one per line).

valid_wordle_words.txt – List of all acceptable guesses (one per line).

🚀 How to Use
Prepare Word Lists
Ensure you have answer.txt and valid_wordle_words.txt in the same directory. These files should contain one word per line.

Run the Solver

bash
Copy
Edit
python wordle_engine.py
Follow Prompts

Enter your guessed word (must be valid and 5 letters).

Enter the color clue using:

g = green (correct letter, correct spot)

y = yellow (correct letter, wrong spot)

b = black/gray (letter not in the word)

Example:

makefile
Copy
Edit
word: crate
colors: bgybb
The engine will suggest the next best word. Repeat until solved or 6 attempts are done.

🔧 File Structure
Copy
Edit
📁 your_project_directory/
├── wordle_engine.py
├── answer.txt
└── valid_wordle_words.txt
📝 Example Session
makefile
Copy
Edit
word: slate
colors: bbybg
crate
colors: ggygg
crane
