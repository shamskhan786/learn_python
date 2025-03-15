from typing import List,Union

# one way to define union type
x :List[str | int] = ["shams",23]

# another way to define union type
y :List[Union[int,float]] = [2.5,33.2,55,77]

i: List[Union[str, int, List[Union[str, int]]]] = ["shams khan", 90, ["shams khan", 90]]

