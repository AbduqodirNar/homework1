def typeBasedTransformer(**kwargs):

  transformed_values = {}
  for key, value in kwargs.items():
    if isinstance(value, (int, float)):
      transformed_values[key] = value ** 2
    elif isinstance(value, str):
      transformed_values[key] = value[::-1]
    elif isinstance(value, bool):
      transformed_values[key] = not value
    elif isinstance(value, (list, tuple)):
      transformed_values[key] = value[::-1]
    elif isinstance(value, dict):
      transformed_values[key] = {v: k for k, v in value.items()}
    else:
      transformed_values[key] = value

  return transformed_values

result = typeBasedTransformer(
    number=4,
    text="Hello",
    boolean=True,
    my_list=[1, 2, 3],
    my_dict={"a": 1, "b": 2}
)

print(result)
