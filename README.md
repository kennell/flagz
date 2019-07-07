# emojiflags

A python package that makes working with emoji flags ([regional indicator symbols](https://en.wikipedia.org/wiki/Regional_Indicator_Symbol)) comfy.

### Install

```
pip install emojiflags
```

### Usage

```python
import emojiflags


flag = emojiflags.get_by_code('ca')
print(flag)  # 🇨🇦
```

### Run tests

```
git clone https://github.com/kennell/emojiflags
cd emojiflags
pip install -e .
pytest
```