:bank: Has it ever happened to you that you went to the bank to do something and then found that it was closed? To help clueless people, we're going to develop a function that tells whether the bank is open.

We know that the bank is open on weekdays - except holidays - and within bank opening hours. 

These functions are already defined:

* :clock10: `within_banking_hours`: receives a time (an hour o'clock that can go from 0 to 23) and tells us whether it is within the bank's attention slot.
* :calendar_spiral: `is_weekend`: receives a day and tells us if it is `"Saturday"` or `"Sunday"`.

> Complete the definition of `is_weekday` and then use it to complete the definition of `is_bank_open`.
