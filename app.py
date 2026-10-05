"""Local browser interface for the Python file-handling exercises."""

import webbrowser

from flask import Flask, render_template, request
from werkzeug.serving import make_server

from python_tasks import TASK_TITLES, ensure_sample_files, execute_task


app = Flask(__name__)
ensure_sample_files()


@app.get("/")
def index():
    return render_template("index.html", tasks=TASK_TITLES, selected=1, output="")


@app.post("/run")
def run_exercise():
    output = ""
    selected = 1
    try:
        selected = int(request.form.get("task", "1"))
        if not 1 <= selected <= len(TASK_TITLES):
            raise ValueError("Choose a task from 1 to 15.")
        output = execute_task(selected, request.form)
    except (ValueError, FileNotFoundError, ZeroDivisionError, OSError) as error:
        output = f"Input or file error: {error}"
    return render_template("index.html", tasks=TASK_TITLES, selected=selected, output=output)


def main() -> None:
    server = None
    for port in range(5000, 5011):
        try:
            server = make_server("127.0.0.1", port, app)
            break
        except OSError:
            continue
    if server is None:
        raise RuntimeError("No available local port found between 5000 and 5010.")

    url = f"http://127.0.0.1:{server.server_port}"
    print(f"Python File Lab is running at {url}")
    try:
        webbrowser.open_new_tab(url)
    except webbrowser.Error:
        print("Open the URL above in your browser.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nPython File Lab stopped.")
        server.server_close()


if __name__ == "__main__":
    main()