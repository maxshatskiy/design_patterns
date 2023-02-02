**Lott**
Structually similar to strategy pattern, but its intent and purpose are very different.
Object behaviour is constrained by the state it is in and there are defined transitions to other states.

The two type of classes are used: Core and Multiple State classes. The Core class maintains the current state and
forwards actions to a current state object. The state objects are hidden from any other objects that are calling
the Core object.

Strategy and state patterns are similar because they both delegate work to other objects. This decomposes a complex
problem into several closely related but simpler problems.

Strategy pattern is used to choose an algorithm at runtime. The main idea is to make implementation choice at runtime.
Strategy classes are rarely aware of other implementations and each _Startegy_ is generally stands alone.

State pattern allows switching between different states dynamically as some process evolves.

**Ayeva**
_State machine - representation of the system by states and transitions and can be represented as graphs.
State pattern: state machine applied to a particular software engineering problem.
Usa cases.  All the problems that can be solved using state machines are good use cases for using the State pattern._

**Eckel**
_Each state can be run() to perform its behaviour and it is possible to pas it and input object soe that it can tell what
the new state ot move to based on that input._
