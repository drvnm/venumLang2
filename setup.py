from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="venumLang",
        version="0.1.0",
        author="Venumlang contributors",
        packages=find_packages(exclude=["test"]),
    )