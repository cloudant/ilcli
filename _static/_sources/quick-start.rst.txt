.. -*- mode:rst; coding:utf-8 -*-

.. _quick-start:

Quick Start
===========

``ilcli`` is a Python library based on ArgumentParser that provides
the following features:

* **Subcommand** creation support so you can build a complex,
  well-structured, and standard CLI.

* Support for including **documentation** (man pages, web links, etc.)
  so users can quickly open different doc directly from the your tool.

* **REST API** automatic conversion: start serving your CLI as a REST
  API so it can be executed remotely.

* **Multi-project** CLI: build a general CLI whose subcommands will be
  pulled from different projects so you can unify tools.

The most important bit of ``ilcli`` is the :class:`~ilcli.Command`
class. All commands you define should be children of this class.


The minimal example
-------------------

.. literalinclude:: examples/minimal.py

This creates a command without options (just ``-h``):

.. program-output:: python examples/minimal.py
   :prompt:

.. program-output:: python examples/minimal.py -h
   :prompt:

Note that the name of the class is taken as program name. You can
tweak this by setting the class attribute ``name`` to whatever value
you need.


Arguments and options
---------------------

Arguments and options should be added by overriding
``_init_arguments()`` method. In this method, you can use
``self.add_argument()`` method for adding arguments in **exactly** the
same way as you would do with :func:`ArgumentParser.add_argument`
method sinc it accepts the same parameters.

.. literalinclude:: examples/args_opts.py

Now our command has a positional argument and one option. If not
provided, it will fail:

.. program-output:: python examples/args_opts.py
   :returncode: 2
   :prompt:

Note that the arguments and options can be provided as part of the
``run()`` method:

.. program-output:: python examples/args_opts.py "I like command line interfaces!"
   :prompt:


Validate arguments
~~~~~~~~~~~~~~~~~~

Although :class:`ArgumentParser` provides some mechanisms for checking
the parameters (such as `type`, `choices`, etc.), sometimes is useful
to perform extra validation on the arguments which are application
specific. For that, you can use ``_validate_arguments()`` method:

.. literalinclude:: examples/args_opts_validation.py

.. program-output:: python examples/args_opts_validation.py -u 'Hello!'
   :prompt:

Note that any extra argument will be treated as an error (the default
:class:`ArgumentParser` behaviour) which will make the program fail:

.. program-output:: python examples/args_opts_validation.py -u 'Hello!' --something more
   :returncode: 2
   :prompt:

It is worth to mention that ``self._run()`` will not be executed if
``self._validate_arguments()`` returns something, so we can make sure
that once ``self._run()`` is executed, the arguments are validated
at our semantics level:

.. program-output:: python examples/args_opts_validation.py 'help me'
   :prompt:

.. program-output:: python examples/args_opts_validation.py 'ilcli is cool!'
   :returncode: 1
   :prompt:

In certain cases, you might want to allow the user to provide multiple
arguments at the command line interface that actually cannot be
specified for multiple reasons. For example, too many possible
argument combinations or your application needs to get values to be
replaced in a template:

.. literalinclude:: examples/args_extra_opts_validation.py

.. program-output:: python examples/args_extra_opts_validation.py '{name} is cool!' name=ilcli
   :prompt:


Subcommands
-----------

One interesting feature that :class:`ilcli.Command` class provides is
that it can be composed by other commands forming sub-commands in a
similar way as tools like ``apt`` or Chef ``knife`` are
structured. The result is a tree-like structure with two types of
commands:

* Node commands: commands that define subcommands. By default, their
  arguments will be passed to their children as common arguments.

* Leaf commands: commands that do not define subcommands. They can
  define their own arguments and, by default, they will inherit the
  parent's ones.

Subcommands are defined as a class attribute:

.. literalinclude:: examples/args_subcommands.py

``ilcli`` will automatically build a tree hierarchy with the command
that is firstly created as root and recursively creates the command
tree. Note that each command can define its own set of arguments.

.. program-output:: python examples/args_subcommands.py -h
   :prompt:

.. program-output:: python examples/args_subcommands.py net -h
   :prompt:

.. program-output:: python examples/args_subcommands.py net ssh -h
   :prompt:


Argument inheritance
~~~~~~~~~~~~~~~~~~~~

As we have seen in the previous example, it can also define arguments
that will be passed to the children. In general, when a command
defines arguments, then they will propagated to all leaf commands
under that command. This is ``ilcli`` default behaviour although it
might be tweaked using the following mechanisms:

* ``inherit_arguments = False``: if it is defined as a class
  attribute in the command, no arguments will be passed to this
  command.

  .. literalinclude:: examples/not_inherit_args.py

  Thus, subcommands could define their own arguments without clashing
  with parent's:

  .. program-output:: python examples/not_inherit_args.py ls -h
     :prompt:

  .. program-output:: python examples/not_inherit_args.py rm -h
     :prompt:

  This is very useful in situations when you want to have a subcommand
  within a specific command (because makes sense there or it is
  related to it) but all the previous arguments do not apply to
  it. For exmplate, you my have::

    $ mytool members list --org myorg
    $ mytool members create --org myorg new-member
    $ mytool members request --url https://api.server.com

  In this case, ``list`` and ``create`` share the argument ``--org``
  that comes from ``members``. However, ``request`` a new member
  requires just the URL (from where you probably get the ``org``
  parameter) and still makes sense having ``request`` under
  ``members`` because it is related to it.

  An important aspect when you use this feature is that the parents'
  validation code is not executed at all. Using this flag you will
  need to implement a new validation argument functions, if
  needed. See the following execution examples:

  .. program-output:: python examples/not_inherit_args.py rm -v
     :prompt:

  .. program-output:: python examples/not_inherit_args.py ls -v
     :prompt:

* ``_init_arguments()``: the parent could decide what arguments pass
  to its children by implementing it in the ``_init_arguments()``
  method. The parent keeps a list of subcommands at
  ``self._subcommands``

The argument inheritance mechanisms implies a few limitations:

* By default, since the arguments actually reside on leaf command
  parsers, there can not be conflicted names. That is, 2 argument
  names can not be defined at different levels of the same path of the
  hierarchy. However, you can change this default behaviour and allow
  argument overriding. See :ref:`argument_overriding`.

* Commands that define sub-commands should not define ``_run()``. By
  default, it will never be executed as only leaf commands are taking
  into account. However, since children has a reference to the parent
  command they might run parent commands as part as their run.

Removing arguments
------------------
A :class:`~ilcli.Command` might inherit an argument you don't want,
either from a parent class or being a sub-command of another
:class:`~ilcli.Command`. These can be ignored via ``ignore_arguments``,
though if you are ignoring lots of things you may want to reevaluate
your class/command heirarchy. Arguments are ignored by their switch
(``-f/--foo``) or the name given for positional arguments.

* ``ignore_arguments = []``: list of switches/positional arguments to ignore,
  identified by their switch (both ``-f`` and ``--foo`` will work) or the name
  given to positional arguments.

.. program-output:: python examples/removing_arguments.py -h
   :prompt:

``firstdemocommand`` ignores the ``-b/--bar`` switch, and adds the ``--foo``
switch

.. program-output:: python examples/removing_arguments.py firstdemocommand -h
   :prompt:

``seconddemocommand`` inherits from ``firstdemocommand`` and both ignores
``-b/--bar`` switch and the ``--foo`` switch.

.. program-output:: python examples/removing_arguments.py seconddemocommand -h
   :prompt:

``thirddemocommand`` inherits from ``firstdemocommand`` and ignores the ``bat``
positional argument.

.. program-output:: python examples/removing_arguments.py thirddemocommand -h
   :prompt:

Documentation support
---------------------

Although using ``-h`` in your commands there is plenty of information
to know how to use your tool, sometimes is also good to provide
extended information.

.. literalinclude:: examples/doc.py

This automatically add an option ``--doc`` in the command where it
class attributes has been defined:

.. program-output:: python examples/doc.py net -h
   :prompt:

In this case, if ``--doc`` is used it will open the man page
specified. Note that this is an action that, once is finished, nothing
else is executed. Also note that the class attributes might be defined
at any point of the command hierarchy, so you could have more general
documentation in top-level commands, and more concrete one in the leaf
commands::

  $ mycmd [--doc] subcommand1 [--doc] ...

.. _argument_overriding:

Argument overriding
-------------------

``ilcli`` will fail if you define the same argument on a single
inheritance path. However, ``ArgumentParser`` allows to resolve this
conflicts by setting ``conflict_handler=resolve``. You can set custom
arguments to be used in all parsers created by ``ilcli`` internally by
using the class property ``parser_args``.

Here it is an example of how to allow argument overriding:

.. literalinclude:: examples/args_conflict_subcommands.py

Note that ``toplevel`` subcommands defines ``parser_args``. Now
``ilcli`` will not fail and, as ``ArgumentParser`` does, subcommands
will override conflicts:

.. program-output:: python examples/args_conflict_subcommands.py subcommand1 -h
   :prompt:

.. program-output:: python examples/args_conflict_subcommands.py subcommand2 -h
   :prompt:

.. program-output:: python examples/args_conflict_subcommands.py subcommand3 -h
   :prompt:


REST API support
----------------

TBD


Multi-project CLI
-----------------

TBD
