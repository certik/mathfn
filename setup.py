from setuptools import setup, find_packages


setup(
    name='mathfn',
    version='0.1',
    license='MIT',
    author="Ondřej Čertík",
    author_email='ondrej@certik.us',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/certik/mathfn',
    keywords='fast math functions lpython',
    install_requires=[
      ],
)
