# AppSec_Dingo
In-Toto and Trusted Platform Modules

Run these commands:

# Make sure you have git, python and pip installed on your system
# and get in-toto
git clone -b develop --recursive https://github.com/Andrew-Zarenberg/AppSec_Dingo.git

# Change into project root directory
cd in-toto

# Install with pip in "develop mode"
# (we strongly recommend using Virtual Environments)
# http://docs.python-guide.org/en/latest/dev/virtualenvs/
pip install -e .

# Export the envvar required for "simple settings"
export SIMPLE_SETTINGS=toto.settings

# Install additional requirements that for some good reason are not in the
# requirements file
pip install pycrypto cryptography

# Change into the demo directoy and you are ready to start
cd demo

# Edit this file - this will be the file that gets verified. (Use whatever text editor you like)
emacs functionary_bob/foo.py

# Clear the TPMs
python clear_tpm.py

# Create stage - create the initial TPM values for the file
python create_stage.py

# ATTENTION: Here you can either modify the same functionary_bob/foo.py file, which will generate a TPM signature error when the following command is run, or you can go ahead and run the command and it should pass.
python verify_stage.py


If you are having trouble getting it to work, here is a link to the original in-toto GitHub repository with installation instructions: https://github.com/in-toto/in-toto/tree/develop/demo

If you are still having issues, please email:
Andrew Zarenberg <az1148@nyu.edu>
