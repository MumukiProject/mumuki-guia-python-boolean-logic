What if it's enough that one of several conditions is satisfied to assert that an expression is true? We can use another operator you already know: the logical disjunction `or`! :bulb:

In _T.E.G._ -  a board  game closely-related to [_Risk_](https://en.wikipedia.org/wiki/Risk_(game)) - a player can win in two ways: by fulfilling his secret objective or by reaching the general objective of conquering 30 countries:

```python
def win(met_secret_goal, number_of_countries_conquered):
  return met_secret_objective or number_of_countries_conquered >= 30
```

> Try the following expressions in the console:
>
>``` python
ムwin(True, 25)
```
>
>``` python
ムwin(False, 30)
```
>
>``` python
ムwin(False, 20)
```
>
>``` python
ムwin(True, 31)
```
> Based on these examples and the console, build - i.e. in a paper notebook - the truth table of the logical disjunction
