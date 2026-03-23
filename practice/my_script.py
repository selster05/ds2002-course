import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(f"Processing file: {filename}")
else:
    print("Error: Please provide a filename")