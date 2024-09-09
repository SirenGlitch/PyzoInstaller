import os

# Install Pyzo and pyqt5
pyzo_install = ('py -m pip install \
--trusted-host pypi.org \
--trusted-host pypi.python.org \
--trusted-host files.pythonhosted.org \
--user pyzo pyqt5')

os.system(pyzo_install)
