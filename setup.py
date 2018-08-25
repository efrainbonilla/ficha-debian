#!/usr/bin/python3

from setuptools import setup, find_packages
from ficha.ficha import VERSION

LONG_DESC= """
Navegador personalizado para sistema de Atención al usuario
de Servicio Nacional de Propiedad Intelectual SENAPI
"""

setup(
    name='ficha',
    version=VERSION,
    description='Navegador personalizado para el sistema ficha.',
    long_description=LONG_DESC,
    author='Efrain Bonilla',
    author_email='efrainbonilla.dev@gmail.com',
    url='https://github.com/efrainbonilla/ficha',
    license='Apache License, Version 2.0',
    packages=find_packages(exclude=['']),
    data_files=[
        # Desktop entry
        ('/usr/share/applications',['share/applications/ficha.desktop']),
        # App icon
        ('/usr/share/icons',['share/icons/ficha.png']),
        # Application core
        ('/usr/share/ficha',['ficha/images/ficha.png']),
        # Documentation files
        ('/usr/share/doc/ficha', ['README.md','LICENSE','AUTHORS', 'copyright', 'TODO'])],
    scripts = ['bin/ficha']
    )

