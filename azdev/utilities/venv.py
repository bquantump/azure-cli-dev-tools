import azdev.utilities.const as const
import os
import subprocess


def validate_env():
    if not os.environ.get(const.VIRTUAL_ENV):
        raise RuntimeError("You are not running inside a virtual enviromet")
    if not os.environ.get(const.AZ_CONFIG_DIR):
        raise RuntimeError(
            "AZURE_CONFIG_DIR env var is not set. Please rerun setup")
    if not os.path.exists(os.path.join(os.environ[const.AZ_CONFIG_DIR], "config")):
        raise RuntimeError(
            "The Azure config file does not exist. please rerun setup")


def edit_activate(azure_config_path, dot_azure_config, dot_azdev_config):
    if const.IS_WINDOWS:
        ps1_edit(azure_config_path, dot_azure_config, dot_azdev_config)
        bat_edit(azure_config_path, dot_azure_config, dot_azdev_config)
    else:
        unix_edit(azure_config_path, dot_azure_config, dot_azdev_config)


def unix_edit(azure_config_path, dot_azure_config, dot_azdev_config):
    activate_path = os.path.join(azure_config_path, const.UN_BIN,
                                 const.UN_ACTIVATE)
    content = open(activate_path, "r").readlines()

    # check if already ran setup before
    if const.AZ_CONFIG_DIR not in content[0]:
        content = [const.AZ_CONFIG_DIR + '=' + dot_azure_config + '\n',
                   const.UN_EXPORT + ' ' + const.AZ_CONFIG_DIR + '\n',
                   const.AZ_AZDEV_DIR + '=' + dot_azdev_config + '\n',
                   const.UN_EXPORT + ' ' + const.AZ_AZDEV_DIR] + content
        with open(activate_path, "w") as file:
            file.writelines(content)


def bat_edit(azure_config_path, dot_azure_config, dot_azdev_config):
    activate_path = os.path.join(azure_config_path, const.SCRIPTS,
                                 const.BAT_ACTIVATE)
    content = open(activate_path, "r").readlines()
    if const.AZ_CONFIG_DIR not in content[1]:
        content = content[0:1] + ['set ' + const.AZ_CONFIG_DIR +
                                  '=' + dot_azure_config + '\n',
                                  'set ' + const.AZ_AZDEV_DIR + 
                                  '=' + dot_azdev_config] + content[1::]
        with open(activate_path, "w") as file:
            file.writelines(content)


def ps1_edit(azure_config_path, dot_azure_config, dot_azdev_config):
    activate_path = os.path.join(azure_config_path, const.SCRIPTS,
                                 const.ACTIVATE_PS)
    content = open(activate_path, "r").read()
    idx = content.find(const.PS1_VENV_SET)
    if idx < 0:
        raise RuntimeError("hmm, it looks like " + const.ACTIVATE_PS + " does"
                           " not set the virutal enviroment variable VIRTUAL_ENV")
    if content.find(const.EVN_AZ_CONFIG) < 0:
        content = content[:idx] + const.EVN_AZ_CONFIG + " = " + \
            "\"" + dot_azure_config + "\"; " + \
            const.EVN_AZ_DEV_CONFIG + " = " + \
            "\"" + dot_azdev_config + "\"; " + \
            content[idx:]
    with open(activate_path, "w") as file:
        file.write(content)


def install_cli(cli_path, venv_path):
    venv_path = os.environ[const.VIRTUAL_ENV] = venv_path
    src_path = os.path.join(cli_path, 'src')
    activate_path = os.path.join(venv_path, 'Scripts', 'activate') if const.IS_WINDOWS else 'source ' + os.path.join(
        venv_path, const.UN_BIN, const.UN_ACTIVATE)
    delimiter = ' && ' if const.IS_WINDOWS else '; '
    executable = None if const.IS_WINDOWS else const.BASH_EXE
    print("\nactivate path is " + str(activate_path))
    subprocess.call(activate_path + delimiter +
                    'pip install azure-common', shell=True, executable=executable)
    subprocess.call(activate_path + delimiter + const.PIP_E_CMD +
                    os.path.join(src_path, 'azure-cli-nspkg'), shell=True, executable=executable)
    subprocess.call(activate_path + delimiter + const.PIP_E_CMD +
                    os.path.join(src_path, 'azure-cli-telemetry'), shell=True, executable=executable)
    subprocess.call(activate_path + delimiter + const.PIP_E_CMD +
                    os.path.join(src_path, 'azure-cli-core'), shell=True, executable=executable)
    subprocess.call(activate_path + delimiter + const.PIP_E_CMD +
                    os.path.join(src_path, 'azure-cli'), shell=True, executable=executable)
    subprocess.call(activate_path + delimiter + const.PIP_E_CMD +
                    os.path.join(src_path, 'azure-cli-testsdk'), shell=True, executable=executable)