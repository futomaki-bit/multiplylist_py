# multiplylist_py
Multiply everything in a list in Python

### Goal: ###
- Testing more in Python

### Results: ###

**Affecting the List:**
``` Python
for index in range(len(randomList)):
    randomList[index] *= m
```

``` Python
randomList = [i*m for i in randomList]
```

**No effect on the List:**
``` Python
# No effect
for item in randomList:
    item *= m
```
