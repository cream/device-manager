from distutils.core import setup
from distutils.command.install_scripts import install_scripts

class post_install(install_scripts):

    def run(self):
        install_scripts.run(self)

        from shutil import move
        for i in self.get_outputs():
            n = i.replace('.py', '')
            move(i, n)
            print "moving '{0}' to '{1}'".format(i, n)


ID = 'org.cream.Devices'
data_files = [('share/cream/{0}'.format(ID), ['src/manifest.xml'])]


setup(
    name = 'cream-device-manager',
    version = '0.0.8',
    author = 'The Cream Project (http://cream-project.org)',
    url = 'http://github.com/cream/device-manager',
    package_dir = {'udisks': 'src/udisks'},
    packages = ['udisks'],
    data_files = data_files,
    cmdclass={'install_scripts': post_install},
    scripts = ['src/device-manager.py']
)
