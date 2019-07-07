# flagz 🇲🇽 🇨🇿 🇧🇾

A Python package that makes working with emoji flags ([regional indicator symbols](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol)) comfy.

### Install

```
pip install flagz
```

### Usage

```python
import flagz


flag = flagz.by_code('ca')
print(flag)  # 🇨🇦
```

If no flag exists, a `ValueError` will be raised

### Run tests

```
git clone https://github.com/kennell/flagz
cd flagz
pip install -e .
pytest
```
