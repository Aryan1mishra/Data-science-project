from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements

setup( 
    name='Data science project',
    version='0.1',
    author='Aryan',
    description='My first data science end to end professional project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)