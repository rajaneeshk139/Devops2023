from flask import Flask, request

app = Flask(__name__)

app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get JSON payload from the webhook
    # Process the webhook payload here
    print(data)
    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

