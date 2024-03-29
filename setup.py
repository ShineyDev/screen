import re
import setuptools


with open("docs/requirements.txt", "r") as stream:
    extras_require_docs = stream.read().splitlines()

extras_require = {
    "docs": extras_require_docs,
}

packages = [
    "screen",
    "screen.controls",
    "screen.controls.primitives",
    "screen.drawing",
    "screen.utils",
]

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
    description="A Python library for creating TUI inspired by WPF.",
    extras_require=extras_require,
    include_package_data=True,
    license="Apache Software License",
    name="screen",
    packages=packages,
    python_requires=">=3.6.0",
    url="https://github.com/ShineyDev/screen",
    version=version,
)
