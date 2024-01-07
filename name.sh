#!/bin/bash

# Navigate to the directory containing the files
cd /path/to/your/directory

# Loop through each .py file
for file in *.py; do
    # Extract the current number from the filename
    current_number=$(echo "$file" | grep -oE '[0-9]+' | sed 's/^0*//')

    # Pad the number to three digits
    padded_number=$(printf "%03d" "$current_number")

    # Construct the new filename with the padded number
    new_filename="${padded_number}.py"

    # Rename the file
    mv "$file" "$new_filename"

    # Print the changes
    echo "Renamed $file to $new_filename"
done

