def format_names(d_name: dict[str, str]) -> list[str]:
    """Capitalize first name and last name of the a dictionary ans return a list"""
    return [x.capitalize() + " " + y.capitalize() for x, y in d_name.items()]
