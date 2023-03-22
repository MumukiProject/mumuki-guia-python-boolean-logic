At an amusement park in town, a new roller coaster :roller_coaster: was installed and we were asked to tell people if they can ride it before they got in line. The requirements to enter the attraction are:

* reach the minimum height of 1.5 m  - or 1.2 m if you're accompanied by an adult;
* not have a heart condition.


> Define a 3-parameters function `can_ride` that receives a person's height in meters, whether they are accompanied by an adult and whether they have a heart condition. For example:
>
> ```python
> ムcan_ride(1.7, False, True)
> False # they cannot ride
>   	# because although their height is over 1.5m,
>   	# they have a heart condition
> ```
