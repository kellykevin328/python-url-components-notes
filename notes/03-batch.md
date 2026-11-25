# Ordered batch processing for Inspect URL components

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
"https://example.com:8443/a?q=1#part"
```

Result:
```json
{
  "scheme": "https",
  "host": "example.com",
  "path": "/a",
  "query": "q=1",
  "fragment": "part"
}
```

## Case 2

Input:
```json
"/relative/path"
```

Result:
```json
{
  "scheme": "",
  "host": null,
  "path": "/relative/path",
  "query": "",
  "fragment": ""
}
```

## Case 3

Input:
```json
"https://[::1]/"
```

Result:
```json
{
  "scheme": "https",
  "host": "::1",
  "path": "/",
  "query": "",
  "fragment": ""
}
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

urlsplit separates structure but is not a security validator. Inspect the scheme and host explicitly before making any outbound request.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
