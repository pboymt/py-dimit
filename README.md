# py-dimit

Dimension of a quantity in Python language.

## Installation

```bash
$ pip install dimit
# or
$ python -m pip install dimit
```

## Usage

```python
from dimit import Dimension, L, M, T, DIMLESS

# L is a preset dimension for length
Dimension('L') == L
# Output: True

# Build a dimension of velocity (LT^-1).
Velocity = L / T # or L * T**-1
# or
Velocity = Dimension('LT-1')
# Output: Dimension(LT-1)

# Only support operator *, / amd **.
L*L*L == L**3
# Output: True

# Compare two dimensions
Dimension('LMT-2') == Dimension('MLT-2')
# Output: True
```
