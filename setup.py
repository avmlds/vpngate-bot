from setuptools import find_packages, setup

setup(
    name="vpngate_bot",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "telebot == 0.0.5",
        "requests == 2.27.1",
        "prettytable == 3.10.0",
    ],
    scripts=["vpngate_bot/open-gate"],
    python_requires=">=3.7",
)
