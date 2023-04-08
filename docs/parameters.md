# Custom parameters

You can customize some properties of the image by sending query parameters with the request.

## Size

The size of the image can be changed by passing the `size` parameter. The value must be a number between `32` and `512`.
Default: `64`

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro&size=256
```

## Background color

The background color of the image can be changed by passing the `background` parameter. The value must be either a valid web color or `random`. Default: `lightgrey`

Specific color:

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro&background=limegreen
```

Random color:

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro&background=random
```

## Shape

The shape of the image can be changed by passing the `shape` parameter. The value must be either `circle` or `square`.
Default: `square`

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro&shape=circle
```

## Text color

The text color of the image can be changed by passing the `text` parameter. The value must be a valid web color.
Default: `#282828`

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro&text=white
```

## Combined

You can combine multiple parameters to create a unique avatar.

```
http://127.0.0.1:5000/avatar/?name=Tim+Fisicaro&background=limegreen&text=black&shape=circle&size=512
```
