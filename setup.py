import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle-core",
    version="1.0.0",
    author="derogab",
    author_email="derosagabriele@outlook.it",
    description="A simple tool capable of managing customized automations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/derogab/puzzle",
    license='MIT',
    package_dir={'puzzle': 'core'},
    packages=[
        'puzzle',
    ],
    install_requires=[
        'python-telegram-bot',
        'flask'
    ],
    keywords='puzzle',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)