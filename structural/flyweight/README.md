**Steven F. Lotty**:
The Flyweight is a memory optimization pattern.
It ensures that objects that share a state can use the same memory for their shared state. It is normally implementeed 
after a program has demonstrated memory problems.

**Kamon Ayeva**
Whenever we create a new object, extra memory needs to be allocated.
A flyweight is a shared object that contains state-independent, immutable data. The state-dependent, mutable data 
should not be part of flyweight because this is infromation that cannot be shared, since it differs per object.
Flyweights is all about improving performance and memory usage. All embedded systems and performance-critical
applications can benefit from it.
Where to use it:
* application needs to use a large number of objects;
* it is expensive to store/render them. Once the mutable state is removed, many groups of distinct objects
can be replace by relatively few shared objects.
* object identity is not important for the application. sharing causes identity comparison to fail.
