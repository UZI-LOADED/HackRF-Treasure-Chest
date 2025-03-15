import os

# Base directory for Replay Attacks
base_dir = "Replay_Attacks"

# List of subdirectories to create
subdirs = [
    "Automotive", "BruteForce", "DeBruijn", "Door_Chimes", "Doorbells",
    "Fans", "Garage_Doors", "Gas_Sign", "Gates", "Handicap",
    "Lights", "Motorola", "OpenSesame", "Outlets", "Pagers",
    "Remotes", "Restaurant_Pagers", "Sprinkler_Controllers", "Thermostats", "Weather_Radios"
]

# Function to create directories and placeholder files
def create_files(base_dir, subdirs):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    for subdir in subdirs:
        path = os.path.join(base_dir, subdir)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, ".gitkeep"), 'w') as f:
            f.write("")

# Run the function
create_files(base_dir, subdirs)

print("Directories and placeholder files created.")
