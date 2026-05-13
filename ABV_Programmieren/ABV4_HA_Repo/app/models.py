from dataclasses import dataclass

def normalize_name(name: str) -> str:
    return name.strip().title()

@dataclass
class Student:
    name: str
    points: int
    passed: bool

    @classmethod
    def from_csv_row(cls, row):
        name = normalize_name(row["name"])
        try:
            points = int(row.get("points", ""))
        except (ValueError, TypeError):
            points = 0
        passed = str(row.get("passed", "false")).strip().title().lower() == "true"
        passed = points >= 5
        return cls(name=name, points=points, passed=passed)
