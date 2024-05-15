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