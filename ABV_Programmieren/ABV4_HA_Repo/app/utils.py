from app.models import Student




def load_students() -> list[Student]:
    raw_rows = [
        {"name": " anna ", "points": "10", "passed": "true"},
        {"name": "ben", "points": "N/A", "passed": "false"},
        {"name": "carl", "points": "8", "passed": "true"},
        {"name": "max", "points": "2", "passed": "FALSE"},
        {"name": "TOM", "points": "Five", "passed": "True"},
        {"name": "hANNAH ", "points": "3", "passed": "false"},
        {"name": " jakob ", "points": "7", "passed": "true"},
        {"name": "MARION     ", "points": "7"},
    ]

    students = []
    for row in raw_rows:
        try:
            # Eingerückt: Gehört zur Schleife und zum Try-Block
            student = Student.from_csv_row(row)
            students.append(student)
        except ValueError as e:
            # Eingerückt: Passiert nur, wenn ein Fehler auftritt
            name = row.get("name", "unknown").strip().lower()
            print(f"Row skipped (invalid points): {name} -> {e}")
            
    # Ganz wichtig: Zurück auf die Ebene der Funktion schieben!
    return students


def calculate_average_points(students: list[Student], min_students: str) -> float:
    required_count = int(min_students)
    if len(students) <= required_count:
        raise ValueError("Not enough students to calculate a stable average.")

    points = []
    for student in students:
        points.append(student.points)
    total = sum(points)
    return total / len(points)


def print_report(students: list[Student], average: float) -> None:
    print("=== Course Report ===")
    for student in students:
        print(f"{student.name}: {student.points} points, passed={student.passed}")
    print(f"Average points: {average:.2f}")
