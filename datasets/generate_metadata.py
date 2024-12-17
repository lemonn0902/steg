import os
import pandas as pd

# Paths to the folders
images_folder = "/Users/shreya/Desktop/datasets/combined-dataset"  # Path to PNG images
messages_folder = "/Users/shreya/Desktop/datasets/messages"        # Path to TXT files
output_csv_path = "metadata.csv"    # Output CSV file path

# List all image and message files
image_files = sorted([f for f in os.listdir(images_folder) if f.endswith('.png')])
message_files = sorted([f for f in os.listdir(messages_folder) if f.endswith('.txt')])

# Check if counts match
if len(image_files) != len(message_files):
    print("Warning: The number of image files and message files does not match!")
    print(f"Images: {len(image_files)}, Messages: {len(message_files)}")

# Combine data into a DataFrame
data = {
    "images": image_files,
    "message_files": message_files
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv(output_csv_path, index=False)
print(f"Metadata CSV generated successfully at '{output_csv_path}'!")
