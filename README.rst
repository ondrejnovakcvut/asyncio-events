Events-asyncio
----
This is a modification of `Events library`_ that adds support for asyncio.
Unlike the original library, this modification only supports Python 3.5+.

The C# language provides a handy way to declare, subscribe to and fire events.
Technically, an event is a "slot" where callback functions (event handlers) can
be attached to - a process referred to as subscribing to an event. Here is
a handy package that encapsulates the core to event subscription and event
firing and feels like a "natural" part of the language.

.. code-block:: pycon

    >>> async def something_changed(reason):
    ...     await some_awaitable()
    ...     print "something changed because %s" % reason
    ...

    >>> from events import Events
    >>> events = Events()
    >>> events.on_change += something_changed

Multiple callback functions can subscribe to the same event. When the event is
fired, all attached event handlers are invoked in sequence. To fire the event,
perform a call on the slot:

.. code-block:: pycon

    >>> await events.on_change('it had to happen')
    'something changed because it had to happen'

By default, Events does not check if an event can be subscribed to and fired.
You can predefine events by subclassing Events and listing them. Attempts to
subscribe to or fire an undefined event will raise an EventsException.

.. code-block:: pycon

    >>> class MyEvents(Events):
    ...     __events__ = ('on_this', 'on_that', )

    >>> events = MyEvents()

    # this will raise an EventsException as `on_change` is unknown to MyEvents:
    >>> events.on_change += something_changed

You can also predefine events for a single Events instance by passing an iterator to the constructor.

.. code-block:: pycon

    >>> events = Events(('on_this', 'on_that'))

    # this will raise an EventsException as `on_change` is unknown to events:
    >>> events.on_change += something_changed


Installing
----------
Events is on PyPI so all you need to do is: ::

    pip install asyncio-events

Testing
-------
Just run: ::

    python setup.py test


License
-------
Asyncio-events is BSD licensed. See the LICENSE_ for details.


Attribution
-----------
Based on Events library by `Nicola Iarocci`.

.. _LICENSE: https://github.com/pyeve/events/blob/master/LICENSE
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/
.. _`Nicola Iarocci`: https://github.com/nicolaiarocci
.. _`Events Library`: https://github.com/pyeve/events
