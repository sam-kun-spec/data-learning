
""" What is NumPy?

**NumPy** = Numerical Python. It's a library for working with numbers and arrays super fast.

**Why use it?**
- Python lists are slow for math. NumPy arrays do the same thing 50x faster.
- Built-in math functions: sum, mean, standard deviation, etc.
- Essential for data science, machine learning, analytics.

**Example — why NumPy matters:**
```python
# Python list (slow)
my_list = [1, 2, 3, 4, 5]
result = [x * 2 for x in my_list]  # clunky

# NumPy array (fast + clean)
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2  # just multiply directly
```
```
[2 4 6 8 10]
```

---

## Installation

Open terminal and run:
```
pip install numpy
```

That's it. Takes 30 seconds.

**Verify it worked:**
```python
import numpy as np
print(np.__version__)
```

Should print a version number like `1.24.3` or similar.


"""

import numpy as np
print(np.__version__)
