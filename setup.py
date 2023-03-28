from distutils.core import setup
setup(
  name = 'hypergraphx',         
  packages = ['hypergraphx'], 
  version = '1.1',      
  license='BSD-3-Clause license',        
  description = 'HGX is a multi-purpose, open-source Python library for higher-order network analysis',   
  author = 'HGX-Team',              
  author_email = 'lotitoqf@gmail.com',      
  url = 'https://github.com/HGX-Team/hypergraphx',   
  download_url = 'https://github.com/HGX-Team/hypergraphx/archive/refs/tags/Alpha1.tar.gz',    
  keywords = ['hypergraphs', 'networks'], 
  install_requires=[
          'numpy',
          'scipy',
          'networkx',
          'rpy2',
          'pandas',            
          'seaborn',
          'matplotlib',
          'pytest',
          'scikit-learn',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD License',   
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)