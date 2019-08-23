from setuptools import setup

setup(
    name='gcloud-dyndns',
    version='1.0',
    packages=['gcloud_dynamic_dns'],
    scripts=['bin/update-gcloud-dns'],
    url='https://github.com/jasonrig/gcloud-dyndns',
    license='MIT',
    author='Jason Rigby',
    author_email='hello@jasonrig.by',
    description='Update GCP Cloud DNS using the host\'s publicly visible IP address',
    install_requires=[
        'google-cloud-dns>=0.30.2,<0.31',
        'requests>=2.22.0,<2.23'
    ]
)
