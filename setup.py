from setuptools import setup, find_packages

setup(
    name='k-SchoolMeal',
    version='1.1.0 Alpha',

    description='school meal data',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',


    author='EGGnmad',
    author_email='viewnono1219@gmail.com',

    url='https://github.com/EGGnmad/K-SchoolMeal',
    download_url='https://github.com/EGGnmad/K-SchoolMeal',
    install_requires = ['aiohttp', 'python-dotenv'],

    packages=find_packages(),
    include_package_data= True,
    keywords=['korea', 'school meal'],
    python_requires = '>=3.7',
)