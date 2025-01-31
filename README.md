# ubiquerg

[![Build Status](https://travis-ci.org/pepkit/ubiquerg.svg?branch=master)](https://travis-ci.org/pepkit/ubiquerg)
[![Coverage Status](https://coveralls.io/repos/github/pepkit/ubiquerg/badge.svg?branch=master)](https://coveralls.io/github/pepkit/ubiquerg?branch=master)
[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pepkit.github.io)

Ubiquerg is a utility package with a collection of helpful universally useful functions. The name means work (erg) everywhere (ubique), indicating our intention for these to be low-level functions that can be used in lots of different places. Functions are divided into groups, including:

- collection
- environment
- files
- paths
- system
- web

## Development guidelines

- Ubiquerg should have no dependencies outside of standard built-in python modules. Please do not add any functions that introduce a new dependency.
- Functions should be generic. They should perform basic, low-level processing that is not specific to a particular application.
- Functions should only be added to ubiquerg if they are used in at least 2 existing modules.
- Functions should be kept relatively small and simple (ideally <50 lines of code).


