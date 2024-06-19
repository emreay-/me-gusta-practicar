from setuptools import setup, find_packages

setup(
    name='me_gusta_practicar',
    version='0.1.0',
    author='Emre Ay',
    author_email='your.email@example.com',
    description='A Python project for practicing Spanish',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/emreay-/me-gusta-practicar',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={
        'me_gusta_practicar': ['assets/*'],
    },
    include_package_data=True,
    install_requires=[
        "pygame"
    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage',
            'openai'
        ],
    },
    entry_points={
        'console_scripts': [
            'me_gusta_practicar=me_gusta_practicar.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
