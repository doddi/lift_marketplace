# Sonatype Lift Marketplace

This is a repository containing contributed tools for Sonatype Lift

## Limitation
Currently, this marketplace only supports Python based tooling. Future enhancements will add other ecosystems.
Only supports V1 of the Lift Api

## Contributing
To contribute a tool simply create a PR with the additional tool.
The new tool should be in its own folder with the python file to run under that folder given the same name

For example the tool `foobar` must have a python file `foobar.py`

If setup is needed a `setup.sh` can be added to the tooling folder, this is run before the tool is run.
Note that as of this writing this is different to that explained in the Lift API documenation, this setup will only run prior to running the tool and is therefore not ran prior to the `applicable` checks
