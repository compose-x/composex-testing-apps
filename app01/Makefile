################################################################################
#
# {{ cookiecutter.macro_name }}
#
################################################################################

ifndef VERBOSE
.SILENT:
endif

RM			= rm -f
ECHO			= echo -e
TAG			= etags
PIP			= pip
PYTHON			= python3
SHELL			= /bin/bash
WHICH                   = /usr/bin/which
WATCH                   = /usr/bin/watch
TEST                    = /usr/bin/test
ZIP			= /usr/bin/zip

SRC			= function.py
AWS			= aws

VENV 			?= .venv
VENV_ACTIVATE		=. $(VENV)/bin/activate

STACK			:=lambda-function-{{ cookiecutter.macro_name }}
FUNCTION_NAME		:={{ cookiecutter.macro_name }}
BUCKET_NAME		:={{ cookiecutter.bucket_name }}

export VIRTUAL_ENV 	:= $(abspath ${VENV})
export PATH 		:= ${VIRTUAL_ENV}/bin:${PATH}

all			: venv build provision


${VENV}			:
			$(PYTHON) -m venv $@


venv-install		: requirements.txt | ${VENV}
			$(PIP) install -U pip
			$(PIP) install -r requirements.txt

venv-dev-install	: requirements_dev.txt | ${VENV}
			$(PIP) install --upgrade -r requirements_dev.txt


venv			:
			test -d ${VENV} || $(MAKE) venv-install
			$(VENV_ACTIVATE)
			$(WHICH) python


build			: $(VENV_ACTIVATE)
			vagrant up --parallel


provision		: $(VENV_ACTIVATE)
			$(WHICH) ansible
			vagrant provision --provision-with rproxy


.PHONY			: all venv venv-install build provision
