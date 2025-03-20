#!usr/bin/python3
"""
Definition of generate_invitations function
"""


def generate_invitations(template_content, attendees):
    """
    My base function
    """
    if not isinstance(template_content, str):
        raise TypeError("template must be a string!")
    if not isinstance(attendees, list) or\
            not all(isinstance(element, dict) for element in attendees):
        raise TypeError("attendees must be a list of dictionnaries")
    if len(template_content) == 0 or len(attendees) == 0:
        raise ValueError("No empty arguments please")

    i = 1

    for attendee in attendees:
        invitation = template_content
        invitation = invitation.replace
        ("{name}", str(attendee.get("name", "N/A")))
        invitation = invitation.replace
        ("{event_title}", str(attendee.get("event_title", "N/A")))
        invitation = invitation.replace
        ("{event_date}", str(attendee.get("event_date", "N/A")))
        invitation = invitation.replace
        ("{event_location}", str(attendee.get("event_location", "N/A")))

        with open(f"output_{i}.txt", 'w', encoding='UTF-8') as file:
            file.write(invitation)

        i += 1
