import subprocess


def fdesetup(action, *args):
    '''
    Wrapper around the macOS provided `fdesetup` binary. Used to manage FileVault.

    '''
    command = ['/usr/bin/fdesetup', action]
    if args:
        # Iterate through all list elements to ensure each is just a string.
        for item in args:
            if type(item) != str:
                raise ValueError('optional arguments must be strings')

        # If all list elements are strings we can safely combine it with the `command` list
        command.extend(args)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Throw an exception if stderr is returned
    if stderr:
        raise Exception(stderr)

    return stdout


def users():
    out = fdesetup('list')
    users_list = [user.split(',')[0] for user in out.split('\n')][:-1]
    return users_list


def remove_user(username):
    out = fdesetup('remove', '-user', username)
    return out


def add_user(username):
    out = fdesetup('add', '-usertoadd', username)
    return out



