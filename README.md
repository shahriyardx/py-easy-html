# Easy HTML
Generate HTML using python and also convert to PDF.

# Installation
```sh
pip install py-easy-html
```

# Getting started
General usage
```py
h1 = generate_tag('h1', body='This is a h1', class_name="your_class", id_name="your_id", self_closing=False)
```
> Output
```html
<h1 class="your_class" id="your_id">This is a h1</h1>

<!-- With self_closing=True -->
<h1 class="your_class" id="your_id" />
```

You can also do nested tags
```py
h1 = generate_tag('h1', body=generate_tag('span', body='Span inside h1'))
```
> Output
```html
<h1>
  <span>Span inside h1</span>
</h1>
```

And also multiple nested tags
```py
h1 = generate_tag(
        'h1',
        style={
          "display": "flex",
          "justify-content": "space-between",
          "align-items": "center",
        },
        body=[
            generate_tag('span', body='First Span'),
            generate_tag('span', body='Second'),
        ],
    )
```
> Output
```html
<h1 style="display: flex;justify-content: space-between;align-items: center;">
  <span>First Span</span>
  <span>Second</span>
</h1>
```
