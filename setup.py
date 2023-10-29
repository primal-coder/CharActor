from setuptools import setup, find_packages

setup(
    name='CharActor',
    version='0.1.0',
    description='A module for creating and managing rpg characters.',
    author='James Evans',
    author_email='joesaysahoy@gmail.com',
    url='https://github.com/primal-coder/CharActor',
    packages=find_packages(),
    install_requires=['dicepy'],
    python_requires='>=3.8',
    keywords=[
        'rpg', 'character', 'dnd', 'd&d', 'dungeons and dragons', 
        'dungeons & dragons', 'player character', 'actor', 'charactor'
        ]
)