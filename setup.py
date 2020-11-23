from setuptools import setup, find_packages

setup(
  name='ctf_server',
  version='0.1',
  long_description='im a haxxor',
  packages=['ctf-server'],
  include_package_data=True, #Looks for MANIFEST.in file which tracks static data
  zip_safe=False,
  install_requires=find_packages()
)
