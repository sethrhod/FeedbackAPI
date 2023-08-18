## adding or removing events
 - The Feedback backend api has a route which hosts json data for each event item available for download

  # event_name.json
  - For the user to be able to download the event data in the app the required event data must be added into the correct local directory of the api

  - The directory structure is as follows:

      FeedbackAPI/
        |- event_bundles/
          |- events/
            |- event_name/ (event data)
              |- event_name.json
              |- images/
                |- (images for app)
                |- logo/
                  |- event_name_logo.png
          |- zips/
            |- event_name.zip (compressed event_name folder)


  - The event_name.json file must contain the following attributes:

    {
      "id": "abcd1234",
      "name": "Fictional Tech Summit 2023",
      "date": "2023-09-15T10:30:00",
      "time": "10:30 AM - 6:00 PM",
      "location": "Virtual Event",
      "description": "Fictional Tech Summit 2023 is a virtual event for tech enthusiasts. Join us for a day of exciting sessions and virtual networking.",
      "logo": "/images/logo/fictionaltechsummitlogo.png",
      "registration": "https://www.eventbrite.com/e/fictional-tech-summit-2023-registration-123456789",
      "speakerAPI": "https://sessionize.com/api/v2/abcd1234/view/Speakers",
      "sessionAPI": "https://sessionize.com/api/v2/abcd1234/view/Sessions",
      "sponsorsAPI": "https://fictionaltechsummit.com/sponsors.json",
      "colors": {
        "light": {
          "primary": "#E74C3C",
          "secondary": "#3498DB",
          "background": "#F5F5F5",
          "foreground": "#E0E0E0",
          "card": "#FFFFFF",
          "accent": "#7F8C8D",
          "text": "#333333"
        },
        "dark": {
          "primary": "#E74C3C",
          "secondary": "#3498DB",
          "background": "#111111",
          "foreground": "#1F1F1F",
          "card": "#2B2B2B",
          "accent": "#505050",
          "text": "#FFFFFF"
        }
      }
    }

  - The event_name parent folder must then be zipped and placed in the event_bundles/zips/ directory

  # events.json
  - For the event to be available for the user to download on the app an event object must be added to the events.json file with the following attributes:
      {
        "name": "Atlanta Cloud Conference 2023",
        "date": "2023-03-25T09:00:00",
        "zip_path": "event_bundles/zips/event_Atlcloudconf.zip"
      }
  - The zip path must point to the local path of the zipped file to download because it will be sent in the url in the request to the /download/ route of the api to actually download the contents and store them on the devicemarkdow