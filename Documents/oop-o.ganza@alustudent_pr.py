class Patient:
    def __init__(self, id, name, age, gender, admission_date, condition):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    def get_details(self):
        return (f"Patient ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Admission Date: {self.admission_date}\n"
                f"Condition: {self.condition}")


def count_patients(patient_list):
    return len(patient_list)


def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]


# Creating multiple Patient objects
patient1 = Patient(1, "Alice Johnson", 30, "Female", "2024-10-01", "Flu")
patient2 = Patient(2, "Bob Smith", 45, "Male", "2024-10-05", "Cough")
patient3 = Patient(3, "David Brown", 28, "Male", "2024-10-10", "Headache")

# Storing patients in a list
patients = [patient1, patient2, patient3]

# Counting the number of patients
total_patients = count_patients(patients)
print(f"Total number of patients: {total_patients}")

# Listing all patient names
patient_names = list_patient_names(patients)
print("Patient Names:", patient_names)


# Input for patient ID
try:
    patient_id_to_search = int(input("Enter Patient ID to search: "))
    found = False
    for patient in patients:
        if patient.id == patient_id_to_search:
            found = True
            print("\nPatient Details:")
            print(patient.get_details())
            break
    if not found:
        print("Patient not found.")
except ValueError:
    print("Invalid input. Please enter a valid integer for Patient ID.")
    