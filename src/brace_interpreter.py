import sys

def curly_to_indented(code):
    lines = code.splitlines()  # Split code into lines
    indented_code = []
    indent_level = 0  # Track the indentation level

    for line in lines:
        line = line.strip()

        # Detect the start of a new block with an opening brace
        if line.endswith('{'):
            indented_code.append(' ' * (indent_level * 4) + line[:-1].strip() + ':')  # Replace `{` with `:`
            indent_level += 1  # Increase the indentation level

        # Detect the end of a block with a closing brace
        elif line == '}':
            indent_level -= 1  # Decrease the indentation level

        # Handle regular lines of code
        else:
            indented_code.append(' ' * (indent_level * 4) + line)

    # Join all lines into the final code string
    return '\n'.join(indented_code)

def main():
    # Check if a file was passed as an argument
    if len(sys.argv) != 2:
        print("Usage: brace_interpreter.py <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read the curly-brace code from the file
    with open(input_file, 'r') as f:
        curly_code = f.read()

    print("Original curly-brace code:\n", curly_code)  # Print original code for debugging

    # Convert the code from curly braces to indentation
    indented_code = curly_to_indented(curly_code)

    print("\nTransformed code:\n", indented_code)  # Print transformed code

    # Write the transformed code to a file for inspection
    with open("tests/transformed_code.py", 'w') as f:
        f.write(indented_code)

    print("\nExecuting code...\n")
    
    # Using exec in a safe context
    exec(indented_code)

if __name__ == "__main__":
    main()
    
try:
    exec(indented_code)
except Exception as e:
    print(f"An error occurred while executing the code: {e}")

