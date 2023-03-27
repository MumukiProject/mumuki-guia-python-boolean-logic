Let's start with something simple - remember the `not` operator? It's called negation or logical complement and is used to negate a boolean value. For example, if you represent _hunger_ with a boolean parameter `is_hungry`, the contrary will be `not is_hungry`. :no_mouth:

This doesn't seem like a very interesting idea, but it can be used to reuse the logic of a function we have already defined. For example, if we already have a function `is_even`, it is enough to negate it to know whether a number is odd.

```python
def is_odd(number):
  return not is_even(number)
```

> Now it's your turn! Define the function `is_adult` and then `is_minor` from it. Both functions will take an `age`  as an argument, and will return whether it is 18 years or older and whether it is less than 18 years, respectively.
