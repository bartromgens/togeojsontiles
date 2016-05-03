from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(
    name='togeojsontiles',
    version='0.1.2',
    description='Create geojson-tiles from gpx or geojson using tippecanoe (C++) and togeojson (javascript)',
    long_description=long_description,
    keywords='gis geojson tippecanoe tiles map-tiles mbtiles gpx',
    url='http://github.com/bartromgens/togeojsontiles',
    author='Bart Römgens',
    author_email='bart.romgens@gmail.com',
    license='MIT',
    packages=['togeojsontiles'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
