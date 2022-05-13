from setuptools import find_packages, setup



setup(
    name='MIND-GRAF',
    version='0.0.0',
    packages = find_packages(),
    install_requires=['click'],
    entry_points = {'[console_scripts]': ['mgraf=basicCmd:mgraf','show=basicCmd:show',
    'define=basicCmd:define','remove=basicCmd:remove','clear=basicCmd:clear','trace=basicCmd:trace']
})