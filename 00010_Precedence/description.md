When a mathematical expression consists of multiple operators, we know that multiplications and divisions are performed before additions and subtractions:

```python
5 * 3 + 8 / 4 - 3 == 14 # it is resolved as 15 + 2 - 3
```

Just as in mathematics, when logical operators are used, expressions are evaluated in a certain order called _precedence_. How's that? :thinking:

For example, look at this function that tells whether Umi will use a credit card :credit_card::

```python
def pays_with_credit_card(interest_free, card, cash_available):
  return interest_free and installments_available(card) >= 3 or cash_available < 100
```

How will this definition be interpreted? Will Umi use credit cards only when payment is interest-free? Or is it enough that Umi has less than $100 in cash?

> Let's find out! Try to figure out what the precedence of boolean operations is. Here are some test examples:
>
>``` python
ムpays_with_credit_card(True, "visa", 320)
```
>
>``` python
ムpays_with_credit_card(False, "visa", 80)
```
>
>``` python
ムpays_with_credit_card(True, "mastercard", 215)
```
>
>``` python
ムpays_with_credit_card(True, "mastercard", 32)
```
>
> However, don't forget you can test as many expressions as you want. When you're done, type `done()`.
