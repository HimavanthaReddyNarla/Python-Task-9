# Python File Lab

This project contains runnable solutions for all 15 file-handling exercises. The same Python functions power the terminal menu and the local browser interface.

## Start the browser app

From this folder, run:

```powershell
python app.py
```

The app starts on `127.0.0.1` using an available port from 5000 to 5010 and opens the page in your browser. Stop it with `Ctrl+C` in the terminal.

## Run the terminal menu

```powershell
python python_tasks.py
```

Choose an exercise from 1 to 15, or choose 0 to exit. The student record exercises keep their data in text files in this folder.

## Files created on first run

- `welcome.txt` contains the two welcome lines.
- `student_names.txt` contains five names.
- `sample_lines.txt` contains five lines for the reading and counting exercises.
- `students.txt` starts with three names and marks; the append and mini-management exercises use this file.
- `student.txt`, `task11_students.txt`, `record_students.txt`, and `validated_students.txt` are created as needed.

Flask is required for the browser app. The terminal exercises use only the Python standard library.