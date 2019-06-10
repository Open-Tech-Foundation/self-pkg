import os
from child_process import spawn
from getpass import getpass

password = getpass("Please enter your password: ")
password = f"{password}\n".encode()

os.makedirs('/tmp/self-pkg', exist_ok=True)

os.chdir('/tmp/self-pkg')

print('> Downloading archive')
spawn([
    'wget', 'https://github.com/git/git/archive/v2.21.0.tar.gz', '-O',
    'git-2.21.0.tar.gz'
], "Failed to download package source archive")

print('> Extracting archive')
spawn(['tar', '-zxvf', 'git-2.21.0.tar.gz'],
      err_msg="Failed to extract package archive")

print('> Installing dependencies')
spawn(['sudo -S yum groups install "Development Tools" -y'],
      shell=True,
      input=password,
      err_msg="Yum group install failed")
spawn(['sudo -S yum install -y openssl-devel curl-devel expat-devel'],
      shell=True,
      input=password,
      err_msg="Yum group install failed")

os.chdir('git-2.21.0')

print('> Building package')
spawn(['make', 'configure'], err_msg="Package building failed", verbose=True)
spawn(['./configure', '--prefix=/usr/local'],
      err_msg="Package building failed",
      verbose=True)

print('> Installing package')
spawn(['sudo -S make install'],
      shell=True,
      input=password,
      err_msg="Package Install failed",
      verbose=True)
