import subprocess
from os import uname
from sys import platform
import re

try:
    import winregistry as winregistry_lib
except ImportError:
    winregistry_lib = None


def run_native_command(cmd: str) -> str:
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding='utf-8') \
            .stdout \
            .strip()
    except subprocess.SubprocessError:
        return None


def retrieve_registry_key_value(key_name: str, value_name: str) -> str:
    if winregistry_lib is None:
        return None
    try:
        with winregistry_lib.open_value(key_name, value_name) as reg:
            if reg.data and isinstance(reg.data, str):
                return reg.data.strip()
    except OSError:
        pass
    return None


def read_from_file(path: str) -> str:
    try:
        with open(path) as f:
            return f.read().strip()
    except IOError:
        return None

def sanitize_machine_id(id: str) -> str:
  return re.sub(r'[\x00-\x1f\x7f-\x9f\s]', '', id).strip()


def identify_machine() -> str:
    """
    machine_id returns the platform specific device GUID of the current host OS.
    """

    winregistry = winregistry_lib is not None

    machine_id = None
    if platform == 'darwin':
        machine_id = run_native_command(
            "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'")

    elif platform in ('win32', 'cygwin', 'msys'):
        if winregistry:
            machine_id = retrieve_registry_key_value(r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography',
                                                     'MachineGuid')
        else:
            machine_id = run_native_command(
                "powershell.exe -ExecutionPolicy bypass -command (Get-CimInstance -Class Win32_ComputerSystemProduct).UUID")
        if not machine_id:
            machine_id = run_native_command('wmic csproduct get uuid').split('\n')[2] \
                .strip()

    elif platform.startswith('linux'):
        machine_id = read_from_file('/var/lib/dbus/machine-id')
        if not machine_id:
            machine_id = read_from_file('/etc/machine-id')
        if not machine_id:
            cgroup = read_from_file('/proc/self/cgroup')
            if cgroup and 'docker' in cgroup:
                machine_id = run_native_command('head -1 /proc/self/cgroup | cut -d/ -f3')
        if not machine_id:
            mount_info = read_from_file('/proc/self/mountinfo')
            if mount_info and 'docker' in mount_info:
                machine_id = run_native_command(
                    "grep -oP '(?<=docker/containers/)([a-f0-9]+)(?=/hostname)' /proc/self/mount_info")
        if not machine_id and 'microsoft' in uname().release:  # wsl
            machine_id = run_native_command(
                "powershell.exe -ExecutionPolicy bypass -command '(Get-CimInstance -Class Win32_ComputerSystemProduct).UUID'")

    elif platform.startswith(('openbsd', 'freebsd')):
        machine_id = read_from_file('/etc/hostid')
        if not machine_id:
            machine_id = run_native_command('kenv -q smbios.system.uuid')

    if not machine_id:
        raise RuntimeError('failed to obtain machine_id on platform {}'.format(platform))

    return sanitize_machine_id(machine_id)

if __name__ == "__main__":
    print(identify_machine())