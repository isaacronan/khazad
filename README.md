# khazad

Flask nanoservice to generate random JSON data of any expressible structure.

## Request Format

The service exposes a single endpoint:

`POST /config`

The request body is any **CONFIG** object of the following recursive structure (where only the **type** is mandatory, and *defaults* are indicated in *italics*):

### Pool

```javascript
{
    type: 'pool',
    values: [{
        weight: number,
        value: CONFIG
    }]
}
```

This will resolve to a single, random value from a pool of weighted values.

* **values:** *[{ value: { type: 'fixed' }}]* - array (length >= 1) of objects
    * **weight:** *1* - integer >= 0
    * **value:** *{ type: 'fixed' }* - a CONFIG object

### Object

```javascript
{
    type: 'object',
    fields: [{
        label: string,
        value: CONFIG,
        presence: number
    }],
}
```

This will resolve to an object with certain potential fields.

* **fields:** *[]* - array (length >= 0) of objects
    * **label:** *''* - field label i.e. key, attribute name, etc.
    * **value:** *{ type: 'fixed' }* - a CONFIG object
    * **presence:** *1* - floating point number in range [0, 1] indicating the probability of the field's presence in the resulting object

### Array

```javascript
{
    type: 'array',
    minlength: number,
    maxlength: number,
    value: CONFIG
}
```

This will resolve to an array of random length.

* **minlength:** *0* - integer >= 0
* **maxlength:** *0* - integer >= minlength
* **value:** *{ type: 'fixed' }* - a CONFIG object

### Number

```javascript
{
    type: 'number',
    min: number,
    max: number,
    scale: number
}
```

This will resolve to a random number.

* **min:** *0* - floating point number
* **max:** *0* - floating point number >= min;
* **scale:** *0* - integer >= 0 indicating the number of decimal places

### Fixed

```javascript
{
    type: 'fixed',
    values: [any]
}
```

This will resolve to a random value from a fixed set of values.

* **values:** *[null]* - array (length >= 1) of JSON values

## Response Format

The response will be a JSON value whose structure corresponds to the CONFIG object in the request.

## Docker Build

The Docker build expects a single argument to indicate the port of the REST service:

```
docker image build --tag khazad-image --build-arg PORT=1420 ~/path/to/khazad
```