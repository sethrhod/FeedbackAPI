import psycopg2
import json
import logging
import requests

# a function that sorts the feedback by speaker

def sort_feedback_by_speaker():
    speaker_feedback = []
    speakers = fetch_speakers_data()
    feedback = organize_feedback()
    for speaker in speakers:
        speaker_feedback.append({
            "speaker": speaker['fullName'],
            "sessions": []
        })
        for session in speaker['sessions']:
            speaker_feedback[-1]['sessions'].append({
                "sessionid": session['id'],
                "feedback": []
            })
            for feedback_item in feedback:
                if str(session['id']) == str(feedback_item['sessionid']):
                    speaker_feedback[-1]['sessions'][-1]['feedback'].append(
                        feedback_item['feedback'])
    return speaker_feedback


def fetch_speakers_data():
    response = requests.get(
        "https://sessionize.com/api/v2/curiktb3/view/Speakers")
    data = response.json()
    speakers = []
    for speaker in data:
        speakers.append({
            "fullName": speaker['fullName'],
            "sessions": speaker['sessions']
        })
    return speakers


def organize_feedback():
    rows = get_all_feedback()
    data = []
    for row in rows:
        data.append({
            "sessionid": row[1],
            "feedback": row[2]
        })
    return data


def get_all_feedback():
    with open('config.json') as f:
        config = json.load(f)

    try:
        conn = psycopg2.connect(
            dbname=config['<database-name>'],
            user=config['<admin-username>'],
            host=config['<server-name>'],
            password=config['<admin-password>']
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM feedback;")
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        logging.info("Error while connecting to PostgreSQL", e)
        print(e)


if __name__ == "__main__":
    print(sort_feedback_by_speaker())
