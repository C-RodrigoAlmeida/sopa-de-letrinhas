def sort_combinations(elements: dict[str, str]) -> dict[str, str]:
    return {**elements, **{f'-{key}': f'-{value}' for key, value in elements.items()}}
