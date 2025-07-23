from setuptools import setup, find_packages,setup
from typing import List

Hyphen_E_Dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    :param file_path: str: Path to the requirements file.
    :return: List[str]: List of package names.
    """
    
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

    if Hyphen_E_Dot in requirements:
        requirements.remove(Hyphen_E_Dot)
    return requirements

setup(
    name='Cab_Cancellation_predict',
    version='0.0.1',
    author='Vaibhav Arya',
    author_email='vkarya711@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
    