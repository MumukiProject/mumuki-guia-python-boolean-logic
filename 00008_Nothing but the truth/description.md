Now let's think about what the truth table that represents the behavior of the function you just wrote would look like.
 
The statement is `is_light_tone`, and the truth value it carries will depend on each color you are evaluating. The final boolean will result from operating on these colors by `has_contrast`:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="padding: 5px 8px">font color is light</th>
	<th class ="text-center" style="padding: 5px 8px">background color is light</th>
	<th class ="text-center" style="padding: 5px 8px">page has contrast</th>
  </tr>
  <tr>
	<td>True</td>
	<td>True</td>
	<td>False</td>
  </tr>
  <tr>
	<td>True</td>
	<td>False</td>
	<td>True</td>
  </tr>
  <tr>
	<td>False</td>
	<td>True</td>
	<td>True</td>
  </tr>
  <tr>
	<td>False</td>
	<td>False</td>
	<td>False</td>
  </tr>
</table>

> Test your `has_contrast` function with the following values and verify if it behaves like the table:
>
>``` python
ムhas_contrast("yellow", "beige")
```
>
>``` python
ムhas_contrast("blue", "purple")
```
>
>``` python
ムhas_contrast("white", "black")
```
