from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from tags import get_relevant_tags
from food import search_food
from food import display_carbs


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms_reply():
    # Create a MessagingResponse object to generate TwiML.
    resp = MessagingResponse()

    # See if the number of images in the text message is greater than zero.
    if request.form['NumMedia'] != '0':

        # Grab the image URL from the request body.
        image_url = request.form['MediaUrl0']
        tags = get_relevant_tags(image_url)

        # print the best guest
        print (tags[0:3])

        # search for the food ID
        food_id = search_food(', '.join(tags[0:1]))
        print food_id

        carbs = float(display_carbs(food_id))
        print type(carbs)

        #resp.message ('Fruit: '+ tags[0] + ', ' + carbs + ' g carb(s)')

        if carbs < 15:
            resp.message ('Fruit: '+ tags[0] + ', ' + str(carbs) + ' g carb(s) '+ ' Keto Friendly, you are good to go!')
        else :
            resp.message ('Fruit: '+ tags[0] + ', ' + str(carbs) + ' g carb(s)' + ' Not Keto Friendly!') 

    else:
        resp.message('Please send an image.')

    return str(resp)


if __name__ == '__main__':
    app.run()