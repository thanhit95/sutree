from setuptools import setup, find_packages

with open('README.md') as file_readme:
    README = file_readme.read()

setup_args = dict(
    name='pytreedisplay',
    version='1.0.0',
    description='A utility help visualize binary trees by using ASCII text',
    long_description_content_type="text/markdown",
    long_description=README + '\n',
    license='3-Clause BSD License',
    packages=find_packages(exclude=['*test.*', '*test']),
    author='Thanh Trung Nguyen',
    author_email='thanh.it1995@gmail.com',
    keywords=['tree', 'display', 'view', 'print', 'visualize', 'visualization', 'ascii', 'terminal', 'binary'],
    url='https://github.com/thanhit95/pytree',
    download_url='https://pypi.org/project/pytreedisplay'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
