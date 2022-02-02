# in_memory_database

As per the question , operation was suppose to be o(log N) so i decided to go with binary tree datastructure

I'm appending based on the key value and the corresponding value to that key in the tree.
Note that as per the transaction please use upper case SET, GET, UNSET , NUMEQUALTO and END 
Please use python3 in your MAC book for this problem. 

###OUTPUT OF EACH TEST CASE IS AS BELOW:

####Test case 1

```
Alans-MacBook-Pro:in_memory_database alanrodrigues$ python3 main.py 
INPUT:SET x 10
INPUT:GET x
10
INPUT:UNSET x
INPUT:GET x
NULL
INPUT:END
Alans-MacBook-Pro:in_memory_database alanrodrigues$ 
```

####Test case 2

```
Alans-MacBook-Pro:in_memory_database alanrodrigues$ python3 main.py 
INPUT:SET a 10
INPUT:SET b 10
INPUT:NUMEQUALTO 10
2
INPUT:NUMEQUALTO 20
0
INPUT:SET b 30   
INPUT:NUMEQUALTO 10
1
INPUT:END
Alans-MacBook-Pro:in_memory_database alanrodrigues$ 
```


####Test case 3

```
Alans-MacBook-Pro:in_memory_database alanrodrigues$ python3 main.py 
INPUT:BEGIN
INPUT:SET a 10
INPUT:GET a
10
INPUT:BEGIN
INPUT:SET a 20
INPUT:GET a
20
INPUT:ROLLBACK
INPUT:GET a
10
INPUT:ROLLBACK
INPUT:GET a
NULL
INPUT:END
Alans-MacBook-Pro:in_memory_database alanrodrigues$ 
```

####Test case 4

```
Alans-MacBook-Pro:in_memory_database alanrodrigues$ python3 main.py 
INPUT:BEGIN
INPUT:SET a 30
INPUT:BEGIN
INPUT:SET a 40
INPUT:COMMIT
INPUT:GET a
40
INPUT:ROLLBACK
NO TRANSACTION
INPUT:END
Alans-MacBook-Pro:in_memory_database alanrodrigues$ 
```

####Test case 5

```
Alans-MacBook-Pro:in_memory_database alanrodrigues$ python3 main.py 
INPUT:SET a 50
INPUT:BEGIN
INPUT:GET a
50
INPUT:SET a 60
INPUT:BEGIN
INPUT:UNSET a
INPUT:GET a
NULL
INPUT:ROLLBACK
INPUT:GET a
60
INPUT:COMMIT
INPUT:GET a
60
INPUT:END
Alans-MacBook-Pro:in_memory_database alanrodrigues$ 
```

####Test case 6

```
Alans-MacBook-Pro:in_memory_database alanrodrigues$ python3 main.py 
INPUT:SET a 10
INPUT:BEGIN
INPUT:NUMEQUALTO 10
1
INPUT:BEGIN
INPUT:UNSET a
INPUT:NUMEQUALTO 10
0
INPUT:ROLLBACK
INPUT:NUMEQUALTO 10
1
INPUT:COMMIT
INPUT:END
Alans-MacBook-Pro:in_memory_database alanrodrigues$ 
```