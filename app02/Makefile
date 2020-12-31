################################################################################
#
# app02
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

ACCOUNT_ID		:=$(aws sts get-caller-identity | jq -r .Account)

VENV 			?= .venv
VENV_ACTIVATE		=. $(VENV)/bin/activate

FUNCTION_NAME		:=app02
REPO_NAME		:=blog-app-02

export VIRTUAL_ENV 	:= $(abspath ${VENV})
export PATH 		:= ${VIRTUAL_ENV}/bin:${PATH}

all			: venv build provision

account			:
			echo $(ACCOUNT_ID)


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

rproxy			:
			$(DOCKER) build -t Dockerfile.rproxy .



build			: rproxy app


publish			:
			$(DOCKER) push 


.PHONY			: all venv venv-install build provision
