import re


def print_error(e):
    print("****Error****")
    print(e)
    print("****End Error ****")


def is_valid_url(url):
    """
  This function checks if a string is a valid URL using a regular expression.

  Args:
      url (str): The URL string to validate.

  Returns:
      bool: True if the URL is valid, False otherwise.
  """

    regex = r"^https?://[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}(?:[/?#][^ \n\t]+)*$"
    return re.match(regex, url) is not None


def find_by_attribute(data_array, attribute_name, value):
    """
  Finds the first object in the array with the specified attribute and value.

  Args:
      data_array: The list of objects to search.
      attribute_name: The name of the attribute to compare.
      value: The value to match in the attribute.

  Returns:
      The first object that matches the criteria, or None if not found.
  """

    return next((obj for obj in data_array if getattr(obj, attribute_name) == value), None)
