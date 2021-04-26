from setuptools import setup, find_packages

with open('README.md') as file_readme:
    README = file_readme.read()

setup_args = dict(
    name='sutree',
    version='0.2.0',
    description='Tree data structure library',
    long_description_content_type="text/markdown",
    long_description=README + '\n',
    license='3-Clause BSD License',
    packages=find_packages(exclude=['*test.*', '*test']),
    author='Thanh Trung Nguyen',
    author_email='thanh.it1995@gmail.com',

    keywords=['tree', 'binary', 'avl', 'bst',
              'display', 'view', 'print', 'visualize', 'visualization', 'ascii', 'console', 'terminal'],

    url='https://github.com/thanhit95/sutree',
    download_url='https://pypi.org/project/sutree'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
