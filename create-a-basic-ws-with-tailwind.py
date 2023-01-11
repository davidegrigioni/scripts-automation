# Create a Website with TailwindCSS VERSION 0.1 by Davide Grigioni
import os
import subprocess

# Initialize a package.json
subprocess.check_call('npm init -y', shell=True)

# Install TailwindCSS + Create tailwind.config.js
subprocess.check_call('npm install -D tailwindcss', shell=True)
subprocess.check_call('npx tailwindcss init', shell=True)

# Create an input.css to Inject Tailwind directives
with open('input.css', 'w') as f:
    f.write('@tailwind base;\n')
    f.write('@tailwind components;\n')
    f.write('@tailwind utilities;')
    
# Create a /css dir
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder('./css/')

# Run a TailwindCSS minified version for optimization

subprocess.check_call('npx tailwindcss -i ./input.css -o ./css/style.css --minify', shell=True)

# Inject a basic index.html
with open('index.html', 'w') as f:
    f.writelines(["<!doctype html>\n", "<html>\n", "<head>\n"])