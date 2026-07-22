import datetime


def log_event(message, filepath="app.log"):
    try:
        timestamp = datetime.datetime.now()
        ts_str = timestamp.strftime("%y-%m-%d %H:%M:%S")

        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"[{ts_str}] {message}\n")

    except PermissionError:
        print("Error: You do not have permission to write to this file.")

    except OSError as error:
        print(f"File error: {error}")


log_event("Application started")
log_event("Training started")