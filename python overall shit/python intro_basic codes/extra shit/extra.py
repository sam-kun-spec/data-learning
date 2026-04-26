# ============================================================
# WHAT IS:  if __name__ == '__main__' ?
# ============================================================
#
# Every Python file has a built-in variable: __name__
#   - Run file directly  → __name__ == "__main__"
#   - File is imported   → __name__ == "filename"
#
# So this line means:
#   "Only run this code if the file is run directly, not imported."
#
# WHY HACKERRANK USES IT:
#   Their system imports your file to test functions.
#   This guard stops the whole program from auto-running during tests.
#
# EXAMPLE:
#   def main():
#       print("Hello!")
#
#   if __name__ == '__main__':
#       main()   # only runs when YOU execute this file
#
# ------------------------------------------------------------

if __name__ == '__main__':
    pass  # replace 'pass' with main() or your code
