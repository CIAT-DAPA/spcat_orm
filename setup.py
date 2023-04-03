from setuptools import setup, find_packages

setup(
    name="ormgap",
    version='v1.0.0',
    author="victor-993",
    author_email="v.hernandez@cgiar.com",
    description="ORM para la base de datos de gap analysis",
    url="https://github.com/CIAT-DAPA/spcat_orm",
    download_url="https://github.com/CIAT-DAPA/spcat_orm",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='mongodb orm gap-analysis',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine==0.26.0"
    ]
)
