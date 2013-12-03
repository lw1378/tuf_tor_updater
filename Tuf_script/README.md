Introduction
=================================
1. repository_operator.py
---------------------------------
Before using repository_operator.py, you should first install tuf-repository-tool.
* See the help log.

```python

  $ python repository_operator.py --help
  *** Hello ...
  --Help info--
  Usage: 
  """
  before generate new repository directory, you should make sure that there
  is a basic legal temp directory to put your update files, you could create by
  yourself, or use "generate_file_dir" to generate a directory and just put your
  files into the directory.
  1. Generate TUF repository, syntax:
  $python repository_operator.py --generate_repository directory_name
  2. Genrerate new TUF repository for update, syntax:
  $python repository_operator.py --update_repository directory_name
  3. Generate TUF repository without delegations, syntax:
  $python repository_operator.py --generate_repository -nd directory_name
  4. Generate new TUF repository for update without delegations, syntax:
  $python repository_operator.py --update_repository -nd directory_name
  """

```

* Generate a completely new repo metadata and client, with -nd means 'no delegation'

```python

  # generate a new repo metadata and client, here with '-nd' as an example
  $ python repository_operator.py --generate_repository -nd targets_files
  *** Hello ...
  Input Server path:
  # Here input the server path on your computer
  /home/laiwang/Documents/apache_Server/
  Server path:  /home/laiwang/Documents/apache_Server/
  Input client path:
  # Here input the client path, actually client is in different environment from server
  # Here just use local client as an example, but in different path
  /home/laiwang/Documents/repy_tuf/client/
  Client path: /home/laiwang/Documents/repy_tuf/client/
  # After input the server and client path, we also need to input the path of writemetainfo_dir
  # And we also need to input the path of private key and public key which are used to
  # generate the metainfo of softwareupdater.py
  *** Hello ...
  Create directory  targets_files
  Warning: 'tor-browser-2.3.25-14_en-US.exe' not in previous metainfo file!
  Writing a metafile with updates to:
  >>> Updating targets_files files ...
  >>> Creating RSA keys ...
  >>> Creating root, timestamp, release and targets ...
  >>> Copying target files ...
  >>> Adding target files ...
  >>> Making client directory ...
  *** Process complete ...
  >>> Updating /home/laiwang/Documents/apache_Server/ files ...
  >>> Updating /home/laiwang/Documents/repy_tuf/client/ files ...
  
```

Specific usage:

```python
  # 
```

2. writemetainfo.py
---------------------------------
Use writemetainfo.py to generate the metainfo of speicific file(s) in writemetainfo_dir directory.
Without metainfo file, you cannot download an update with softwareupdater.py

```python
  $ python writemetainfo.py private_key_file_name public_key_file_name
```


3. scripts
---------------------------------
when using this script, you should first modify this script so that it is your os directory's path.
you should have your tuf platform and repy v1 platform so that you could run your code.

```python
  # run the script
  # generate new repo
  $ . ./create_repository.sh
  # update repo
  $ . ./update_repository.sh
  # test to download with softwareupdater.py
  $ . ./safe_download.sh
```
