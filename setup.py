from setuptools import setup

setup(name='amninders_normal_binomial_dist',
      packages=['amninders_normal_binomial_dist'],
      version='0.7',
      license='MIT',
      description='Calculating and Plotting a Gaussian distributions and a Binomial distribution',
      long_description = file: README.md,
      long_description_content_type = text/markdown
      author='Amninder Singh',
      url='https://github.com/amnindersingh12/gaussian-binomial',
      install_requires=[            
          'matplotlib'
        ],
      zip_safe=False)
