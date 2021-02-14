from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='valorant-api',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/MinshuG/valorant-api',
    license='MIT',
    author='MinshuG',
    description='Python wrapper for valorant-api.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ],
    keywords=['valorant', 'valorant-api.com']
)
