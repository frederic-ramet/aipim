import requests
import streamlit as st

from utils.cookies import get_access_token
from utils.utils import print_error

base_url = st.secrets['BACKEND_BASE_URL']


def fetch_all_products():
    get_all_users_api_url = f"{base_url}/api/v1/user/profiles/"

    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(get_all_users_api_url, headers=headers)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        print_error(f"Error fetching user data: {e}")
        return []


def fetch_user_profile():
    get_user_profile_api_url = f"{base_url}/api/v1/user/profile/"

    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(get_user_profile_api_url, headers=headers)
        response.raise_for_status()
        user_data = response.json().get("data")
        return user_data
    except requests.exceptions.RequestException as e:
        return None
        # st.error(f"Error fetching user profile data: {e}")


def create_user(data):
    # Defining the endpoint of your backend API for creating a user
    create_user_api_url = f"{base_url}/api/v1/auth/register/"

    # Making a POST request to the backend API with user data
    response = requests.post(create_user_api_url, json=data)

    # Check if the request was successful
    if response.status_code == 201:
        st.success("User created successfully!")
        print(f"Status of User Register! {response.json()}")
    else:
        st.error(f"Failed to create user. Please try again: {response.text}")
        print(f"Failed to create user. Please try again: {response.text}")

    return response


def fetch_user_profile_by_id(user_id):
    get_user_profile_api_url = f"{base_url}/api/v1/user/profile/{user_id}"

    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(get_user_profile_api_url, headers=headers)
        response.raise_for_status()
        user_result = response.json().get("data")
        return user_result
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user profile by id: {e}")


def update_user_by_id(user_id, update_data):
    update_user_profile_api_url = f"{base_url}/api/v1/user/update-profile/{user_id}"

    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.patch(update_user_profile_api_url, headers=headers, json=update_data)
    # Check if the request was successful
    if response.status_code == 200:
        st.success(f"User updated successfully!: {response.json()}")
    else:
        st.error(f"Failed to update/edit user's profile. Please try again: {response.text}")
        print(f"Failed to update/edit user's profile: {response.text}")

    return response


def delete_user_by_id(user_id, status):
    update_user_profile_api_url = f"{base_url}/api/v1/user/account/{user_id}/status?activate_account={status}"

    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.delete(update_user_profile_api_url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        st.success(f"User deleted(deactivated) successfully!: {response.json()}")
    else:
        st.error(f"Failed to delete user's profile. Please try again: {response.text}")
        print(f"Failed to delete user's profile: {response.text}")

    return response


def pull_user_repo_by_id(user_id):
    pull_user_repo_api_url = f"{base_url}/api/v1/client/{user_id}/git-repo/update"
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.put(pull_user_repo_api_url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        st.success(f"User's repository updated successfully!: {response.json()}")
    else:
        st.error(f"Failed to updated user's repository. Please try again: {response.text}")
        print(f"Failed to updated user's repository: {response.text}")

    return response