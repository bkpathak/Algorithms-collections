### Recursive Backtracking
In backtracking algorithm we make one choice from the available options at each
decision point. We will keep exploring until we met the final goal state or the
choice is not valid. If the choice is not valid then we backtrack the decision point
one steps above and explore the another available choice. If all the available choices
are exhausted in each decision point then the solution for the problem is not present.

### General Pseudo code for Backtracking algorithm:

 ```python
 def solve( Configuration conf):
   if (no more choices):
     return (conf is a goal state)

   for (all available choices):
     try one choice
     ok = solve(conf with choice c) # recurse
     if(ok):
       return True
     else:
       unmake choice c # Backtrack

  return False # All choices are tried
 ```
