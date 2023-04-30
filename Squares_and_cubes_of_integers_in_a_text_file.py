# Squares_and_cubes_of_integers_in_a_text_file_Marquez Francis Ivan B._BSCpE 1-5

# Squaring and cubing
def square (integer):
    return (integer*integer)

def cube (integer):
    return (integer*integer*integer)

# Read integers.txt and create squares.txt and cubes.txt
with  open("integers.txt", "r") as my_file1, open ("squares.txt", "a") as my_file2, open ("cubes.txt", "a") as my_file3:
    # Squaring loop
    for line in my_file1:
        my_file2.write(line)
    

# Append to squares.txt
# Cubing loop
# Append to cubes .txt

