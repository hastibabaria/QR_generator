from flask import Flask, render_template, request, send_file
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to bytes
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Convert bytes to base64 string
    img_str = base64.b64encode(img_bytes).decode('utf-8')

    return render_template('display_qr.html', qr_image=img_str)

    return render_template('display_qr.html', qr_image=img_buffer)
if __name__ == '__main__':
    app.run(debug=True)
