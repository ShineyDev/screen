import re
import setuptools


with open("screen/__init__.py", "r") as stream:
    version = re.search(r"^version = [\"]([^\"]*)[\"]", stream.read(), re.MULTILINE).group(1)

if version.endswith(("a", "b", "rc")):
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

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Typing :: Typed",
]

extras_require = {
    "docs": ["sphinx", "sphinxcontrib_trio", "sphinx-rtd-theme"],
}

project_urls = {
    "Documentation": "https://screen.readthedocs.io",
    "Issue Tracker": "https://github.com/ShineyDev/screen/issues",
    "Source": "https://github.com/ShineyDev/screen",
}

setuptools.setup(
    author="ShineyDev",
    classifiers=classifiers,
    description="A Python library for creating TUI inspired by WPF.",
    extras_require=extras_require,
    license="Apache Software License",
    name="screen",
    packages=[
        "screen",
        "screen.controls",
        "screen.controls.primitives",
        "screen.drawing",
        "screen.utils",
    ],
    project_urls=project_urls,
    python_requires=">=3.6.0",
    url="https://github.com/ShineyDev/screen",
    version=version,
)
