from setuptools import setup, find_packages
import sys
import os

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_wheel = {'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

with open('README.md', 'r') as f:
    long_description = f.read()


def custom_git_parse(root):
    """ Travis only clones a 'shallow' repository (--depth=50), but we need
    the full repository to compute the version from the git metadata.
    By default setuptools_scm (as of v1.15.0) only warns when the repository
    is shallow; here we make it `fetch_on_shallow`.

    See: https://github.com/pypa/setuptools_scm/issues/93
    """
    from setuptools_scm.git import parse, fetch_on_shallow
    if os.path.exists(os.path.join(root, 'PKG-INFO')):
        return None
    else:
        return parse(root, pre_parse=fetch_on_shallow)


setup_params = dict(
    name="booleanOperations",
    use_scm_version={
        'parse': custom_git_parse,
    },
    description="Boolean operations on paths.",
    long_description=long_description,
    author="Frederik Berlaen",
    author_email="frederik@typemytype.com",
    url="https://github.com/typemytype/booleanOperations",
    license="MIT",
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    setup_requires=[
        "setuptools_scm>=1.15.0",
    ] + pytest_runner + wheel,
    tests_require=[
        'pytest>=3.0.2',
    ],
    install_requires=[
        "pyclipper>=1.0.5",
        "fonttools>=3.1.2",
        "ufoLib>=2.0.0",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

if __name__ == "__main__":
    setup(**setup_params)
