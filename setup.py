import setuptools
import steamdeck_tweaks

# with open('requirements.txt') as fh:
#     required = fh.read().splitlines()

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Steam Deck Tweaks',
    version=steamdeck_tweaks.__version__,
    author='Nicholas Dyer',
    description='A collection of different tweaks for the Steam Deck.',
    license='GNU GPL-3.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gogs.citruxx.com/nickedyer/steamdeck-tweaks',
    packages=setuptools.find_packages(),
    # https://pypi.org/classifiers/
    classifiers=[
    ],
    # install_requires=required,
    python_requires='>=3.10',
    include_package_data=True,
)
