import os

def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data
        invitation = template
        invitation = invitation.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

        # Generate the output file name
        output_filename = f"output_{index}.txt"

        # Write the processed template to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)
    
    print(f"{len(attendees)} invitation files generated successfully.")

