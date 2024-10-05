import os

# Create a random repository folder
repo_name = "MysteryProject"
os.makedirs(repo_name, exist_ok=True)

# Create some random files with dummy content
files_content = {
    "README.md": "# MysteryProject\n\nThis is a mysterious project. Maybe it holds secrets, maybe not.",
    "main.py": """def mystery_function():
    return "The truth is out there, but not here."

if __name__ == "__main__":
    print(mystery_function())
    """,
    "data.txt": "No secrets here, just some random data.\nMaybe...",
    ".gitignore": "# Ignore Python compiled files\n__pycache__/\n*.pyc\n",
    "config.json": """{
    "name": "MysteryProject",
    "version": "1.0.0",
    "description": "A project full of mystery."
}"""
}

# Create the files in the repository
for file_name, content in files_content.items():
    with open(os.path.join(repo_name, file_name), 'w') as file:
        file.write(content)

# Zip the repository for user to download
import shutil
shutil.make_archive(repo_name, 'zip', repo_name)

repo_name + ".zip"
