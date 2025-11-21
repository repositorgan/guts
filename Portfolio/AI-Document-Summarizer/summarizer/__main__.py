## Input example.
## We want to import main() function from: app.y
## Why? Cross product capacity of project.
# python -m summarizer example.txt
from .app import main
if __name__ == "__main__":
  ## Call command line interface, (CLI), entry function from: app.py
  main()
