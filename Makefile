# -*- mode:makefile; coding:utf-8 -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

all:
	@echo "Nothing to do for target all"

develop:
	pip install -e .[dev] --upgrade --upgrade-strategy eager
	python setup.py develop

clean:
	$(RM) $(shell find . -name "*~")
	$(RM) -r $(shell find . -type d -name "__pycache__")

clean-all: clean
	$(RM) -r *.egg-info docs doc-source/_build dist
	$(RM) doc-source/ilcli.*rst doc-source/modules.rst

tests:
	pytest --cov ilcli test -v

lint:
	flake8

wheel:
	$(RM) -r dist
	python3 setup.py sdist bdist_wheel

doc:
	# Build the API docs from the source code - overwrites those
	# files, which are ignored by git
	sphinx-apidoc -o doc-source ilcli
	sphinx-build doc-source docs
