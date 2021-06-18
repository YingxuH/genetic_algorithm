import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name = 'genetic_algorithm',
  packages = ['genetic_algorithm'],
  version = '0.2.2',
  license='MIT',
  description = 'A python package implementing the genetic algorithm',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'He Yingxu',
  author_email = 'yingxu.he1998@gmail.com',
  url = 'https://github.com/YingxuH/genetic_algorithm',
  download_url = 'https://github.com/YingxuH/genetic_algorithm/archive/0.2.2.tar.gz',
  keywords = ['genetic algorithm', 'machine learning'],
  install_requires = [
    "numpy",
    "pandas"
  ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)