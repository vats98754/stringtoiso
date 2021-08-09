from distutils.core import setup
setup(
  name = 'stringtoiso',
  packages = ['stringtoiso'],
  version = '0.2',
  license='MIT',
  description = 'A library that converts string inputs representing languages like "Spanish" into their ISO-639 code equivalents.',
  long_description = '''# stringtoiso
## _The first String to ISO-code Converter_

This is a package, uploaded on PyPI by anvayvats, to convert an input string representing a language (like 'Spanish') into its ISO-639-X code equivalent. For now, the system only converts to ISO-639-1, ISO-639-2B, ISO-639-2T, ISO-639-3, but the goal is to expand this package to support ISO-X-X. This package:

- Scraped a spreadsheet of standardized nomenclature used to classify all known languages.
- Created dictionaries for each language's string representation to the ISO-639-1, ISO-639-2B, ISO-639-2T, ISO-639-3 codes.
- All key-value pairs were corrected and synonyms were added (e.g. "Persian": "fa" and "Farsi": "fa" were both included).
- This is very useful for different libraries in Python that have functions requiring an ISO code as a parameter.

## Features

- Import the module to use the 'convert' function with parameters 'isoType' and 'langName', where 'isoType' (parameter of type string or int) is the type of ISO code you want, and 'langName' (parameter of type string) is the name of the language for which you want to find the correponding ISO code. 
- As of the release of v0.1, only isoType='1', isoType='2B', isoType='2T', and isoType='3' are supported. As for languages, all those mentioned by the International Organization for Standardization (ISO) are included in this package.

## Tech

And, of course, stringtoiso itself is open source with a [public repository](https://github.com/vats98754/stringtoiso) on GitHub.

## Installation

stringtoiso requires Python 2.7 or Python 3.x to run, and has no dependencies.

To install the module, use pip through the command line (or terminal on Mac):

```sh
pip install stringtoiso
```

If you have not already installed pip, check [webpage](https://pip.pypa.io/en/stable/installation/) to do so.

## Plugins

As of now, this module has no plugins.

## Development

Want to contribute? This is an open-source project to which anyone can contribute, but seeing as the module is not very advanced, those without Python expertise can join.

## MIT License
Copyright (c) 2021 Anvay Vats
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  ''',
  author = 'Anvay Vats',
  author_email = 'vats98754@gapps.uwcsea.edu.sg',
  url = 'https://github.com/vats98754/stringtoiso/',
  download_url = 'https://github.com/vats98754/stringtoiso/archive/refs/tags/v_02.tar.gz',
  keywords = ['ISO-639-1', 'ISO-639-2B', 'ISO-639-2T', 'ISO-639-3', 'ISO-639', 'ISO', 'converter', 'string', 'gTTS'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
