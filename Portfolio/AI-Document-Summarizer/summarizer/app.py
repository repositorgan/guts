# What? Produce output that summarize input text or text file plus a save option. 
# How? Allow portability to varying operating systems via the python3 interpreter. Powered with artificial intelligence, (AI).
# Why? Clean command line interface, (CLI), experience of terminal input to output summary for streamlined efficiency in human interpretation to drive interaction.
# Who? User on interaction or those with a document of text to summarize.
# Where? CLI and text file. 
#!/usr/bin/env python3

"""
AI-Powered Text Summarizer CLI Tool
Features:
- CLI support (argparse)
- Error handling (missing or empty file)
- Output to file option
- Verbose mode option
- Clean, production-ready architecture
"""

# Import necessary modules.
import argparse # Input analysis (parsing) processed with grammar.
import sys # System exit.
import os # File path.
import time # Timestamping.

# Import (AI text summarization and load text file) functions from called upon modules.
from .model import summarize_text
from .utils import load_text

# Spinner animation for longer operations. Heighten user experience, (UX).
def spinner():
  # Function to cycle through characters.
  while True:
    for frame in "|/-\\":
      yield frame

# Define main CLI function as script runs. 
def main():
  # Initialize parser (analysis) with description.
  parser = argparse.ArgumentParser(
    description="AI-powered text summarizer CLI tool"
  )
  # Input the text file we want to consolidate.
  parser.add_argument(
    "input_file",
    type=str,
    help="Path to the text file you want to summarize"
  )
  # Output text file naming.
  parser.add_argument(
    "-o", "--output",
    type=str,
    help="Optional output file to save the summary"
  )
  # Allow for plenty of, (verbose), documentation of each step of process (ideal for teaching and auditing).
  parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="Enable verbose mode for detailed logs"
  )

  # Analyse the user argument.
  args = parser.parse_args()

  # Qualify input file.
  if not os.path.exists(args.input_file):
    print(f"Error: File not found: {args.input_file}")
    sys.exit(1)

  # Load and read text file.
  if args.verbose:
    print(f"[INFO] Loading file: {args.input_file}")
  text = load_text(args.input_file)
  
  # Prevent empty file summarization.
  if not text.strip():
    print("Error: File is empty. Cannot summarize an empty text file.")
    sys.exit(1)

  # Show summarization is rendering
  if args.verbose:
    print("Generating summary...")
  
  # Display spinner.
  spin = spinner()
  for _ in range(10):
    sys.stdout.write(next(spin))
    sys.stdout.flush()
    time.sleep(0.05)
    sys.stdout.write("\b")

  # Executive AI summarization.
  summary = summarize_text(text)
  
  # Print summary to console.
  print("\n=== SUMMARY RESULT ===\n")
  print(summary)

    # Save output to file if requested.
  if args.output:
    with open(args.output, "w", encoding="utf-8") as f:
      f.write(summary)

    print(f"\n Summary saved to: {args.output}")


# Direct execution only.
if __name__ == "__main__":
    main()
