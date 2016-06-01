beets-drop
===================

Beets plugin to drop incomplete and unclassified items in particular folders

Install
-------

.. code-block:: bash

    pip install https://github.com/mazenovi/beets-drop/archive/master.zip

To activate it, add `drop` to the list of you plugins in your
configuration file (config.yaml)

.. code-block:: bash

    plugins: [...] drop [...]


How to use it
-------------

You can now configure one path for incomplete item and one path to unclassified item.
Add in your configuration file (config.yaml)

.. code-block:: bash

drop:
    unclassified: /your/path/to/Unclassified

    incomplete: /your/path/to/Incomplete
