from setuptools import setup, find_packages

setup(
    name='err',
    version='0.1',
    author='Theo Koester',
    author_email='theopkoester@icloud.com',
    description='Holds all the database files and the entire backend of our applications.',
    url='https://github.com/MNwake/cwa.git',
    packages=find_packages(),  # Update with your actual package name
    install_requires=[
        'certifi==2023.11.17',
        'dnspython==2.5.0',
        'mongoengine==0.27.0',
        'pymongo==4.6.1',
        'setuptools==69.0.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

