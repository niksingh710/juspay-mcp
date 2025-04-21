from setuptools import setup, find_packages

setup(
    name="juspay-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.8",
        "httpx>=0.28.1",
        "mcp[cli]>=1.6.0",
        "python-dotenv>=1.1.0",
        "starlette>=0.46.1",
        "uvicorn>=0.34.0",
    ],
    entry_points={
        "console_scripts": [
            "juspay-tools=juspay_tools.main:main",
        ],
    },
)