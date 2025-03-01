#!/bin/bash
INPUT_FILE="proprietary-files.txt"  # The file containing the list of paths
SEARCH_DIR="/home/j0sh1x/Downloads/angler-opm7.181205.001/root"  # The directory where files will be searched
OUTPUT_FILE="output.txt"  # The file where results will be written

> "$OUTPUT_FILE"  # Clear the output file before writing

while IFS= read -r line; do
    # Extract the filename from the path
    filename="${line##*/}"
    
    # Find the file in the search directory
    found_paths=$(find "$SEARCH_DIR" -type f -name "$filename" 2>/dev/null)
    
    for found_path in $found_paths; do
        if [[ -n "$found_path" ]]; then
            # Remove the search directory prefix completely
            relative_path="${found_path#"$SEARCH_DIR/"}"
            
            # Ensure the new path retains the vendor/system structure correctly
            new_entry="$relative_path:$relative_path"
            
            # Write to output file
            echo "$new_entry" >> "$OUTPUT_FILE"
        fi
    done
done < "$INPUT_FILE"

echo "Processing complete. Output saved to $OUTPUT_FILE"
