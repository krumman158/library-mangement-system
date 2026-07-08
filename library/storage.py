from library.config import DATA_FILE

def read_all_lines() -> list[str]:
  """Return every non-empty line from the data file."""
  with open(DATA_FILE, "r") as file:
    return [line for line in file.read().splitlines() if line.strip()]


def write_all_lines(lines: list[str]) -> None:
 """Overwrite the data file with these lines."""
 with open(DATA_FILE,'w') as file:
   for line in lines:
     file.write(line+'\n')


def append_line(line: str) -> None:
 """Add one line to the end of the data file."""
 with open(DATA_FILE,'a') as file:
   file.write(line + "\n")