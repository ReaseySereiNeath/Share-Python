import os
import sys
import platform


class SystemInfo:
    @staticmethod
    def script_name():
        return os.path.basename(sys.argv[0])

    @staticmethod
    def python_path():
        return sys.executable

    @staticmethod
    def python_version():
        return sys.version

    @staticmethod
    def platform():
        return platform.system()
