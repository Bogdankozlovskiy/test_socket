main = b"""
<h1>hello main page</h1>
<img src='data:image/jpeg;base64,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'>
"""

shop = b"""
<h1>hello shop page</h1>
"""