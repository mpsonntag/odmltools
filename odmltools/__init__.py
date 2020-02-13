from sys import version_info

if version_info.major < 3 or version_info.major == 3 and version_info.minor < 6:
    print("WARNING: The odMLtools package is not tested with your Python version. "
          "Please consider upgrading to the latest Python distribution.")
