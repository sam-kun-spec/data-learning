# ─── FILE HANDLING BASICS ───────────────────────────────────────────────────

# ── 1. Write to a file (creates it if it doesn't exist) ──────────────────────
f = open("yo.txt", "w")
f.write("Hello, World!\n")
f.write("Python file handling is easy.\n")
f.close()

# ── 2. Read the entire file ───────────────────────────────────────────────────
f = open("yo.txt", "r")
content = f.read()
f.close()
print("── read() ──")
print(content)

# ── 3. Read line by line ──────────────────────────────────────────────────────
f = open("yo.txt", "r")
print("── readline() ──")
print(f.readline())   # first line
print(f.readline())   # second line
f.close()

# ── 4. Read all lines into a list ─────────────────────────────────────────────
f = open("yo.txt", "r")
lines = f.readlines()
f.close()
print("── readlines() ──")
print(lines)

# ── 5. Append to a file (does NOT overwrite) ──────────────────────────────────
f = open("yo.txt", "a")
f.write("This line was appended.\n")
f.close()

# ── 6. Using 'with' statement (auto-closes the file) ──────────────────────────
with open("yo.txt", "r") as f:
    print("── with block ──")
    for line in f:
        print(line, end="")   # each line already has \n

# ── 7. Write multiple lines at once using writelines() ────────────────────────
lines_to_write = ["Line one\n", "Line two\n", "Line three\n"]
with open("new_file.txt", "w") as f:
    f.writelines(lines_to_write)

# ── 8. Check file position and seek ───────────────────────────────────────────
with open("yo.txt", "r") as f:
    f.read(5)              # read first 5 characters
    print("\n── tell() position after reading 5 chars:", f.tell())
    f.seek(0)              # go back to start
    print("── after seek(0):", f.read(5))   # reads first 5 again

# ── 9. Delete a file safely ───────────────────────────────────────────────────
import os
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
    print("\nnew_file.txt deleted")

# ── tip: run from this folder ─────────────────────────────────────────────────
# cd "python overall shit/file handling"
# python well.py
