import subprocess

def generate_requirements():
    try:
        # Run pip freeze command to get list of installed packages with versions
        with open("requirements.txt", "w") as f:
            subprocess.run(["pip", "freeze"], stdout=f)
        print("requirements.txt generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
generate_requirements()
