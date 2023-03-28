Oops! That means that when short of cash, Umi will use credit cards even if they carry interests. :money_with_wings: 

Did you figure out the precedence of boolean operations? :thinking: Just in case, here's a table with their precedence and some operations we've seen (and others we haven't):

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="width: 10px">Precedence</th>
	<th class ="text-center" style="width: 75px">Operation</th>
	<th class ="text-center" style="width: 75px">Description</th>
  </tr>
  <tr>
	<td>1</td>
	<td>**</td>
	<td>Exponentiation</td>
  </tr>
  <tr>
	<td>2</td>
	<td>*,  /,  %</td>
	<td>Multiplication, division, remainder</td>
  </tr>
  <tr>
	<td>3</td>
	<td>+,  -</td>
	<td>Sum, remain</td>
  </tr>
  <tr>
	<td>4</td>
	<td>in,  <,  <=,  >,  >=,  ==,  !=</td>
	<td>Belonging, comparisons</td>
  </tr>
  <tr>
	<td>5</td>
	<td>not</td>
	<td>Logical Negation</td>
  </tr>
  <tr>
	<td>6</td>
	<td>and</td>
	<td>Logical conjunction</td>
  </tr>
  <tr>
	<td>7</td>
	<td>or</td>
	<td>Logical disjunction</td>
  </tr>
</table>

In this table, the precedence goes from highest to lowest, that is, priority 1 is the highest and priority 7 is the lowest :dizzy_face:. For example, if we do...

``` python
8 + 2 * 3 < 15 and not 5 == 4
```

...we'll get `True` since it resolves the operations in this order:

1. `2 * 3` which returns `6` then: `8 + 6 < 15 and not 5 == 4`
2. `8 + 6` which returns `14` then: `14 < 15 and not 5 == 4`
3. `14 < 15` which returns `True` then: `True and not 5 == 4`
4. `5 == 4` which returns `False` then: `True and not False`
5. `not False` which returns `True` then: `True and True`
6. `True and True` which finally returns `True`.
