import os
import random

# Path to the combined dataset folder
combined_dataset_folder = "/Users/shreya/Desktop/datasets/combined-dataset"  # Change this to your folder path
output_messages_folder = os.path.join(combined_dataset_folder, "messages")
os.makedirs(output_messages_folder, exist_ok=True)  # Create messages folder if it doesn't exist

# Sample data for generating placeholders
blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
diagnoses = ["Brain Tumor", "Lung Cancer", "Heart Disease", "Fracture", "Infection", "Stroke"]
medications = ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"]
ages = range(20, 90)  # Age range: 20 to 90

# Function to generate synthetic medical-like text
def generate_medical_text(index):
    patient_id = random.randint(10000, 99999)
    blood_type = random.choice(blood_types)
    diagnosis = random.choice(diagnoses)
    meds = ", ".join(random.sample(medications, random.randint(1, 3)))
    age = random.choice(ages)

    # Format the text message
    text = (
        f"Patient ID: {patient_id}\n"
        f"Blood Type: {blood_type}\n"
        f"Diagnosis: {diagnosis}\n"
        f"Medications: {meds}\n"
        f"Age: {age}"
    )
    return text

# List all PNG files in the combined dataset
png_files = [file for file in os.listdir(combined_dataset_folder) if file.lower().endswith(".png")]

# Generate and save placeholder text files
for idx, png_file in enumerate(png_files, start=1):
    message_file_name = f"message_{idx}.txt"
    message_path = os.path.join(output_messages_folder, message_file_name)
    
    # Generate synthetic medical text
    synthetic_text = generate_medical_text(idx)
    
    # Save the text to a file
    with open(message_path, "w") as text_file:
        text_file.write(synthetic_text)

print(f"Generated {len(png_files)} medical-like placeholder text files in '{output_messages_folder}'.")
