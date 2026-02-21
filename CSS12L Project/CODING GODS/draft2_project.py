import csv
import os

filename = "materials.csv"

materials = {}

def load_from_csv():

	if os.path.exists(filename):

		file = with open(filename, "r")
		reader = csv.reader(file)

		next(reader, None)

		for row in reader:
			name = row[0].capitalize()
			tensile_strength = int(row[1])
			materials[name] = tensile_strength

def save_to_CSV():

	file = with open(filename, "w")

	writer = csv.writer(file)

	writer.writerow(["Material", "Tensile Strength"])

	for name in materials:
		writer.writerow([name.capitalize(), materials[name]])

def add_material():

    name = input("Material name: ")

    if name in materials:
        print("Material already exists.")
        x = input("Do you want to update it? (yes/no): ")
        if x.lower() == "yes":
        	update_material()
        else:
        	return

    tensile_strength = int(input("Tensile Strength (MPa): "))

    materials[name] = tensile_strength

    print("Material added successfully!")

def view_strongest_material():

    strongest = max(materials, key=materials.get)

    print(f'Strongest material: {strongest} ({materials[strongest]} MPa)')

def update_material():

    name = input("Enter material name to update: ")

    if name.capitalize() in materials:

        new_strength = int(input("Enter new tensile strength (MPa): "))
        materials[name.capitalize()] = new_strength

        print("Material updated successfully.")

    else:
        print("Material not found.")

def delete_material():

    name = input("Material the material to delete: ")

    if name.capitalize() in materials:
        del materials[name.capitalize()]
        print("Deleted.")

    else:
        print("Material not found.")

def display_all_materials():

    if len(materials) == 0:
        print("No materials found.")
        return

    print("\nAll Materials:")
    for name in materials:
        print(name, "-", materials[name], "MPa")

def display_menu():
    print('''
    	=== Material Strength Calculator ===
		1. Add Material
		2. View Strongest Material
		3. Update Material
		4. Delete Material
		5. Display All Materials
		6. Save to CSV
		7. Load from CSV
		8. Exit
		''')

load_data()
while True:

	display_menu()
	choice = int(input("Enter your choice: "))

	match(choice):
		    case 1:
		        add_material()

		    case 2:
		        show_strongest()

		    case 3:
		    	update_material()

		    case 4:
		    	delete_material()

		    case 5:
		        show_all()

		    case 6:
		        save_data()
		        print("Data saved.")

		    case 7:
		    	load_data()
		    	print("Data successfully loaded. Displaying contents sorted by name:\n")
		    	sorted_materials = sorted(materials.items())
		    	print("Material".ljust(20), "Tensile Strength (MPa)")
		    	print("-" * 45)
		    	for name, strength in sorted_materials:
		    		print(name.ljust(20), strength)

		    case 8:
		    	answer = input("Would you like to save before exiting? (yes/no): ")

		    	if answer.lower() == "yes":
		    		print("Saving to materials.csv...")
		    		save_data()
		    		print("Data successfully saved to CSV.")
		    		print("Exiting program. Goodbye!")
		    		break
		    case _:
		        print("Invalid choice.")
