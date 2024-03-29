from skbuild import setup

# python -c "import skbuild;print(skbuild.constants.CMAKE_BUILD_DIR())"

setup(
    name="skbgudhi",
    version="0.0.0",
    description="GUDHI python module build with scikit-build",
    author="The GUDHI Editorial Board",
    author_email="gudhi-contact@inria.fr",
    license="MIT",
    packages=["skbgudhi"],
    python_requires=">=3.7",
)
