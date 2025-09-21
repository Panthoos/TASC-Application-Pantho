from setuptools import find_packages, setup

package_name = 'tasc_application'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pantho',
    maintainer_email='pantho@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 
            "data_publisher = tasc_application.publisher:main",
            "data_subscriber = tasc_application.subscriber:main",
        ],
    },
)
