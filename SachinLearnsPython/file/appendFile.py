def log_event(message, filepath="app.log"):
    timestamp = datetime.datetime.now()
    ts_str = timestamp.strftime("%y-%m-%d %H:%M:%S")
    with open(filepath,"a", encoding="utf-8") as f:
        f.writing(f"[{ts_str}]{message}")

#Simulate 3 traning epochs
for epoch in range (1,4):
    accuracy = 0.75 + epoch*0.05
    log_event(f"Epoch{epoch}-accuracy:{accuracy:.2f}")

#read back log
with open("app.log","r") as f:
    print(f.read())