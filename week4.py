# File Read & Write Challenge with Error Handling

def modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (convert to uppercase for example)
        modified_content = content.upper()

        # Write to the new output file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f" Modified content has been written to {output_file}")

    except FileNotFoundError:
        print(" Error: The file you entered does not exist.")
    except Exception as e:
        print(f" An error occurred: {e}")


# --- Main Program ---
filename = input("Enter the name of the file to read: ")
new_filename = "modified_" + filename

modify_file(filename, new_filename)
