Let's do some transformations. First, replace the statements `font color is light` and `background color is light` with generic statements `A` and `B`. Then, represent the operation performed by `has contrast` with the symbol `⊻`. What we get is... a new truth table! :tada:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="width: 75px">A</th>
	<th class ="text-center" style="width: 75px">B</th>
	<th class ="text-center" style="width: 100px">A ⊻ B</th>
  </tr>
  <tr>
	<td>V</td>
	<td>V</td>
	<td>F</td>
  </tr>
  <tr>
	<td>V</td>
	<td>F</td>
	<td>V</td>
  </tr>
  <tr>
	<td>F</td>
	<td>V</td>
	<td>V</td>
  </tr>
  <tr>
	<td>F</td>
	<td>F</td>
	<td>F</td>
  </tr>
</table>

This behavior exists as a logic operator and is called `xor` or exclusive disjunction.
 
Unlike `and`, `or`, and `not`, `xor` is seldom defined in programming languages. :cry: However, now that you know how it works, if you ever need it you can define it on your own. :wink:

> Let's check our knowledge! Define the generic function `xor`, which takes two booleans and returns the corresponding truth value.
