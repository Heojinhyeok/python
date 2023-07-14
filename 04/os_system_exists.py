import os
import sys

if os.path.exists(output_filename):
    print('This is overwrite the file %s. (C)ontinue or (Q)uit?' % output_filename)
    response = input('> ')
    if not response.lower().startswith('c'):
        sys.exit(0)

print("Overwrite...")
