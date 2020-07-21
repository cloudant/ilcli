# ilcli

`ilcli` (I like commmand line interfaces) is a Python library for
creating CLIs easily and includes cool features.


```python

import ilcli

class mycli(ilcli.Command):
    """
    This is my cool cli
    """
    def _run(self):
        self.out('Running!')

exit(mycli().run())
```

## Contribute!

Help us to improve the compliance-tool. See [CONTRIBUTING.md](CONTRIBUTING.md)

* [Quick start][] guide: https://cloudant.github.io/ilcli

[Quick start]: https://cloudant.github.io/ilcli/quick-start.html

## Installation

```
pip install ilcli
```
