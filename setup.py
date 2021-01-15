import setuptools

requirements = []
with open("requirements.txt", "r") as fp:
  requirements = fp.read().splitlines()

longDesc = ""
with open("README.md", "r") as f:
  longDesc = f.read()

setuptools.setup = (
  name = "Minigames-Discord",
  version = "...", #Whyfai, Do this part
  author = [
    "Whyfai",
    "proguy914629"
  ],
  description = "...", #Whyfai
  long_description = longDesc,
  url = "https://github.com/proguy914629bot/Minigames-Discord-Edition",
  packages=setuptools.find_packages(),
  install_requires = requirements,
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ]
)
