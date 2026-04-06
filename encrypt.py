import sys
from utils import encrypt_file

if len(sys.argv) != 4:
    print("Usage: python encrypt.py <input_file> <output_file> <password>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
password = sys.argv[3]

encrypt_file(input_file, output_file, password)