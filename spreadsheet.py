
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.isdigit():
            return int(value)
        try:
            float(value)  # Check if it can be converted to float
            return "#Error"
        except ValueError:
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            elif value.startswith("='") and value.endswith("'"):
                return value[2:-1]
            elif value.startswith("="):
                ref_value = value[1:]
                if ref_value.isdigit():
                    return ref_value
                elif ref_value in self._cells:
                    referenced_value = self._cells[ref_value]
                    if cell == referenced_value[1:]:
                        return "#Circular"
                    if referenced_value.isdigit():
                        return referenced_value
                    try:
                        float(referenced_value)
                        return "#Error"
                    except ValueError:
                        pass
                elif "+" in ref_value:
                    parts = ref_value.split("+")
                    if all(part.strip().isdigit() for part in parts):
                        return str(sum(int(part.strip()) for part in parts))
            return "#Error"

