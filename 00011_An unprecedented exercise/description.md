If you have paid attention to the previous function, you'll have noticed that the operation with the highest precedence is the negation `!`, followed by the conjunction `&&` and finally the disjunction `||`. But what if you want to alter the order in which they resolve? :thought_balloon:

Just as in mathematics, we can use parentheses to group the operations we want to perform first.

> Let's try it out! Umi can concentrate on programming only while taking infusions, but not just any infusion. It has to be _mate_ :mate: at exactly 80ºC or tea :tea: that is at least 95ºC.
>
> Define the function `can_focus` that receives a drink, its temperature and a boolean that tells us whether Umi is programming:
>
``` python
>ムcan_focus('tea', 100, True)
>True
>
>ムcan_focus('mate', 70, True)
False
>
>ムcan_focus('tea', 95, False)
>False
```
> Try to solve it with a single function! Then we'll see how it would be if we divided the problem into several functions.
