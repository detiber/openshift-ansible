''' pytest local conftest plugin '''


def pytest_ignore_collect(path):
    ''' pytest_ignore_collect hook to avoid recursing into symlink directories '''
    if path.islink():
        return True
    return False
