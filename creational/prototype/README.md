**Wessel Badenhorst:**
In the prototype pattern we favor composition over inheritance. Classes that are composed of parts allows you
to substitute those parts at runtime. The classes to instantiate are specified at runtime by means of dynamic loading.
Sub-classing is reduced significantly.
This pattern forces to programm interface, which leads to a better design.

3 components:
* **prototype** declares an interface for cloning itself;
* **client** creates a new object by asking a prototype to clone itself;
* **concrete prototype** implements the operation for cloning itself;


**From https://radek.io/2011/08/03/design-pattern-prototype/**

The intent of prototype is to create new instances of clases by clonning a prototype instance, rather than building them
from scratch. This is particularly usefull when initialization of objects is very expensive and very similar among the
majority of created instances.

**Template pattern from Steven F. Lott**