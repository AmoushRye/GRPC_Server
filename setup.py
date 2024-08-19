from setuptools import setup

PACKAGE_NAME = "GRPC_server"

package_dir_map = {
    f"{PACKAGE_NAME}": "GRPC_server",
}
setup(
    name = PACKAGE_NAME,
    version='0.4',
    packages=package_dir_map.keys(),
    package_dir=package_dir_map,
    include_package_data=True,
    install_requires=[
        'grpcio',
        'grpcio-tools',
    ],
    entry_points={
        'console_scripts': [
            'startServer=GRPC_server.server:main',
        ]
    },
)
