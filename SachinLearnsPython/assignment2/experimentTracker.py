experiment_count = 0

def run_experiment():
    global experiment_count
    local_count = 1
    experiment_count += local_count
    print(f"Experiment run.{local_count}")

def show_count():
    print("Total experiments performed:", experiment_count)

run_experiment()
run_experiment()
run_experiment()
show_count()
