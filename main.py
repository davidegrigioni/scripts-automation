# ! New Version 2.0  By Daniele Colucci ( AKA Py-Moon )

import os
import pathlib


class PayLoads:
    npm_depends: str = """
npm init -y
npm install -D tailwindcss
npx tailwindcss init
npm install --save-dev webpack
npm install --save-dev webpack-cli
"""
    html_template: str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
"""
    css_template: str = """
@tailwind base;
@tailwind components;
@tailwind utilities;
"""
    paste: str = """
npx tailwindcss -i .\public\css\input.css -o .\dist\css\style.css --minify
"""


class App:
    def __init__(self):

        path = pathlib.Path(__file__).parent.resolve()

        self.create_folder(fr'{path}\dist')
        self.create_folder(fr'{path}\dist\html')
        self.create_folder(fr'{path}\dist\css')
        self.create_folder(fr'{path}\dist\js')
        self.create_folder(fr'{path}\public')
        self.create_folder(fr'{path}\public\html')
        self.create_folder(fr'{path}\public\css')
        self.create_folder(fr'{path}\public\js')
        self.create_file(fr'{path}\public\html\index.html', PayLoads.html_template)
        self.create_file(fr'{path}\public\css\input.css', PayLoads.css_template)
        self.exc(PayLoads.npm_depends)

        print('Commands: '
              f'Tailwind: npx tailwindcss -i {path}\public\css\input.css -o {path}\dist\css\style.css --minify'
              'Copied to clipboard')

    @staticmethod
    def create_folder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print(f'Error: Creating directory. {directory}')

    @staticmethod
    def create_file(fname: str, fcont: str):
        with open(fname, 'w') as f:
            for _ in fcont:
                f.write(_)

    @staticmethod
    def exc(cmd: str):
        os.system(cmd)


if __name__ == '__main__':
    App()
