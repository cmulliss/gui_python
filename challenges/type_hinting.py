from typing import List

# hints that the sequence needs be a list and returns a float
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)


list_avg()


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
