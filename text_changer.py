def rename_in_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()


        with open(output_file, 'w') as file:
            index = 0
            for line in lines:
                if 'luggagetags' in line:
                    parts = line.strip().split('/')
                    file_name = parts[-1].split('.')[0]  # Extracting the part to be changed

                    new_name = f"luggagetags_{index+1}"  # Modify the new prefix as needed
                    new_line = line.replace(file_name, new_name)
                    index += 1

                    file.write(new_line)

                    print(f"Modified: {line.strip()} -> {new_line.strip()}")

                else:
                    file.write(line)

        print(f"File modification complete. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    input_file_path = "demo.txt"  # Replace with the path to your input file
    output_file_path = "demo.txt"  # Replace with the desired output file path

    rename_in_text_file(input_file_path, output_file_path)

