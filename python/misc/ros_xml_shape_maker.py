#! /usr/bin/python3


validity = "Not a valid answer, try again." #The answer validity message:

#Names of the measurements for the shapes:
solid_sphere = ["mass", "radius"]
solid_cuboid = ["mass", "width", "height", "depth"]
solid_cylinder = ["mass", "radius", "height"]

whole_objects = [] #List to lists of variables needed for each link:

#Loop to allow as many links to be created as the user wants.
while True:
    measurements = [] #List to hold measurements for chosen shape:

    #Loop to ask for link name until a valid answer is given. If answer is not valid print validity message and ask again.
    while True:
        link_name = str(input("what will be the link name, link name should start with link_ : "))
        if link_name[:5] == "link_":
            break

        else:
            print(validity)
            continue

    #Loop for asking for shape and checking if answer is valid. If answer is not valid then print validity message and ask again.
    while True:
        acceptable_shapes = {1: "Solid sphere",
                            2: "Solid cuboid",
                            3: "Solid cylinder "}

        shape = int(input("""What shape you want to use:
                      1 = Solid sphere
                      2 = Solid cuboid
                      3 = Solid cylinder """))

        #Check if shape is in the dictionary of acceptable shapes
        if shape in acceptable_shapes.keys():
            break

        else:
            print(validity)
            continue

    #Determine the variable: asked_values , depending on chosen shape.
    if "sphere" in acceptable_shapes[shape]:
        asked_values = solid_sphere

    elif "cuboid" in acceptable_shapes[shape]:
        asked_values = solid_cuboid

    else:
        asked_values = solid_cylinder


    shape_values = (', '.join(asked_values)) #Variable to be used in telling the user what measurements they will need to give depending on the shape.
    chosen_shape = acceptable_shapes[shape] #The shape in string form is assigned to variable chosen_shape

    #Due to a weird thing in code runner, the space at the end of Solid sylinder needs to be taken off at this point.
    #Tell used which chape they chose and the measurements they will need to give.
    if chosen_shape == "Solid cylinder ":
        print(f"you choosed {chosen_shape[:-1]}, give: {shape_values}")
    
    else:
        print(f"you choosed {chosen_shape}, give: {shape_values}")

    #A loop in which measurements are asked and appended to the measurements list. If the answer is not a float validity message is printed and user will need to try again.
    counter = 0
    while True:
        try:
            if counter == len(asked_values):
                break

            else:
                ask_measures = float(input(f"now give, {asked_values[counter]} as decimal number: "))
                measurements.append(ask_measures)
                counter = counter + 1
        
        except ValueError:
            print(validity)
            continue

    #Functions to calculate the inertia. The variable names are the same in each function and are made global for convenience
    def get_sphere_inertia_matrix(mass, radius):
        global ixx, iyy, izz, ixy, ixz, iyz
        ixx = iyy = izz = (2.0 / 5.0) * radius**2 * mass
        ixy = 0.0
        ixz = 0.0
        iyz = 0.0

    def get_cube_inertia_matrix(mass, width, height, depth):
        global ixx, iyy, izz, ixy, ixz, iyz
        ixx = (1.0 / 12.0) * (height**2 + depth**2) * mass
        iyy = (1.0 / 12.0) * (width**2 + depth**2) * mass
        izz = (1.0 / 12.0) * (width**2 + height**2) * mass
        ixy = 0.0
        ixz = 0.0
        iyz = 0.0

    def get_cylinder_inertia_matrix(mass, radius, height):
        global ixx, iyy, izz, ixy, ixz, iyz
        ixx = (1.0 / 12.0) * (3.0 * radius**2 + height**2) * mass
        iyy = (1.0 / 12.0) * (3.0 * radius**2 + height**2) * mass
        izz = (1.0 / 2.0) * radius**2 * mass
        ixy = 0.0
        ixz = 0.0
        iyz = 0.0
 
    if chosen_shape == "Solid sphere":
        get_sphere_inertia_matrix(measurements[0], measurements[1]) #Call function get_sphere_inertia_matrix using the list: measurements index.
        whole_objects.append([chosen_shape, link_name, measurements[0], measurements[1], ixx, ixy, ixz, iyy, iyz, izz]) #Append all relevant information as a list to the already existing list: whole_objects

    elif chosen_shape == "Solid cuboid":
        get_cube_inertia_matrix(measurements[0], measurements[1], measurements[2], measurements[3])
        whole_objects.append([chosen_shape, link_name, measurements[0], measurements[1], measurements[2], measurements[3], ixx, ixy, ixz, iyy, iyz, izz])

    else:
        get_cylinder_inertia_matrix(measurements[0], measurements[1], measurements[2])
        whole_objects.append([chosen_shape, link_name, measurements[0], measurements[1], measurements[2], ixx, ixy, ixz, iyy, iyz, izz]) 

    #Ask user if they want to quit or not. If answer is not yes or no, then print validity message.
    while True:
        ask_another = str(input("Do you want to quit, then answer yes if you want to continue answer no: "))
        if ask_another == "yes":
            break

        elif ask_another == "no":
            break

        else:
            print(validity)
            continue

    if ask_another == "no":
        continue

    else:
        break

#Ask for filename as string. If the last 4 characters of string are not .xml then print validity message and try again.
while True:
    filename = input("give a filename where to save, use .xml ending for filename: ")
    if filename[-4:] == ".xml":
        break

    else:
        print(validity)
        continue
    
#Creating variables holding string to be used to put the file together.
for i in whole_objects:
    if i[0] == "Solid sphere":
        geometry = f'<sphere radius="{i[3]}"/>'
        inertia = f'<inertia ixx="{i[4]}" ixy="{i[5]}" ixz="{i[6]}" iyy="{i[7]}" iyz="{i[8]}" izz="{i[9]}"/>'

    elif i[0] == "Solid cuboid":
        geometry = f'<box size="{i[5]} {i[3]} {i[4]}"/>'
        inertia = f'<inertia ixx="{i[6]}" ixy="{i[7]}" ixz="{i[8]}" iyy="{i[11]}" iyz="{i[10]}" izz="{i[9]}"/>'

    else:
        geometry = f'<cylinder length="{i[4]}" radius="{i[3]}"/>'
        inertia = f'<inertia ixx="{i[5]}" ixy="{i[6]}" ixz="{i[7]}" iyy="{i[8]}" iyz="{i[9]}" izz="{i[10]}"/>'
        
    #Append to the file which name was given by the user. Indexing and previously made variables are used in f string to put everything into the file at once.
    f = open(filename, "a")
    f.write(f"""    
    <link name="{i[1]}">
      <inertial>
        <mass value="{i[2]}"/>
        {inertia}
      </inertial>
      <visual>
        <geometry>
          {geometry}
        </geometry>
      </visual>
      <collision>
        <geometry>
          {geometry}
        </geometry>
      </collision>
    </link>""")
    f.close()

