# Examples of PyWeb Scripting Language

## Template Rendering

```py
# Rendering a simple template with variables
output = render_template('template.html', {'title': 'Hello, World!', 'content': 'Welcome to PyWeb!'})
```

## Variable Substitution

```py
# Replacing variables in a string
name = 'John'
message = f'Hello, {name}!'  # Output will be 'Hello, John!'
```

## Conditional Blocks

```py
# Using conditional statements to control flow
if user.is_authenticated:
    output = '<h1>Welcome back!</h1>'
else:
    output = '<h1>Please log in.</h1>'
```

## Loops with HTML Integration

```py
# Looping through a list to create an HTML list
items = ['Item 1', 'Item 2', 'Item 3']
output = '<ul>'
for item in items:
    output += f'<li>{item}</li>'
output += '</ul>'  # Closing the list
```

# Notes
- Ensure the template files are correctly set up for rendering.
- Variable substitution needs to follow the syntax of the scripting language.
- Conditional blocks and loops can be utilized to generate dynamic HTML content.