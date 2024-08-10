from setuptools import setup, find_packages

with open("README.md", "r") as f:
    decription = f.read()

setup(
    name="SuperTerminal",  # Replace with your package name
    version="1.0.0",        # Replace with your package version
    author="Kiarash Karami",    # Replace with your name
    author_email="Kiarash_Karami@outlook.com",  # Replace with your email
    description="Natural Language to Terminal Command Translator.",  # Replace with a short description
    long_description=decription,
    long_description_content_type="text/markdown",  # Keep as is
    url="https://github.com/Kiarash-Karami/SuperTerminal",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Keep as is
    entry_points={
        "console_scripts": [
            "SuperTerminal=SuperTerminal.main:main",  # Replace with your package name and entry point
        ],
    },
    install_requires=[
        "groq",  # Add your dependencies here
    ],
    python_requires=">=3.6",  # Replace with the minimum required Python version
)
