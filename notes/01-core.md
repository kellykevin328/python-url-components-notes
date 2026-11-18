# Inspect URL components: implementation

## What the example does

urlsplit separates structure but is not a security validator. Inspect the scheme and host explicitly before making any outbound request.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"https://example.com:8443/a?q=1#part"
```

Expected result:

```json
{
  "scheme": "https",
  "host": "example.com",
  "path": "/a",
  "query": "q=1",
  "fragment": "part"
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
