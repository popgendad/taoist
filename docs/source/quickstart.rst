Quickstart
==========

.. _installation:

Installation
------------

The taoist package can be installed via PyPi

.. code-block:: console

   $ pip install taoist

.. _examples:

Examples
--------

Next, connect ``taoist`` to your Todoist account. First you must retrieve your API token 
from the Todoist app. Once you have your API token, you can authenticate to the web service
by running

.. code-block:: console

   taoist init --token <TOKEN>

if run without the ``--token`` switch, you will be interactively prompted to provide the API token.

To see your list of projects, run

.. code-block:: console

   taoist project list

Similarly, to see your list of tasks, run

.. code-block:: console

   taoist task list
