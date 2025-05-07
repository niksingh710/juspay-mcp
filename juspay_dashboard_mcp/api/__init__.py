# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

import os
import glob

# Determine the package directory (the directory containing this __init__.py)
package_dir = os.path.dirname(__file__)

# Build a list of Python module files in the directory
modules = glob.glob(os.path.join(package_dir, "*.py"))

# Construct __all__ by iterating through the module file names
__all__ = []
for module in modules:
    module_name = os.path.basename(module)[:-3]  # Remove the .py extension
    if module_name != "__init__":
        __all__.append(module_name)
        # Optionally import the module so that its symbols are available directly
        __import__(f"{__name__}.{module_name}", globals(), locals(), [], 0)

