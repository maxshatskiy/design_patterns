**Kamon Ayeva:**
Client asks for an object without knowing which class is used to generate this object.
The idea is to simplify the object creation process.
A factory pattern reduces the complexity of maintaining an application by decoupling the code that creates and object
from the code that uses it.

**Factory method** returns a different object per input parameter.
**Abstract factory**, is a group of factory methods used to create a family of a related objects.

The factory method centralizes object creation and tracking of objects becomes much easier.

**Aaron Maxwell:**

**Simple factory pattern:** object type is fixed but there are different ways to create it.
**Factory method:** factory dynamically chooses one of several different types. The factory will create an
object, but will choose its type from one of several possibilities, dynamically deciding at runtime based
one some criteria.
It is typically used when we have one base class and are creating an object that can be one of several different
derived classes.

**Eckel B.**
The Abstract Factory has not one but several factory methods. Each factory method creates s different kind of object.
The idea is that at the point of creation of the factory object, you decide how all the objects created by that 
factory will be used.
Examples: 
1. create a factory object appropriat eto the GUI that we are working with and from then on when 
we ask it for menu, button or slider it will automatically create the appropriate version of that item for GUI.
2. we creating a general-purpose gaming enviroment and want to be able to support different types of games.

**From Steven F. Lott**
There are two central features of an Abstract Factory:
* We need to have multiple implementation choices. Each implementation has a factor class to create objects.
A single Abstract Factory defines the interface to the implementation factories.
* We have a number of closely related objects, and the relationship are implemented via multiple methods of each factory.



