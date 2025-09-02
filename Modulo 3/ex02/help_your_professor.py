def average(d_students: dict[str, int]) -> float:
    """sum all values of a dict and return your avg"""
    if len(d_students) > 0:
        return sum(d_students.values()) / len(d_students)
    else:
        return 0
