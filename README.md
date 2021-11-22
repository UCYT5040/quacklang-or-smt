# quacklang or smt

quacklang or smt is a esolang built for ducks.

## Current Limitations

- Arguments are limited.
  - Only strings and numbers are allowed.
    - Be Carful! Do NOT run code like this: `"hi"+exit()+"hi"`. The interpreter is not powerful enough to see that this is bad.
    - If you want to help out with this, try finding a workaround to run Python without matching `["'].*["'].*["'].*["']`
      - Open an issue or pull request to contribute.
      - Strings like `"hi aren't you gonna leave? i can't"` wont work with that pattern but we have a solution when implemented.
