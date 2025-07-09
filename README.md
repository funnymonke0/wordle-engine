# 🧠 WordleEngine

**WordleEngine** is a Python-based solver for the popular word game **Wordle**. It narrows down possible solutions based on user-provided feedback (colors: green, yellow, black) and selects optimal guesses based on frequency analysis.

---

## 📂 Features

- Loads and manages Wordle answer and valid word lists.
- Simulates user feedback based on guesses (`g` = green, `y` = yellow, `b` = black).
- Suggests optimal guesses by evaluating letter frequencies across positions.

---

## 📄 Requirements

- Python 3.x
- Two word list files:
  - `answer.txt` – List of possible Wordle answers (one per line).
  - `valid_wordle_words.txt` – List of all acceptable guesses (one per line).

---

## 🚀 How to Use

1. **Prepare Word Lists**  
   Ensure you have `answer.txt` and `valid_wordle_words.txt` in the same directory. These files should contain one word per line.

2. **Run the Solver**  
   ```bash
   python wordle_engine.py
   ```

3. **Follow Prompts**  
   - Enter your **guessed word** (must be valid and 5 letters).
   - Enter the **color clue** using:
     - `g` = green (correct letter, correct spot)
     - `y` = yellow (correct letter, wrong spot)
     - `b` = black/gray (letter not in the word)

   Example:
   ```
   word: crate
   colors: bgybb
   ```

4. The engine will suggest the next best word. Repeat until solved.

---

## 🧠 Algorithm Summary

- Filters words based on given colors.
- Tracks letter frequencies for each position.
- Scores each candidate word:
  - Rewards high-frequency letters in optimal positions.
- Selects the best-scoring word as the next guess.

---

## 🔧 File Structure

```
📁 your_project_directory/
├── wordle_engine.py
├── answer.txt
└── valid_wordle_words.txt
```

---

## 📝 Example Session

```
word: slate
colors: bbybg
crate
colors: ggygg
crane
```
