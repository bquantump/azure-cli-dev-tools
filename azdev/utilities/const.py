# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

import sys

DEFAULT_RESULT_FILE = 'test_results.xml'
COMMAND_MODULE_PREFIX = 'azure-cli-'
EXTENSION_PREFIX = 'azext_'
EXT_REPO_NAME = 'azure-cli-extensions'
IS_WINDOWS = sys.platform.lower() in ['windows', 'win32']
CONFIG_NAME = 'config'
ACTIVATE_PS = 'Activate.ps1'
PS1_VENV_SET = '$env:VIRTUAL_ENV'
SCRIPTS = 'Scripts'
VIRTUAL_ENV = 'VIRTUAL_ENV'
VENV_CMD = 'python -m venv --system-site-packages '
VENV_CMD3 = 'python3 -m venv --system-site-packages '
AZ_CONFIG_DIR = 'AZURE_CONFIG_DIR'
AZ_AZDEV_DIR = 'AZDEV_CONFIG_DIR'
AZ_DEV_SRC = 'dev_sources'
AZ_CLOUD = 'AzureCloud'
CLOUD_SECTION = 'cloud'
EXT_SECTION = 'extension'
CLI_SECTION = 'clipath'
EVN_AZ_CONFIG = '$env:AZURE_CONFIG_DIR'
EVN_AZ_DEV_CONFIG = '$env:AZDEV_CONFIG_DIR'
PIP_E_CMD = 'pip install -e '
PIP_R_CMD = 'pip install -r '
AUTO_REST_CMD = 'autorest --az --azure-cli-extension-folder='
UN_BIN = 'bin'
UN_ACTIVATE = 'activate'
UN_EXPORT = 'export'
BAT_ACTIVATE = 'activate.bat'
BASH_EXE = '/bin/bash'
GITHUB_SWAGGER_REPO_URL = 'https://github.com/Azure/azure-rest-api-specs'
GITHUB_API_SWAGGER_REPO_URL = 'https://api.github.com/repos/Azure/azure-rest-api-specs'
SWAGGER_REPO_NAME = 'azure-rest-api-specs'
SHELL = 'SHELL'
BASH_NAME_WIN = 'bash.exe'

ENV_VAR_TEST_MODULES = 'AZDEV_TEST_TESTS'               # comma-separated list of modules to test
ENV_VAR_VIRTUAL_ENV = ['VIRTUAL_ENV', 'CONDA_PREFIX']   # used by system to identify virtual environment
ENV_VAR_TEST_LIVE = 'AZURE_TEST_RUN_LIVE'               # denotes that tests should be run live instead of played back
