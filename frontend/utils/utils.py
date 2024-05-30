import json
import re
import ast

import pandas as pd


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


def parse_settings(settings: str):
    settings = settings.replace("\n", "")
    settings = settings.replace('\"', '"')
    settings = settings.replace("'", '"')
    settings = "{" + settings + "}"
    settings_obj = json.loads(settings)
    return settings_obj


def parse_string_list(list_as_string: str):
    try:
        return ast.literal_eval(list_as_string)
    except:
        return []


def list_to_string_items(list):
    return ','.join(list)


def string_items_to_list(items_string):
    return items_string.split(",")


def build_list_as_string(list):
    if len(list) > 0:
        items = "','".join(list)
        return f"['{items}']"
    else:
        return "[]"


def string_items_to_string_list(items_string):
    if items_string.strip() == '':
        return "[]"
    else:
        return build_list_as_string(string_items_to_list(items_string))


def select_market_by_title(markets, title):
    # Find the selected market dictionary based on the selected title
    return next((market for market in markets if market['title'] == title), None)


def date_col(value):
    return pd.to_datetime(value, format='%Y-%m-%d %H:%M:%S')


def parse_market_settings(market_setting_as_string):
    settings = market_setting_as_string.rstrip(',')  # Remove trailing commas (optional)
    settings = settings.replace("\n", "")
    settings = settings.replace('\"', '"')
    settings = settings.replace("'", '"')
    try:
        return json.loads(settings)
    except json.JSONDecodeError as e:
        print(f"Error parsing settings JSON: {e}")
        return {}


def select_distributor_by_label(distributors, label):
    # Find the selected market dictionary based on the selected title
    return next((distributor for distributor in distributors if distributor['label'] == label), None)