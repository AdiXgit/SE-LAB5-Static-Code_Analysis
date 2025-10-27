# Static Code Analysis — Issues and Fixes

## Selected 4 Main Issues

| # | Tool | Issue Type | Line(s) | Description | Fix Applied |
|---|------|-------------|----------|--------------|--------------|
| 1 | **Bandit** | **Security (High)** | 59 | Use of `eval()` on user input — dangerous, can execute arbitrary code. | Replaced `eval()` with `ast.literal_eval()` (or `json.loads()`), which safely parses input without executing code. |
| 2 | **Pylint** | **Bug (Medium)** | 8 | Mutable default argument `items=[]` can cause unexpected shared state between function calls. | Changed default argument to `None` and initialized list inside the function. |
| 3 | **Pylint** | **Security/Best Practice (High)** | 19 | Bare `except:` statement hides all exceptions, making debugging difficult and unsafe. | Replaced with `except ValueError:` and handled specific exceptions properly. |
| 4 | **Pylint** | **Best Practice (Medium)** | 26, 32 | File handling done without a context manager — file may stay open if an error occurs. | Used `with open(filename, "r", encoding="utf-8") as f:` for safe automatic closure. |


**Author:** *Aditya_D_RAO PES2UG23CS031*  
**Lab:** *Static Code Analysis – SE Lab 5*
