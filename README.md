# simple-cmdb

A CMDB in zero time, based on [FastAPI](https://fastapi.tiangolo.com/)

## Make use of the venv

`source simple-cmdb/bin/activate`, or for more details, [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## Start uvicorn, for development

`uvicorn main:app --reload`

## Design Goals

* Dynamic inventory for ansible... so, based around [groups]
    * I think this means we need a limited number of URLs, one for each Dev/Test/Staging/Prod environment
    * I suggest https://ayr.library.ualberta.ca/cmdb/\<environment\>/
* Ansible dynamic inventory interface: probably a very simple script, in line with `inventory-test`, that will query this app & then reformat the output as the appropriate JSON
* Ansible will now be in charge of building our servers via templates in VMWare... we need key hardware details, including CPU socket and thread counts, memory, and disk volumes, types, sizes, etc, accessible in a dictionary that Ansible can consume
* We need to store the bulk of the information from the Server tab of the "IT Discovery Worksheet", and make it easily accessible for reporting purposes... export as .csv ? 
* We need to be able to update this information automatically
* We need to be able to track how this information changed over time (how was it changed; who changed it; when was it changed)
* Only some data can be updated automatically, eg like the amount of memory allocated to a VM.  But for other types of data, like ownership of a project, we need a solution to enable staff to update information dynamically, eg a web interface
* (Access controls? Permission who-can-edit-what? )
* We need a convenient way to pre-load the data from the spreadsheet eg from CSV

## Storing the Data

There are multiple choices to act as a back-end data store.  I've written this before with just a YAML file. It could be a SQL database, or a Redis collection. 

## Disaster Recovery, and the Critical Nature of the Data

The bulk of our DR plan rests on us being able to re-build the VM's in essentially the same format they existed pre-disaster, with a little bit of CommVault recovery sprinkling our data back into the appropriate location.

The information inside this app is absolutely critical. It needs to be backed up regularly. 

In the context of a disaster, we should be able to begin building the database servers before CommVault is running, so exporting the data & mailing it off to the cloud, or stashing it on Github, is an entirely appropriate design pattern. Think deltas. Think git. Think USB flash drives.