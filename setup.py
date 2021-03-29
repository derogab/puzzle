import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jarvis",
    version="0.1.0-beta",
    author="derogab",
    author_email="derosagabriele@outlook.it",
    description="Just A Rather Very Intelligent System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/derogab/jarvis",
    license='MIT',
    package_dir={'jarvis': 'core'},
    packages=[
        'jarvis',
    ],
    install_requires=[
        'python-telegram-bot'
    ],
    keywords='jarvis',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)