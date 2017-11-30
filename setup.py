from distutils.core import setup

setup(name='infoblox',
      version='0.1.0',
      description='Infoblox Python module',
      author='Marin Atanasov Nikolov',
      author_email='dnaeon@gmail.com',
      license='BSD',
      packages=['infoblox' ],
      package_dir={'': 'src'},
      scripts=[
        'src/infoblox-cli',
      ],
      install_requires=[
        'docopt >= 0.6.1',
        'requests >= 2.2.1',
      ]
)
