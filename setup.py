from setuptools import setup, find_packages

setup(name='handcash_connect_sdk',
      version='0.1.0',
      description='handcash_connect_sdk - library for interacting with Handcash Connect API',
      long_description='This library allows you to authorize with Handcash Cloud server and use Handcash Connect API '
                       'in order to get user\'s info and do payments on behalf of user\'s wallet.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
      ],
      keywords='api handcash',
      url='https://github.com/krzysiekfonal/handcash-connect-sdk-python',
      author='Krzysztof Fonal',
      author_email='krzysiek.fonal@gmail.com',
      license='The Unlicense',
      packages=find_packages(exclude=("tests",)),
      install_requires=[
          'bitcoinx', 'request'
      ],
      zip_safe=True)