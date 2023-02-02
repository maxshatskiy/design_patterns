Kamon Ayeva:
In the process of writing code that handles algorithms in the real world, we often
end up writing redundant code. The template pattern focuses on eliminating code redundancy. the idea is that we 
should be able to redefine certain parts of an algorithm without changing its structure.

The Template design pattern focuses on eliminating code repetition. If we notice that there is repeatable code
in algorithms that have structural similarities, we can keep the invariant parts of the algorithms in
a template method and move the variant parts in action/hook methods/functions.

Steven F. Lott:
This pattern is usefull for removing duplicate code. It is designed for situations where
we have several different tasks to accomplish that have some, but not all, steps in common. The common steps are
implemented in a base class and the distinct steps are overridden in subclasses to provide custom behaviour.
In some ways it is like Strategy pattern, except similar sections of the algorithms are shared using a base class.

Eckel. B.

A fundamental concept in the application framework is the Template Method which is typically hidden beneath
the covers and drives the application by calling the various method in the base class, some of which you have 
overriden in order to create the application.
The Template Method is defined in the base class and cannot be changed. it calls other base-class methods in order
to do its job.
