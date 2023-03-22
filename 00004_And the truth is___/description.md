In Boolean logic, the behavior of an operator can be defined with a _truth table_, where **A** and **B** are the expressions or truth values operated on, and the symbol **^** represents the conjunction.

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="width: 75px">A</th>
	<th class ="text-center" style="width: 75px">B</th>
	<th class ="text-center" style="width: 100px">A ^ B</th>
  </tr>
  <tr>
	<td>True</td>
	<td>True</td>
	<td>True</td>
  </tr>
  <tr>
	<td>True</td>
	<td>False</td>
	<td>False</td>
  </tr>
  <tr>
	<td>False</td>
	<td>True</td>
	<td>False</td>
  </tr>
  <tr>
	<td>False</td>
	<td>False</td>
	<td>False</td>
  </tr>
</table>

In the world of logic these expressions are called _propositions_. But what things can be a proposition? :thought_balloon: They need only have a truth value, that is, any boolean expression can be one.

> To check it, test your function `is_peripatetic` in the console with the following values ​​and check if it behaves as in the table:
>
>``` python
ムis_peripatetic("athletics", "Argentina", 10)
```
>
>``` python
ムis_peripatetic("philosophy", "Argentina", 3)
```
>
>``` python
ムis_peripatetic("engineering", "Canada", 1)
```
>
>``` python
ムis_peripatetic("philosophy", "Greece", 5)
```
