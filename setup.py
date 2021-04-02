import re
import setuptools


classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: User Interfaces",
    "Typing :: Typed",
]

extras_require = {
    "docs": [
        "sphinx",
        "sphinxcontrib_trio",
        "sphinx-rtd-theme",
    ],
}

packages = [
    "screen",
    "screen.controls",
    "screen.controls.primitives",
    "screen.drawing",
    "screen.utils",
]

project_urls = {
    "Documentation": "https://screen.readthedocs.io",
    "Issue Tracker": "https://github.com/ShineyDev/screen/issues",
    "Source": "https://github.com/ShineyDev/screen",
}

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("screen/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass


setuptools.setup(
    author="ShineyDev",
    classifiers=classifiers,
    description="A Python library for creating TUI inspired by WPF.",
    extras_require=extras_require,
    license="Apache Software License",
    name="screen",
    packages=packages,
    project_urls=project_urls,
    python_requires=">=3.6.0",
    url="https://github.com/ShineyDev/screen",
    version=version,
)
