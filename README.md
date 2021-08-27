# ParseHtmlPage
## Use Library
***
### import parse
```
from parse import Parse
```
***
### create Object
```
text = Parse(sitename="https://example.com", auth=[login, password], method="text")
```
#### required arguments:

> _sitename_
> str() or list()

> _auth_
> *Empty* - "" or [login, password]

> _method_
> str() or dict()
> dict() -> {"https://example.com":_method_}
> method -> "text" or "json"

#### other arguments:
> _infinity_
> False or True

> _interval_
> False or int()
> int() -> 1 equal 1 second