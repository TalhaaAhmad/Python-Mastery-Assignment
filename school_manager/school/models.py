# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_number: int
    marks: list[float] = field(default_factory=list)

    def average(self) -> float:
        if len(self.marks) == 0:
            return 0.0
        return sum(self.marks) / len(self.marks)
