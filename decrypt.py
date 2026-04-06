import sys
from utils import decrypt_file

if len(sys.argv) != 4:
    print("Usage: python decrypt.py <input_file> <output_file> <password>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
password = sys.argv[3]

decrypt_file(input_file, output_file, password)