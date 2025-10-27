# Reflection — Static Code Analysis (Lab 5)

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
- The **simpler issues** involved minor coding practices like using context managers and avoiding mutable default arguments. These were quick to correct since the tools clearly indicated the cause and the fix required only small edits.  
- The **most difficult fix** was the one involving `eval()`. Replacing it required finding a safe way to parse input (`ast.literal_eval`) while keeping the program’s behavior the same. It demanded more testing and reasoning compared to the style-related fixes.

---

## 2. Did the static analysis tools report any false positives? If so, describe one example.
- Overall, the tools were accurate, but **Pylint’s warning about the `global` statement** was not truly problematic in this project.  
  Since the script is short and not part of a larger application, maintaining a single global dictionary for inventory was a practical and acceptable design choice, even though it’s discouraged in larger systems.

---

## 3. How would you integrate static analysis tools into your actual software development workflow?
- I would include **Pylint**, **Flake8**, and **Bandit** as part of a **Continuous Integration (CI)** setup, for example through **GitHub Actions**.  
- Every time code is pushed or a pull request is opened, these tools would automatically run, checking for both logical and security issues.  
- Locally, I’d also use pre-commit hooks so that no code with lint or security errors can be committed, ensuring code quality right from the development stage.

---

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- **Security improved** after removing `eval()`, closing off the chance of arbitrary code execution.  
- **Code reliability increased** once the mutable default argument issue was fixed and exceptions were handled specifically.  
- **File operations became safer** due to the use of context managers, which automatically handle opening and closing files.  
- **Readability and organization** improved after renaming functions to `snake_case` and adding docstrings.  
- The overall outcome is a cleaner, safer, and easier-to-maintain script, confirmed by the post-fix results: Bandit found no issues and Pylint gave a score of 9.49/10.

---

**Author:** Aditya D Rao  
**Branch:** `fix/static-analysis-Aditya-D-Rao`  

