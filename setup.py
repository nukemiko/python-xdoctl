from setuptools import setup


def pkgver():
    with open('VERSION', encoding='utf-8') as f:
        _pkgver = f.read().strip()
    return _pkgver


def longdesc():
    with open('README.md', encoding='utf-8') as f:
        _desc = f.read().strip()
    return _desc


setup(
    name='python-xdoctl',
    version=pkgver(),
    packages=['xdoctl'],
    url='https://github.com/nukemiko/python-xdoctl',
    license='MIT',
    author='nukemiko',
    author_email='north666dakota@gmail.com',
    description='Xdotool 命令包装器',
    long_description=longdesc(),
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    platforms='linux',
    keywords=['xdotool', 'libxdo', 'xdo', 'mouse', 'keyboard']
)
