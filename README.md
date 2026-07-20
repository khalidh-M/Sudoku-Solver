# 🧩 Sudoku Solver

A Python application that solves Sudoku puzzles using the **Backtracking Algorithm**.

This project was built to strengthen my understanding of Python programming, recursion, and algorithmic problem-solving. The solver automatically fills empty cells while following all Sudoku rules.

---

## 📌 Overview

Sudoku is a logic-based puzzle played on a **9 × 9 grid** divided into **3 × 3 subgrids**.

The objective is to fill every empty cell so that:

- Every row contains the numbers **1–9**
- Every column contains the numbers **1–9**
- Every 3 × 3 box contains the numbers **1–9**

This solver uses a **recursive backtracking algorithm** to find a valid solution.

---

## 🚀 Features

- Reads a Sudoku puzzle from a Python list
- Displays the original puzzle
- Finds empty cells automatically
- Validates moves according to Sudoku rules
- Solves the puzzle using recursion and backtracking
- Prints the solved board in a readable format

---

## 🛠 Technologies Used

- Python 3
- Recursion
- Backtracking Algorithm
- Functions
- Lists (2D Arrays)

---

## 📂 Project Structure

```
Sudoku-Solver/
│
├── solver.py
├── README.md
└── requirements.txt
```

---

## 🧠 Algorithm

The solver follows these steps:

1. Find the next empty cell.
2. Try placing numbers **1 to 9**.
3. Check whether the number is valid.
4. If valid, place the number.
5. Recursively solve the remaining puzzle.
6. If no valid number exists, backtrack and try another number.
7. Continue until the puzzle is solved.

This approach is known as the **Backtracking Algorithm**.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/khalidh-M/sudoku-solver.git
```

Move into the project directory:

```bash
cd sudoku-solver
```

Run the program:

```bash
python solver.py
```

---

## ▶️ Example Output
Example Output
![alt text](<Sudoku-Solver Unsolved Board-1.jpg>)
```
🧩 ORIGINAL BOARD

0 0 0 | 0 6 7 | 0 8 0
1 0 9 | 0 0 0 | 0 0 0
...

=========================

✅ SOLVED BOARD
Example Output
Images/Sudoku-Solver Solved Board.jpg

2 5 3 | 1 6 7 | 4 8 9
1 7 9 | ...
```

---

## 📚 What I Learned

Through this project, I improved my understanding of:

- Python functions
- Nested loops
- Lists and 2D arrays
- Recursion
- Backtracking algorithms
- Problem-solving techniques
- Code organization

---

## 🔮 Future Improvements

Planned enhancements include:

- Graphical User Interface (Tkinter)
- Random Sudoku puzzle generator
- Difficulty levels
- Input validation
- Performance optimization
- Web version using Streamlit or Flask

---

## 👨‍💻 Author

**Khalidh Murghay**

GitHub:
https://github.com/khalidh-M

---

⭐ If you found this project interesting, consider giving it a star!