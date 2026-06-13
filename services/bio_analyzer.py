import re


def convert_count(value):
    """
    Convert Instagram counts:
    41.6K -> 41600
    2M -> 2000000
    850 -> 850
    """

    value = value.upper().strip()

    try:
        if "K" in value:
            return float(value.replace("K", "")) * 1000

        elif "M" in value:
            return float(value.replace("M", "")) * 1000000

        else:
            return float(value)

    except:
        return 0


def analyze_bio(text):

    data = {
        "username": "Not Found",
        "posts": "0",
        "followers": "0",
        "following": "0"
    }

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        # Username
        if data["username"] == "Not Found" and line != "":
            data["username"] = line

        # Posts
        if "post" in line.lower():

            match = re.search(r'([\d\.KMkm]+)', line)

            if match:
                data["posts"] = match.group(1)

        # Followers
        if "followers" in line.lower():

            match = re.search(r'([\d\.KMkm]+)', line)

            if match:
                data["followers"] = match.group(1)

        # Following
        if "following" in line.lower():

            match = re.search(r'([\d\.KMkm]+)', line)

            if match:
                data["following"] = match.group(1)

    # Numeric values
    data["followers_count"] = convert_count(data["followers"])
    data["following_count"] = convert_count(data["following"])
    data["posts_count"] = convert_count(data["posts"])

    return data