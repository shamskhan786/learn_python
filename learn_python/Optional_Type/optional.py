from typing import Optional

# a: Optional[str] = "shams khan"
a: Optional[str] = None

if a is not None:
    print(a.upper())
else:
    print("Value is None")    