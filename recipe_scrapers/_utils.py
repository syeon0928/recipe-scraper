import re

TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M))?'
)


def get_minutes(dom_element):
    try:
        tstring = dom_element.get_text()
        if '-' in tstring:
            tstring = tstring.split('-')[1]  # some time formats are like this: '12-15 minutes'
        matched = TIME_REGEX.search(tstring)
        minutes = int(matched.groupdict().get('minutes') or 0)
        minutes += 60 * int(matched.groupdict().get('hours') or 0)
        return minutes
    except AttributeError:  # if dom_element not found or no matched
        return 0


# Regular expression to match servings
SERVINGS_REGEX = re.compile(r'(?P<servings>\d+)\s*[-–]?\s*(?:\d+)?\s*servings?', re.IGNORECASE)


def get_servings(dom_element):
    try:
        # Extract text from the DOM element
        tstring = dom_element.get_text().strip()

        # Find a match using the SERVINGS_REGEX
        matched = SERVINGS_REGEX.search(tstring)

        # Extract the servings number if found
        if matched:
            servings = int(matched.group("servings"))
            return servings
        else:
            return None  # Return None if no match is found
    except AttributeError:
        # Return None if dom_element is not found or an error occurs
        return None


def normalize_string(string):
    return re.sub(
        r'\s+', ' ',
        string.replace(
            '\xa0', ' ').replace(  # &nbsp;
            '\n', ' ').replace(
            '\t', ' ').strip()
    )


if __name__ == '__main__':
    minute = get_minutes("25 min")
    print(minute)
