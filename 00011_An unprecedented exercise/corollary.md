And what if we _delegate_, that is, divide our main problem into several, smaller functions? We could split the logic as follows:
 
```python
def can_focus(infusion, temperature, is_programming):
  return infusion_at_right_temperature(infusion, temperature) and is_programming

def infusion_at_right_temperature(infusion, temperature):  
  return infusion == 'tea' and temperature >= 95 or infusion == 'mate' and temperature == 80
```

**If you delegate properly**, sometimes it's not necessary to alter the order of precedence. Another point in favor of delegation! :muscle:
