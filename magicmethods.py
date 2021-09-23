# -*- coding: utf-8 -*-
"""
From http://www.wellho.net/mouth/3002_a-list-of-special-method-and-attribute-names-in-python.html
and also http://www.rafekettler.com/magicmethods.html 

__new__ True constructor - usually wraps __init__
__init__ Object constructor
__call__
__getattr__ Handling object attributes [example] and [calling example]
__setattr__
__delattr__
__getattribute__
__getitem__ subscripting with [..]
__setitem__
__delitem__
__del__ Destructor / wrapper around del
__repr__ Convert to Python source
__str__ Convert to printable string
__cmp__ Compare two objects
__lt__ Less Than
__gt__ Greater Than
__eq__ Equal to
__ne__ Not Equal to
__le__ Less Than or Equal
__ge__ Greater Than or Equal
__hash__ Calculate an (integer) hash value
__nonzero__ Is it nonzero
__unicode__ Convert to Unicode String
__get__
__set__
__delete__
__instancecheck__ isinstance builtin function
__subclasscheck__
__getslice__ Working with slices .. [..:..][example]
__setslice__
__delslice__
__len__ len building function
__add__ + [example]
__mul__ *
__contains__
__coerce__
__iter__
__reversed__
__sub__ -
__div__ /
__floordiv__ //
__mod__ %
__divmod__
__pow__ ^
__lshift__ <<
__rshift__ >>
__and__ &
__xor__ ~
__or__ |
__truediv__ __future__ > /
__radd__ "r" methods operate on object to right
__rmul__
__rsub__
__rdiv__
__rtruediv__
__rfloordiv__
__rmod__
__rdivmod__
__rpow__
__rlshift__
__rrshift__
__rand__
__rxor__
__ror__
__iadd__ +=
__imul__ *=
__isub__ -=
__idiv__ /=
__itruediv__ __future__ > /=
__ifloordiv__ //=
__imod__ %=
__ipow__ ^=
__ilshift__ <<=
__irshift__ >>=
__iand__ &=
__ixor__
__ior__ |=
__neg__ monadic -
__pos__ monadic +
__abs__ abs built in function
__invert__ monadic ~
__complex__ complex built in function
__int__ int built in function
__long__ long built in function
__float__ float built in function
__oct__ oct built in function
__hex__ hex built in function
__index__
__enter__
__exit__
"""


lifecycle = [
    '__new__',
    '__init__',
    '__del__',
]

comparison = [
    '__cmp__',
    '__eq__',
    '__ne__',
    '__lt__',
    '__gt__',
    '__le__',
    '__ge__',
]

unary = [
    '__pos__',
    '__neg__',
    '__abs__',
    '__invert__',
    '__round__',
    '__floor__',
    '__ceil__',
    '__trunc__',
]

arithmetic = [
    '__add__',
    '__sub__',
    '__mul__',
    '__floordiv__',
    '__div__',
    '__truediv__',
    '__mod__',
    '__divmod__',
    '__pow__',
    '__lshift__',
    '__rshift__',
    '__and__',
    '__or__',
    '__xor__',
]

rarithmetic = [
    '__radd__',
    '__rsub__',
    '__rmul__',
    '__rfloordiv__',
    '__rdiv__',
    '__rtruediv__',
    '__rmod__',
    '__rdivmod__',
    '__rpow__',
    '__rlshift__',
    '__rrshift__',
    '__rand__',
    '__ror__',
    '__rxor__',
]

iassign = [
    '__iadd__',
    '__isub__',
    '__imul__',
    '__ifloordiv__',
    '__idiv__',
    '__itruediv__',
    '__imod__',
    '__ipow__',
    '__ilshift__',
    '__irshift__',
    '__iand__',
    '__ior__',
    '__ixor__',
]

typeconv = [
    '__int__',
    '__long__',
    '__float__',
    '__complex__',
    '__oct__',
    '__hex__',
    '__index__',
    '__coerce__',
]

representation = [
    '__str__',
    '__repr__',
    '__unicode__',
    '__bytes__',
    '__format__',
    '__hash__',
    '__nonzero__',
    '__bool__',
    '__dir__',
    '__sizeof__',
]

attributes = [
    '__getattr__',
    '__setattr__',
    '__delattr__',
    '__getattribute__',
]

containers = [
    '__len__',
    '__getitem__',
    '__setitem__',
    '__delitem__',
    '__iter__',
    '__reversed__',
    '__contains__',
    '__missing__',
]

reflection = [
    '__instancecheck__',
    '__subclasscheck__',
]

callables = [
    '__call__',
]

contextmanagers = [
    '__enter__',
    '__exit__',
]

descriptors = [
    '__get__',
    '__set__',
    '__delete__',
]

copying = [
    '__copy__',
    '__deepcopy__',
]

pickling = [
    '__getinitargs__',
    '__getnewargs__',
    '__getstate__',
    '__setstate__',
    '__reduce__',
    '__reduce_ex__',
]


all = (lifecycle + comparison + unary + arithmetic + rarithmetic + iassign +
       typeconv + representation + attributes + containers + reflection +
       callables + contextmanagers + descriptors + copying + pickling)
