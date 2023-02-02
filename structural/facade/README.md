**Eckel**

If you have a rather confusing collection of classes and interactions that the client programmer does not really need
to see, then you can create an interface that is useful for the client programmer and that only presents 
what is necessary.

**Kamon Ayeva**

It is not unusual to end up with a very large collection of classes and interactions. In many cases we do not want to expose
this complexity to the client. This is where facade structural pattern comes to the rescue.
The facade design pattern helps us to hide the internal complexity of our systems and expose only what is 
necessary to the client through a simplified interface. In essence it is an abstraction layer implemented 
over an existing complex system.

**Steven F. Lott**
Any time we want access to common or  typical functionality, we can use a single object's simplified interface. 
If another part  of the project needs access to more complete functionality, it is still able to interact
with the components and individual methods directly.
