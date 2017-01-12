from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='py_win_keyboard_layout',
      version='0.1',
      description='Interaction with keyboard layout on windows',
      long_description=readme(),
      classifiers=[
                  'Development Status :: 3 - Alpha',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 3.5',
                  'Environment :: Win32 (MS Windows)',
                  'Operating System :: Microsoft :: Windows :: Windows 7',
                  'Topic :: Utilities',
                  'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='windows keyboard layout language',
      url='http://github.com/Lex98/py_win_keyboard_layout',
      author='Lex98',
      license='MIT',
      packages=['py_win_keyboard_layout'],
      install_requires=[
          'pywin32',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      zip_safe=False)
