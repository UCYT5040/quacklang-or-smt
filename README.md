# quacklang or smt

quacklang or smt is a esolang built for ducks.

## Current Limitations

- Arguments can not contain quacklang functions.
  - This is caused because right now Python's `eval` is used to check argument values.
  - You can use Python functions, but it is not recommended because this feature/issue is going to be removed soon.
    - Once this is removed, you will have to import libraries that eval Python for you.
