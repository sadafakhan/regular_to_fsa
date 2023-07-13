# regular_to_fsa

```regular_to_fsa``` takes a right-regular grammar from the input and returns an FSA in carmel format.

Args: 
* ```input_file```: a file containing a right-regular grammar, as represented by production rules. Each rule is of the form (A => t B) or (A => t), where t is a terminal symbol. 

Returns: 
* ```output_file```: an FSA in the carmel format 

To run: 
```
cat input_file | ./reg_to_fsa.sh > output_file
```

HW3 OF LING570 (10/23/2021)