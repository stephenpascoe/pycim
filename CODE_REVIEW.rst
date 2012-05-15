Pycim
=====

Please see the ``pycim-mp`` code review as most comments apply equally to ``pycim``.  

1. README.md explains what pycim-mp is instead of pycim.

2. Tests require simplejson but Python 2.6+ has a json module.  Consider
   replacing.

3. I have adapted the test code to run through the ``nose`` test discovery 
   utility

4. See the ``#!REVIEW`` annotations in the source, particularly with regard to  
   the getter/setter idiom for list attributes.  This is the only instance  
   I have found of significant bad design in the source.
