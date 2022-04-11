from __future__ import annotations
from typing import Union

class StrArray:
    items: list[str]

    def __intit__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: str) -> StrArray:
        """Vectorized concatenation operator."""
         # Setup a result list of strings that's empty
        result: list[str] = []
        # loop through each item in self.items
        if isinstance(rhs, str):
            for item in self.items:
                # For each item, append the concatenation of item and rhs to result list
                result.append(item + rhs)
            # Return a  newly constructed StrArray whose items are result
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
            # Assert that len of self.items is equal to length of rhs.items
            # Build up the result list by concatening 
            # each item in self.items with corresponding item in rhs.items
        
        return StrArray(result)
    
first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!!!"
print(result)
print(first + " " + last)
print(last + ", " + first + "!!!")