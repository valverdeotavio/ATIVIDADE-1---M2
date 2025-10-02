from typing import List

def sequence(entry: str) -> int:
    correct_sequence: List[str] = ["B", "C", "D", "A"]
    user_sequence: List[str] = list(entry.upper())

    points = 0

    if len(user_sequence) != 4:
        return 0
    
    if user_sequence[3] == "A":
        points += 5

    for i in range(3):
        if user_sequence[i] == "C" and user_sequence[i + 1] == "D":
            points += 5

    for i in range(4):
        if user_sequence[i] == correct_sequence[i]:
            points += 20

    return points