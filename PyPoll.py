import os
import csv
dir(os)

# SECTION 3.4.1

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# import csv
# dir(csv)
# dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

# print("END OF SECTION 3.4.1")
# SECTION 3.4.2

# # Assign a variable for the file to load and the path.


# file_to_load = os.path.join("resources", "election_results.csv")

# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# election_data.close()

# with open(file_to_load) as election_data:
#      print(election_data)

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# print("END OF 3.4.2")

# # 3.4.3

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write('Counties in the election: \n')
# outfile.write('-------------\n')
# outfile.write("Arapahoe, \n")
# outfile.write("Denver, \n")
# outfile.write("Jefferson ")


# # Close the file
# outfile.close()

# print("END OF 3.4.4")

#START OF 3.4.4

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)