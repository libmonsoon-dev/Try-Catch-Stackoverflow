import webbrowser
from sys import version_info
VERSION = version_info[0]


def stackoverflow_search(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            webbrowser.open(
                "https://stackoverflow.com/search?q=python{0} {1}".format(
                    VERSION, e
                )
            )
            raise e
    return wrapper


if __name__ == '__main__':

    @stackoverflow_search
    def test(a, b):
        return a / b

    test(1, 0)
