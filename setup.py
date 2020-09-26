from setuptools import setup
# @TODO , dynamically generate this from __nada__ file.
# dont need it ??
setup(
    name="Nada",
    version="1.0",
    packages=["nada","nada.common"],
    include_package_data=True,
    install_requires=["click", "colorama"],
    entry_points="""
        [console_scripts]
        nada=nada.nada:init
    """,
)
