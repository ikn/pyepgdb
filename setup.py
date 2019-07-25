import setuptools

with open('README.md', 'r') as f:
    readme_text = f.read()

setuptools.setup(
    name='pyepgdb',
    version='0',
    author='Joseph Lansdowne',
    author_email='ikn@ikn.org.uk',
    description='Python library for parsing Tvheadend epgdb files',
    long_description=readme_text,
    long_description_content_type='text/markdown',
    #url='',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)