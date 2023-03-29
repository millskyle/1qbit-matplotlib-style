from setuptools import setup

setup( name='Plot1Qbit',
       version='0.21',
       author='Kyle Mills',
       author_email="kyle.mills@uoit.net",
       description="Set matplotlib style to conform with 1QBit's brand policies",
       packages=['plot1qbit', 'plot1qbit.report_maker'],
       install_requires=['tabulate', 'matplotlib>=3.1.0', 'gif', 'tqdm', 'numpy'],
       include_package_data=True
    )
