from setuptools import setup
from os.path import join, dirname


setup(
    name='telegram_logger',
    version='0.0.1',
    packages=[''],
    url='https://github.com/zdv-1993/telegram_logger',
    license='MIT',
    author='zdv-1993',
    author_email='zdv-1993@mail.ru',
    description='External logging library. Send log messages to telegram',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'pyTelegramBotAPI>=4.4.1'
    ]
)
