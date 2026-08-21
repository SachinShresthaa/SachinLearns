def medical_agent(symptoms):

    if "fever" in symptoms and "cough" in symptoms:
        return "Possible Disease: Flu"

    elif "fever" in symptoms and "rash" in symptoms:
        return "Possible Disease: Chickenpox"

    elif "headache" in symptoms and "nausea" in symptoms:
        return "Possible Disease: Food Poisoning"

    elif "cough" in symptoms and "breathing problem" in symptoms:
        return "Possible Disease: Bronchitis"

    else:
        return "Disease not identified. Please consult a doctor."


print("=== Simple Medical Diagnosis Agent ===")

symptoms = input("Enter symptoms separated by comma: ").lower()
symptoms = [s.strip() for s in symptoms.split(",")]

result = medical_agent(symptoms)

print(result)