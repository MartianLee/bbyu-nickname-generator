from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


setup(
    name                = 'bbyu-nickname-generator',
    version             = '0.14',
    description         = 'bbyu-nickname-generator',
    author              = 'martianlee',
    author_email        = 'martianlee@gmail.com',
    url                 = 'https://github.com/MartianLee/bbyu-nickname-generator',
    long_description='\n\n'.join((
        readme,
    )),
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['nickname', 'name', 'generator', 'nickname generator', 'bbyu'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
