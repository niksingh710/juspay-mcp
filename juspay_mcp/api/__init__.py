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

