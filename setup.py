import setuptools

install_requires = []

setuptools.setup(
    name="demo_lib",
    version="0.1.0",
    author="",
    author_email="",
    url="",
    description="",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={"demo_lib": []},
    install_requires=install_requires,
)
