from setuptools import setup, find_packages

setup(
    name='django-hardarda',
    version='4.2.0',
    description='This is a project aimed at overriding the default admin templates of Django 4.2, using Bootstrap 5 as the base for the new templates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jonaspeters/django-hardrada',
    author='Jonas Peters',
    author_email='jonas.peters123@gmail.com',
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='django, plugin, bootstrap, admin, templates',
    packages=find_packages(),
    python_requires='>=3.10',
)
