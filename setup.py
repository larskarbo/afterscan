from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name='afterscan',
    description='Turn sloppy photoscans into crisp black and white images',
    long_description = long_descr,
    version='0.1.0',
    url='https://github.com/larskarbo/afterscan',
    author='Lars Karbo',
    author_email='mail@larskarbo.no',
    license='Apache2',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    packages=['afterscan'],
    install_requires=[
        'emoji',
        'Pillow',
        'click',
        'art',
        'progress'
    ],
    entry_points={
        'console_scripts': [
            'afterscan=afterscan.afterscan:main'
        ]
    },
)
