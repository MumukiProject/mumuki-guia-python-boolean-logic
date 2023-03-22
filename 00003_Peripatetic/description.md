Another operator you've already learned about is the logical conjunction (also called _and_), which is true only if the two expressions it operates on are true.

We can chain several of them using the `and` operator and if any of them is false the whole expression will be false.

For example, if you have the function...

```python
 def is_prolific_singer(cds_edited, recitals_performed, recorded_some_dvd):
  return cds_edited >= 10 and recitals_performed > 25 and recorded_some_dvd
```

...it's enough for a singer not to have recorded a DVD to not be considered prolific, even if they have edited more than 10 CDs and given more than 25 recitals. :guitar:

> Define a function `is_peripatetic` that takes the area in which a person works, their country of origin and the number of kilometers they walk per day. A person is peripatetic when they work in philosophy, their country of origin is Greece and likes to walk (he walks more than 2 kilometers per day). For example:
>
> ```python
> ムis_peripatetic("philosophy", "Greece", 5)
True
> ムis_peripatetic("engineering", "Uruguay", 1)
False
> ```
