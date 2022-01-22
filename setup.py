from setuptools import setup, find_packages
import valorant_api

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='valorant-api',
    version=valorant_api.__version__,
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=["python-dateutil", "aiohttp", "requests", "Pillow"],
    keywords=['valorant', 'valorant-api.com']
)
