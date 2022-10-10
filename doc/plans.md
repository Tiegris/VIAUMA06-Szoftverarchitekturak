# Design ideas

Latex táblázatba exportálás
Hozzanak létre egy olyan alkalmazást, amely képes többfajta adatforrásból (json, csv, excel, adatbázis, markdown) szépen formázott latex táblázatot generálni. Az alkalmazás legyen bővíthető, hogy más formátumba generálást is támogasson.

## High level ideas

Console app implemented in Kotlin/Python. Easy to use cli tool with flags and help.

Example usage:

```bash
tex-table --input-type=json --template-arg tabular="|p{3cm}||p{3cm}|p{3cm}|p{3cm}|" path/to/input.json

tex-table --input-type=csv --output-template path/to/output_template path/to/input.csv


```

## Architecture

Reads input data, parses it to internal representation. Using template files it can generate outputs. We define a default template to generate latex tables, provide documentation on how to define your own template.

## Features

