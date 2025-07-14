# Housing Data API

Repository of data from [JCHS](https://www.jchs.harvard.edu/data-search)


## Testing

Use the following for running https (Mac)
Where cert.pem and key.pem are certificate and key
```python
app.run(ssl_context=('.vscode/cert.pem', '.vscode/key.pem'), debug=False, port=8000, host='0.0.0.0')
```

for http use
```python
if __name__ == '__main__':
    app.run(debug=False, port=8000, host='0.0.0.0')
```
