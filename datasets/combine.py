import os
from PIL import Image

# Input folder paths
input_folders = [
    "/Users/shreya/Desktop/datasets/bone-xray-dataset",
    "/Users/shreya/Desktop/datasets/brain-mri-dataset",
    "/Users/shreya/Desktop/datasets/breast-ultrasound"
]

# Output folder
output_folder = "/Users/shreya/Desktop/datasets/combined-dataset"
os.makedirs(output_folder, exist_ok=True)

# Function to convert and save images sequentially
def combine_and_convert(input_folders, output_folder):
    scan_counter = 1  # Start numbering scans
    for folder in input_folders:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            # Check for valid image files
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    # Open image and convert to RGB (ensures PNG compatibility)
                    img = Image.open(file_path).convert("RGB")
                    # Save image to the output folder as PNG
                    output_path = os.path.join(output_folder, f"scan_{scan_counter}.png")
                    img.save(output_path, "PNG")
                    print(f"Saved: {output_path}")
                    scan_counter += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

# Run the function
combine_and_convert(input_folders, output_folder)
print("All images combined and renamed successfully!")
