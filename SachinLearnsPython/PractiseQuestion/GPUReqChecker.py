    # GPU Requirement Checker for Deep Learning

# Taking input from user
ram = float(input("Enter RAM size (in GB): "))
gpu = float(input("Enter GPU memory (in GB): "))
cuda_input = input("Is CUDA available? (True/False): ")

# Convert string input to boolean
cuda = cuda_input.lower() == "true"

# Conditions
ram_ok = ram >= 16
gpu_ok = gpu >= 6
cuda_ok = cuda == True

# Final decision using logical operators
if ram_ok and gpu_ok and cuda_ok:
    print("System is READY for Deep Learning model training ")
else:
    print("System is NOT suitable for Deep Learning ")

    # Optional detailed feedback
    if not ram_ok:
        print("- Increase RAM to at least 16 GB")
    if not gpu_ok:
        print("- GPU memory should be at least 6 GB")
    if not cuda_ok:
        print("- CUDA must be enabled (True)")